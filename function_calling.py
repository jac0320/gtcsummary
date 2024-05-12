import streamlit as st
import json

from rag import keynote_rag, personal_note_rag
from companies import company_rerank, company_info_search
from talks import talk_info_search, talk_rerank
from tenacity import retry, wait_random_exponential, stop_after_attempt
from view_agent import alpha_view_agent


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

    if "DEBUG_AGENT" in query:
        debug_message = f"DEBUG: Function name=alpha_view_agent"
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(debug_message)
        st.session_state.chat_messages.append({"role": "assistant", "content": debug_message})
        return alpha_view_agent(query)
    
    if full_message.finish_reason == "tool_calls" or "DEBUG" in query:

        function_name = full_message.message.tool_calls[0].function.name
        args = full_message.message.tool_calls[0].function.arguments
        args = json.loads(full_message.message.tool_calls[0].function.arguments)
        
        st.info(f"Function generation requested, calling function {function_name} with arguments={args}")

        if function_name == "alpha_view_agent" or "AGENTDEBUG" in query:
            query = args.get("query")
            return alpha_view_agent(query)
        elif function_name == "keynote_rag":
            query = args.get("query")
            return keynote_rag(query)
        elif function_name == "personal_note_rag":
            query = args.get("query")
            return personal_note_rag(query)
        elif function_name == "company_rerank":
            query = args.get("query")
            k = args.get("k", 5)
            return company_rerank(query, k)
        elif function_name == "talk_rerank":
            query = args.get("query")
            k = args.get("k", 5)
            return talk_rerank(query, k)
        elif function_name == "company_info_search":
            query = args.get("query")
            return company_info_search(query)
        elif function_name == "talk_info_search":
            query = args.get("search_title")
            return talk_info_search(query)
        
    else:
        # Do a regular response here with System Prompt
        st.info(f"Function not required, responding to user")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response