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
        plan_msg = "Here is a plan of how to code for your ask:  \n\n" + plan
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(plan_msg))
        st.session_state.chat_messages.append({"role": "assistant", "content": plan_msg})
    except Exception as e:
        err_msg = "Error in executing plan dictionary:  \n\n" + str(e)
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(err_msg))
        st.session_state.chat_messages.append({"role": "assistant", "content": err_msg})

    return plan


def hack_check(code: str):
    
    if ("API_KEY" in code) or ('bash' in code) or ('ENV' in code) or('exec' in code) or ('eval' in code):
        hack_msg = "Potential hacking attempt detected. Don't do it."
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(hack_msg))
        st.session_state.chat_messages.append({"role": "assistant", "content": hack_msg})
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
    st.session_state.chat_messages.append({"role": "assistant", "content": code_blob.text})
    
    code = extract_code_segments(code_blob.text)
    if code is None:
        err_msg = "No code snippet was extracted in generation. Please try again."
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(err_msg))
        st.session_state.chat_messages.append({"role": "assistant", "content": err_msg})
        return
    
    hack_check(code)

    try:
        exec(code, globals())
        return code
    
    except Exception as e:
        code_error = str(e)
        retry_cnt = 1

        retry_msg = f"Oops! Error: {e} when executing generated code. Let me try again..."
        with st.chat_message("agent", avatar="🤖"):
            st.markdown(retry_msg)
        st.session_state.chat_messages.append({"role": "assistant", "content": retry_msg})

        while retry_cnt <= st.session_state.code_generation_retry:
            code = correct_code(query, code_plan, code, code_error)
            hack_check(code)
            try:
                exec(code, globals())
                return code
            except Exception as e:
                code_error = str(e)
                retry_msg = f"Oops! Error: {e} when executing re-generated code. Let me try again..."
                with st.chat_message("agent", avatar="🤖"):
                    st.markdown(retry_msg)
                st.session_state.chat_messages.append({"role": "assistant", "content": retry_msg})

            retry_cnt += 1
        
        show_give_up_message(query)
        
        
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
    st.session_state.chat_messages.append({"role": "assistant", "content": retry_code_blob})

    try:
        retry_code_blob = extract_code_segments(retry_code_blob)
    except Exception as e:
        err_msg = f"No luck here. Error in extracting code segments: {e}"
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(err_msg))
        st.session_state.chat_messages.append({"role": "assistant", "content": err_msg})
        return

    return retry_code_blob


def show_give_up_message(query):

    prompt = Template(WHIP_RESPONSE_TEMPLATE).render(query=query)

    give_up_response = st.session_state.openai_client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.01,
    )

    give_up_msg = give_up_response.choices[0].message.content
    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data(give_up_msg))
    st.session_state.chat_messages.append({"role": "assistant", "content": give_up_msg})


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

    msg = response.choices[0].message.content
    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data(msg))
    st.session_state.chat_messages.append({"role": "assistant", "content": msg})

    return msg


def alpha_view_agent(query=None):

    st.session_state.logger.info(f"USER {st.session_state.session_id} : AGENT : {query}")

    if query is None:
        if query := st.chat_input("Try ask me anything", key="query"):
            run_agent(query)
    else:
        run_agent(query)


def run_agent(query):

    # BLOCK 1: Classify if the query is relevant
    relevance_prompt = Template(QUERY_RELEVANCE_TEMPLATE).render(
        context=SYSTEM_PROMPT,
        query=query
    )

    relevant = boolean_classification(relevance_prompt)
    if not relevant:
        with st.chat_message("agent", avatar="🤖"):
            reject_msg = "The request is not relevant for this project. AMA sometimes don't mean AMA."
            st.write_stream(stream_data(reject_msg))
            st.session_state.chat_messages.append({"role": "assistant", "content": reject_msg})
        return
    
    codegen_prompt = Template(CODEGEN_CLASSIFICATION_TEMPLATE).render(
        context=SYSTEM_PROMPT,
        query=query
    )
    require_codegen = boolean_classification(codegen_prompt)
    
    if require_codegen:
        wait_msg = "Let me try to generate some code to fulfill this ask. Hold on..."
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(wait_msg))    
        st.session_state.chat_messages.append({"role": "assistant", "content": wait_msg})
        plan = generate_code_plan(query, llm=st.session_state.code_planer)
        code = generate_and_execuate_code(query, plan)
        if code is not None:
            st.session_state.chat_messages.append({"role": "assistant", "content": "Code execution successful.", "source": query})
            st.session_state.exec_code[query] = code
    else:
        generate_generic_answer(query)

        