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
from view_agent import alpha_view_agent

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="GTC 2024", 
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

    st.title("GTC 2024 : Learning Notes 🤖📚")
    
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
            model="gpt-3.5-turbo", 
            temperature=0.5, 
            system_prompt=SYSTEM_PROMPT
        )
    else:
        st.session_state.llm = Ollama(
            model="mistral", 
            request_timeout=30.0
        )

    initialize_rag_chat_engine(
        "keynote", 
        KEYNOTE_PERSIST_DIR, 
        prefix="keynote", 
        prompt="You are a chatbot, able to have normal interactions, as well as talk about Jensen Huang's Keynote at GTC 2024. You can also provide information."
    )

    initialize_rag_chat_engine(
        "personal_notes", 
        PERSONAL_NOTE_PERSIST_DIR,
        prefix="personal_notes",
        prompt="You are a chatbot, able to have normal interactions, as well as talk about personal notes writte by Site. You can also provide information."
    )

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies = st.tabs(
        [
            "👋 Welcome!", 
            "🏆 Jensen's Keynote", 
            "📕 My Notes", 
            "🎙️ Talks", 
            "🏢 Companies", 
        ]
    )

    with tab_intro:
        intro()

    with tab_keynote:
        st.video(data='https://www.youtube.com/watch?v=Y2F8yisiS6E')
        keynote_perplexity_summary()
        keynote_openai_summary()

    with tab_ama:
        notes_summary()
        notes_pictures()

    with tab_talks:
        st.info("Select a transcribed talk to view summaried notes")
        show_summarized_notes()
        st.write('---')
        st.info("Search for Collected Technical Talks and Read/Downlaod PDFs")
        talk_show()

    with tab_companies:
        company_tab()

    tools = [
        {
            "type": "function",
            "function": {
                "name": "keynote_rag",
                "description": "Answer question about Jensen Huang's Keynote presentation at GTC 2024. The questions/query only applies to the keynote information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about with Jensen Huang's Keynote Presentation",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "personal_note_rag",
                "description": "Answer question about personal notes written by Site Wang based on his experience at GTC 2024. These notes are all written by Site Wang himself with fresh opinion about several new AI topics about the conferece.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about personal notes written by Site Wang",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "company_rerank",
                "description": "Rank sponsor companies at GTC 2024 based on the user query relevance to the company description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about general description of a company",
                        },
                        "k": {
                            "type": "integer",
                            "description": "how many top results to be returned",
                            "default": 5
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "company_info_search",
                "description": "Answer question about a specific sponsor company at GTC 2024. It is only used when a sepcific company name is mentioned/asked by the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about a specific sponsor company at GTC 2024",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "talk_info_search",
                "description": "Conduct a searched to fetch the url about a specific talk based on the user query. It is only applicable when user is asking about a specific talk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Title string about a specific technical talk at GTC 2024",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "talk_rerank",
                "description": "Rank technical talks at GTC 2024 based on the user query relevance to talks' title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about a general direction of research topics to be used for searching for relevant technical talks at GTC 2024",
                        },
                        "k": {
                            "type": "integer",
                            "description": "how many top results to be returned",
                            "default": 5
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "alpha_view_agent",
                "description": "This function is used to generate code to fulfill a users request. The requests is not a typically information retrieval request but a more complex tasks that requires code generation. The function will generate a plan of steps to address the user question by coding in the streamlit interface.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "User requests for a code generation task",
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]
    
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
            tools=tools,
            query=query
        )
        st.write(response)
        st.rerun()
        
main()