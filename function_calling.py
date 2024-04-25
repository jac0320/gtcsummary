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
    response = chat_completion_request(messages, tools=tools)
    full_message = response.choices[0]
    st.session_state.chat_messages.append({"role": "user", "content": query})
    if full_message.finish_reason == "tool_calls":
        st.info(f"Function generation requested, calling function {full_message.message.tool_calls[0].function.name} with arguments={full_message.message.tool_calls[0].function.arguments}")
        if full_message.message.tool_calls[0].function.name == "keynote_rag":
            query = json.loads(full_message.message.tool_calls[0].function.arguments)["query"]
            return keynote_rag(query)
        elif full_message.message.tool_calls[0].function.name == "personal_note_rag":
            query = json.loads(full_message.message.tool_calls[0].function.arguments)["query"]
            return personal_note_rag(query)
    else:
        st.info(f"Function not required, responding to user")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.content})
        return response