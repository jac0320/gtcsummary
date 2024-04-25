import logging
import os
import sys
import uuid
import pandas as pd
import numpy as np
import streamlit as st
import json

from streamlit_pdf_viewer import pdf_viewer
from llama_index.llms.openai import OpenAI as llamaindex_OpenAI
from openai import OpenAI
import google.generativeai as genai

from writings import *
from templates import *
from utils import *
from function_calling import chat_completion_with_function_execution
from constants import OPENAI_API_KEY

from rag import ask_keynote_rag
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.ollama import Ollama

from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt

logging.basicConfig(level=logging.INFO)

GPT_MODEL = "gpt-3.5-turbo-0613"

st.set_page_config(
    page_title="GTC 2024", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)


def reset_chat_messages():
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hello! Ask anything. I will try to leverage all the tools the answer."},
    ]




def main():

    st.title("GTC 2024 : Learning Notes 🤖📚")
    
    if 'session_id' not in st.session_state:
        session_id = uuid.uuid4().hex
        st.session_state['session_id'] = session_id
        st.session_state.logger = logging.getLogger(session_id)
        st.session_state.logger.setLevel(logging.INFO)

    if 'openai_client' not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    if 'chat_messages' not in st.session_state:
        reset_chat_messages()
        
    st.session_state.code_generation_retry = st.sidebar.slider(
        "Code Generation Retry", 
        min_value=0, 
        max_value=3, 
        value=1, 
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
            model="gpt-3.5-turbo", 
            temperature=0.5, 
            system_prompt=SYSTEM_PROMPT
        )
    else:
        st.session_state.llm = Ollama(
            model="mistral", 
            request_timeout=30.0
        )

    for message in st.session_state.chat_messages: # Display the prior chat messages
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])
    


main()