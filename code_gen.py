import streamlit as st
import re
from jinja2 import Template

import google.generativeai as genai
from openai import OpenAI

from constants import OPENAI_API_KEY
from templates import SYSTEM_PROMPT, PLAN_STEPS_TEMPLATE
from utils import extract_code_segments, stream_data


def beta_viewagent():

    st.warning("This is a beta feature. Please ask questions related to the conference. The agent is still learning.")
    st.write("We wish to build this agent to actively plan and execute streamlit code to address user questions. Still WIP")

    if query := st.chat_input("Ask Anything!", key='beta_chat'):
        
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)

        prompt = PLAN_GENERATION_TEMPLATE.format(context=SYSTEM_PROMPT, query=query, plan_template=PLAN_STEPS_TEMPLATE)
        # Recover for production
        plan = st.session_state.google_gemini.generate_content(
            f"""
                {SYSTEM_PROMPT}

                Given the available information above. Now, a user sends request: {query}
                Please provide a plan of steps to address the user question in the streamlit interface.

                We will later convert these steps into code. Emit the steps in the following dict format:
                {PLAN_STEPS_TEMPLATE}
            """,
            generation_config=genai.types.GenerationConfig(temperature=0.01)
        )

        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(plan.text))
        
        plan_dict = eval(plan.text.replace("`", ""))  # TODO add a post-processing step to ensure the string is cleaned            
        step_code = st.session_state.google_gemini.generate_content(
            f"""
                {SYSTEM_PROMPT}

                Given the available information above. Now, a user sends request: {query}
                We want to address the user question in a streamlit interface.
                A plan has been generated:
                {str(plan_dict)}
                
                Please provide the code to address the user question in the streamlit interface.
                Strictly follow the plan layout. Directly emit executable python code.
            """,
            generation_config=genai.types.GenerationConfig(temperature=0.01)
        )
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(step_code.text))
        
        pattern = r"```python(.*?)```"
        match = re.search(pattern, step_code.text, re.DOTALL)

        try:
            exec(match.group(1))
        except Exception as e:
            st.write(f"Error: {e}")
            prompt = f"""
                    {SYSTEM_PROMPT}

                    Given the available information above. Now, a user sends request: {query}
                    We want to address the user question in a streamlit interface.
                    A plan has been generated:
                    {str(plan_dict)}
                    
                    The following generated code snippet failed to execute to address the user question in the streamlit interface
                    {step_code.text}
                    Error: {e}

                    Please provide a new code snippet that fix it. Directly emit executable python code.
                """
            client = OpenAI(api_key=OPENAI_API_KEY)
            retry_response = client.chat.completions.create(
                model="gpt-4-turbo-2024-04-09",
                messages=[{"role": "user", "content": prompt}],
            )
            retry_code = retry_response.choices[0].message.content
            with st.chat_message("agent", avatar="🤖"):
                st.write_stream(stream_data(retry_code))
                
            pattern = r"```python(.*?)```"
            retry_match = re.search(pattern, retry_code, re.DOTALL)
            exec(retry_match.group(1))