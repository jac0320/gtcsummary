import logging
import os
import sys
import uuid
import pandas as pd
import numpy as np
import streamlit as st

from llama_index.llms.openai import OpenAI as llamaindex_OpenAI
from openai import OpenAI
import google.generativeai as genai

from rag import initialize_rag_chat_engine
from writings import *
from templates import *
from utils import *
from constants import *
from function_calling import chat_completion_with_function_execution
from constants import OPENAI_API_KEY

from companies import company_tab
from talks import talk_show, show_summarized_notes
from tools import TOOLS
from view_agent import alpha_view_agent

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="GTC 2025", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)


def reset_chat_messages():
    st.session_state.chat_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello! Ask anything. I will try to leverage all the tools the answer."},
    ]
    st.session_state.exec_code = {}


def main():

    st.title("GTC 2025 : Learning Notes 🤖📚")
    
    if 'session_id' not in st.session_state:
        session_id = uuid.uuid4().hex
        st.session_state['session_id'] = session_id
        st.session_state.logger = logging.getLogger(session_id)
        st.session_state.logger.setLevel(logging.INFO)

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = OpenAIEmbedding()

    if 'gemini_client' not in st.session_state:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        st.session_state.gemini_client = genai.GenerativeModel('gemini-pro')

    if 'openai_client' not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    if 'chat_messages' not in st.session_state:
        reset_chat_messages()
    
    st.sidebar.button(
        "🧹 Clear Chat Session", 
        on_click=reset_chat_messages, 
        use_container_width=True
    )

    st.session_state.code_planer = st.sidebar.selectbox(
        "Code Planer",
        ["OpenAI", "Gemini"],
        key="code_planer_select",
        index=0
    )
    
    st.session_state.code_generation_retry = st.sidebar.slider(
        "Code Generation Retry", 
        min_value=0, 
        max_value=3, 
        value=2, 
        key="code_genneration_retry_limit"
    )

    st.session_state.llm_name = st.sidebar.selectbox(
        "RAG LLM Model", 
        ["OpenAI", "Ollama"], 
        key="llm_select", 
        index=0
    )

    if st.session_state.llm_name == "OpenAI":
        st.session_state.llm = llamaindex_OpenAI(
            model="gpt-4", 
            temperature=0.5, 
            system_prompt=SYSTEM_PROMPT
        )
    else:
        st.session_state.llm = Ollama(
            model="mistral", 
            request_timeout=30.0
        )

    with st.spinner("Setting up RAG"):
        initialize_rag_chat_engine(
            "keynote", 
            KEYNOTE_PERSIST_DIR, 
            prefix="keynote", 
            prompt="You are a chatbot, able to have normal interactions, as well as talk about Jensen Huang's Keynote at GTC 2025 and 2024. You can also provide information."
        )

        initialize_rag_chat_engine(
            "personal_notes", 
            PERSONAL_NOTE_PERSIST_DIR,
            prefix="personal_notes",
            prompt="You are a chatbot, able to have normal interactions, as well as talk about personal notes writte by Site. You can also provide information."
        )

        initialize_rag_chat_engine(
            "transcribed_notes", 
            NOTES_PERSIST_DIR,
            prefix="transcribed_notes",
            prompt="You are a chatbot, able to have normal interactions, as well as talk about personal notes writte by Site. You can also provide information."
        )

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies = st.tabs(
        [
            "👋 Welcome!", 
            "🏆 Jensen's Keynote", 
            "📕 My Blogs", 
            "🎙️ Talks", 
            "🏢 Companies", 
        ]
    )

    with tab_intro:
        intro()

    with tab_keynote:

        st.subheader("GTC 2025")
        st.video(data="https://www.youtube.com/watch?v=_waPvOwL9Z8")
        keynote_2025_openai_summary()

        st.write('---')
        st.subheader("GTC 2024")
        st.video(data="https://www.youtube.com/watch?v=Y2F8yisiS6E")
        keynote_2024_openai_summary()

    with tab_ama:
        notes_summary()
        notes_pictures()

    with tab_talks:
        show_summarized_notes()
        st.write('---')
        talk_show()

    with tab_companies:
        company_tab()
    
    st.write('---')

    for message in st.session_state.chat_messages: # Display the prior chat messages
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])
        if message["role"] == "assistant" and "Code execution successful." == message["content"]:
            code_key = message.get("source")
            exec(st.session_state.exec_code[code_key], globals())
    
    if 'user' in [i['role'] for i in st.session_state.chat_messages]:
        st.button(
            "🧹 Clear Chat Session", 
            on_click=reset_chat_messages, 
            key="clear_chat_button",
            use_container_width=True
        )
    
    if query := st.chat_input("Ask a question", key="main_chat"):
    
        response = chat_completion_with_function_execution(
            st.session_state.chat_messages, 
            tools=TOOLS,
            query=query
        )
        st.write(response)
        st.rerun()
        
main()