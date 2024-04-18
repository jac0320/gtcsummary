import streamlit as st
from jinja2 import Template
from exceptions import PotentialHackingAttempt

import google.generativeai as genai

from templates import (
    SYSTEM_PROMPT, 
    PLAN_STEPS_TEMPLATE, 
    PLAN_GENERATION_TEMPLATE, 
    CODE_GENERATION_TEMPLATE, 
    CODE_CORRECTION_TEMPLATE,
    CODEGEN_CLASSIFICATION_TEMPLATE,
    QUERY_RELEVANCE_TEMPLATE,
    WHIP_RESPONSE_TEMPLATE,
    GENERAL_AGENT_TEMPLATE
)
from utils import extract_code_segments, stream_data


def boolean_classification(prompt, model='gpt-3.5-turbo', show_output=False, show_prefix=""):
    """
    Classify the query to determine if it requires code generation at all.
    """

    classification = st.session_state.openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.01,
        max_tokens=2,
    )

    classification_content = classification.choices[0].message.content.lower()

    if show_output:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(show_prefix + classification_content))

    if "true" in classification_content:
        return True
    elif "false" in classification_content:
        return False
    else:
        return False


def generate_code_plan(query: str, llm="openai", model='gpt-3.5-turbo'):

    prompt = Template(PLAN_GENERATION_TEMPLATE).render(
            context=SYSTEM_PROMPT, 
            query=query, 
            plan_template=PLAN_STEPS_TEMPLATE
        )

    if llm == "OpenAI":
        response = st.session_state.openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.01,
        )
        plan = response.choices[0].message.content
    elif llm == "Gemini":
        response = st.session_state.gemini_client.generate_content(
            prompt, 
            generation_config=genai.types.GenerationConfig(temperature=0.01)
        )
        plan = response.text
    else:
        raise ValueError("Invalid LLM model specified. Please choose between 'openai' or 'gemini'.")

    try:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("Here is a plan of how to code for your ask:  \n\n" + plan))
    except Exception as e:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("Error in executing plan dictionary:  \n\n" + str(e)))

    return plan


def hack_check(code: str):
    
    if "API_KEY" in code:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("Potential hacking attempt detected. Don't do it."))
        raise PotentialHackingAttempt("Potential hacking attempt detected. Please refrain from using system level commands.")
    

def generate_and_execuate_code(query: str, code_plan: str):

    code_prompt = Template(CODE_GENERATION_TEMPLATE).render(
        context=SYSTEM_PROMPT,
        query=query,
        code_plan=code_plan
    )

    code_blob = st.session_state.gemini_client.generate_content(
        code_prompt,
        generation_config=genai.types.GenerationConfig(temperature=0.01)
    )

    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data("Here is the generated code:  \n\n" + code_blob.text))
    
    code = extract_code_segments(code_blob.text)
    if code is None:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("No code snippet was extracted in generation. Please try again."))
        return ""
    
    hack_check(code)

    try:
        exec(code, globals())
    except Exception as e:
        code_error = str(e)
        retry_cnt = 1
        with st.chat_message("agent", avatar="🤖"):
                st.markdown(f"Oops! Error: {e} when executing generated code. Let me try again...")

        while retry_cnt <= st.session_state.code_generation_retry:
            code = correct_code(query, code_plan, code, code_error)
            hack_check(code)
            try:
                exec(code, globals())
                return code
            except Exception as e:
                code_error = str(e)
                with st.chat_message("agent", avatar="🤖"):
                    st.markdown(f"Oh no... Error: {e} when executing re-generated code. Let me try again...")

            retry_cnt += 1
        
        show_give_up_message(query)

    return code
        
        
def correct_code(query: str, code_plan: str, error_code_blob: str, error: str, model="gpt-4-turbo-2024-04-09"):

    prompt = Template(CODE_CORRECTION_TEMPLATE).render(
            context=SYSTEM_PROMPT,
            query=query,
            code_plan=code_plan,
            wrong_code=error_code_blob,
            error=error
        )

    retry_response = st.session_state.openai_client.chat.completions.create(
        model=model, 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.01,
    )

    retry_code_blob = retry_response.choices[0].message.content
    
    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data("Correct Code Attempt: \n\n" + retry_code_blob))

    try:
        retry_code_blob = extract_code_segments(retry_code_blob)
    except Exception as e:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(f"No luck here. Error in extracting code segments: {e}"))
        return

    return retry_code_blob


def show_give_up_message(query):

    prompt = Template(WHIP_RESPONSE_TEMPLATE).render(query=query)

    give_up_response = st.session_state.openai_client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.01,
    )

    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data(give_up_response.choices[0].message.content))


def generate_generic_answer(query: str, model='gpt-3.5-turbo'):

    prompt = Template(GENERAL_AGENT_TEMPLATE).render(
        context=SYSTEM_PROMPT,
        query=query
    )
    
    response = st.session_state.openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.01,
    )

    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data(response.choices[0].message.content))

    return response.choices[0].message.content


def alpha_viewagent():

    st.warning("This is a beta feature. We wish to build an code-generation agent to go beyond rigid templates!")

    if query := st.chat_input("Ask Anything! Randomly pick a note written by Site and show it to me.", key='beta_chat'):
        st.session_state.logger.info(f"USER {st.session_state.session_id} : AGENT : {query}")
        if query in st.session_state.agent_session["query"]:

            with st.chat_message("User", avatar="😀"):
                st.markdown(query)

            if st.session_state.agent_session["query"][query] == "code":

                with st.chat_message("agent", avatar="🤖"):
                    plan = st.session_state.agent_session["plan"].get(query)
                    if plan is not None:
                        st.write_stream(stream_data(plan))
                    
                    response = st.session_state.agent_session["response"].get(query)
                    if response is not None:
                        st.code(response)
                        exec(response, globals())
            
            elif st.session_state.agent_session["query"][query] == "answer":
                with st.chat_message("agent", avatar="🤖"):
                    st.write_stream(stream_data(st.session_state.agent_session["response"].get(query)))

            return
        
        else:
            with st.chat_message("User", avatar="😀"):
                st.markdown(query)
            st.session_state.agent_session["query"][query] = True

        # BLOCK 1: Classify if the query is relevant
        relevance_prompt = Template(QUERY_RELEVANCE_TEMPLATE).render(
            context=SYSTEM_PROMPT,
            query=query
        )

        relevant = boolean_classification(relevance_prompt)
        if not relevant:
            with st.chat_message("agent", avatar="🤖"):
                st.write_stream(stream_data("The request is not relevant for this project. AMA sometimes don't mean AMA."))
            return
        
        codegen_prompt = Template(CODEGEN_CLASSIFICATION_TEMPLATE).render(
            context=SYSTEM_PROMPT,
            query=query
        )
        require_codegen = boolean_classification(codegen_prompt)
        
        if require_codegen:
            with st.chat_message("agent", avatar="🤖"):
                st.write_stream(stream_data("Let me try to generate some code to fulfill this ask. Hold on..."))    
            plan = generate_code_plan(query, llm=st.session_state.code_planer)
            code = generate_and_execuate_code(query, plan)
            st.session_state.agent_session["query"][query] = "code"
            st.session_state.agent_session["plan"][query] = plan
            st.session_state.agent_session["response"][query] = code
        else:
            answer = generate_generic_answer(query)
            st.session_state.agent_session["query"][query] = "answer"
            st.session_state.agent_session["response"][query] = answer

        