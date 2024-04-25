import streamlit as st
import json

from constants import OPENAI_API_KEY

from rag import keynote_rag, personal_note_rag
from tenacity import retry, wait_random_exponential, stop_after_attempt

GPT_MODEL = "gpt-3.5-turbo-0613"

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    try:
        response = st.session_state.openai_client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e


def chat_completion_with_function_execution(messages, tools=[None], query=None):
    """This function makes a ChatCompletion API call with the option of adding functions"""
    st.session_state.chat_messages.append({"role": "user", "content": query})
    response = chat_completion_request(messages, tools=tools)
    full_message = response.choices[0]
    
    if full_message.finish_reason == "tool_calls":

        function_name = full_message.message.tool_calls[0].function.name
        args = full_message.message.tool_calls[0].function.arguments

        st.info(f"Function generation requested, calling function {function_name} with arguments={args}")
        if function_name == "keynote_rag":
            query = json.loads(full_message.message.tool_calls[0].function.arguments)["query"]
            return keynote_rag(query)
        elif function_name == "personal_note_rag":
            query = json.loads(full_message.message.tool_calls[0].function.arguments)["query"]
            return personal_note_rag(query)
        
    else:
        # Do a regular response here with System Prompt
        st.info(f"Function not required, responding to user")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response