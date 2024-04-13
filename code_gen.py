import streamlit as st
import re
from jinja2 import Template

import google.generativeai as genai
from openai import OpenAI

from constants import OPENAI_API_KEY
from templates import SYSTEM_PROMPT, PLAN_STEPS_TEMPLATE, PLAN_GENERATION_TEMPLATE, CODE_GENERATION_TEMPLATE, CODE_CORRECTION_TEMPLATE
from utils import extract_code_segments, stream_data


def generate_code_plan(query: str):

    prompt = Template(PLAN_GENERATION_TEMPLATE).render(
            context=SYSTEM_PROMPT, 
            query=query, 
            plan_template=PLAN_STEPS_TEMPLATE
        )

    plan = st.session_state.google_gemini.generate_content(
        prompt, 
        generation_config=genai.types.GenerationConfig(temperature=0.01)
    )

    try:
        _ = eval(plan.text.replace("`", ""))
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("Here is a plan of how to code for your ask:  \n\n" + plan.text))
    except Exception as e:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("Error in executing plan dictionary:  \n\n" + str(e)))

    return plan.text


def generate_and_execuate_code(query: str, code_plan: str):

    code_prompt = Template(CODE_GENERATION_TEMPLATE).render(
        context=SYSTEM_PROMPT,
        query=query,
        code_plan=code_plan
    )

    code_blob = st.session_state.google_gemini.generate_content(
        code_prompt,
        generation_config=genai.types.GenerationConfig(temperature=0.01)
    )

    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data("Here is the generated code:  \n\n" + code_blob.text))
    
    code = extract_code_segments(code_blob.text)

    if code is None:
        # TODO: consider adding retry schema
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data("No code snippet was extracted in generation. Please try again."))
        return
    
    try:
        exec(code)
        return
    except Exception as e:
        
        # Here, do the try once more schema using a different model
        with st.chat_message("agent", avatar="🤖"):
            st.write(f"Error: {e} when executing generated code.")
        
        retry_code = correct_code(query, code_plan, code_blob.text, str(e))
        try:
            exec(retry_code)
        except Exception as e:
            with st.chat_message("agent", avatar="🤖"):
                st.write(f"Error: {e} when executing re-generated code.")
            return


def correct_code(query: str, code_plan: str, error_code_blob: str, error: str, model="gpt-4-turbo-2024-04-09"):

    prompt = Template(CODE_CORRECTION_TEMPLATE).render(
            context=SYSTEM_PROMPT,
            query=query,
            code_plan=code_plan,
            wrong_code=error_code_blob,
            error=error
        )

    client = OpenAI(api_key=OPENAI_API_KEY)
    retry_response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
    retry_code_blob = retry_response.choices[0].message.content
    
    with st.chat_message("agent", avatar="🤖"):
        st.write_stream(stream_data("Correct Code Attempt: \n\n" + retry_code_blob))
    try:
        retry_code_blob = extract_code_segments(retry_code_blob)
    except Exception as e:
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(f"Error in extracting code segments: {e}"))
        return

    return retry_code_blob

def beta_viewagent():

    st.warning("This is a beta feature. Please ask questions related to the conference. The agent is still learning.")
    st.write("We wish to build this agent to actively plan and execute streamlit code to address user questions. Still WIP")

    if query := st.chat_input("Ask Anything!", key='beta_chat'):
        
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)

        plan = generate_code_plan(query)
        generate_and_execuate_code(query, plan)

        