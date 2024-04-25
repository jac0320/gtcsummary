import logging
import os
import sys
import uuid
import pandas as pd
import numpy as np
import streamlit as st

from streamlit_pdf_viewer import pdf_viewer
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

from rag import keynote_rag
from view_agent import alpha_viewagent

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="GTC 2024", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)



def talk_show():

    user_search = st.text_input("Describe what you want to learn for a talk", key='talk_search', value=None)
    
    if user_search is not None:
        st.session_state.logger.info(f"USER {st.session_state.session_id} : TALK_SEARCH : {user_search}")
        user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/pdf_full.json')

    if 'embds' not in df.columns:
        df['embds'] = df['Title'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    st.write("Talks ranked based on your search || Scrapped PDF + Title Extracted from PDF")
    if user_search is not None:
        embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
        df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
        st.dataframe(df.sort_values('distance')[['Title']], use_container_width=True, hide_index=True)
    else:
        st.dataframe(df[['Title']], use_container_width=True, hide_index=True)

    titles = df.Title.tolist()
    selected_title = st.selectbox(
        "Select a talk to view/download PDF", 
        titles, 
        key='talk_select', 
        index=None
    )

    if selected_title:
        st.session_state.logger.info(f"USER {st.session_state.session_id} : TALK_PDF : {selected_title}")
        selected_file = df.loc[df['Title'] == selected_title].filename.head(1).squeeze()
        filapath = f"talks/{selected_file}"
        with open(filapath, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name=filapath,
                use_container_width=True,
            )
        pdf_viewer(filapath)


def company_show():

    user_search = st.text_input("Descibe what company you wish to know", key='company_search', value=None)
    if user_search is not None:
        st.session_state.logger.info(f"USER {st.session_state.session_id} : COMPANY_SEARCH : {user_search}")
        user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/company_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['description'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    st.write("Companies ranked based on your search || Extracted using AI from https://www.nvidia.com/gtc/sponsors/#/ ")
    if user_search is not None:    
        embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
        df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
        st.dataframe(df.sort_values('distance')[['name', 'description']], use_container_width=True, hide_index=True)
    else:
        st.dataframe(df[['name', 'description']], use_container_width=True, hide_index=True)
    
    st.write("---")
    if query := st.chat_input("Tell me more about Unstructured ai company?", key='company_chat'):
        st.session_state.logger.info(f"USER {st.session_state.session_id} : COMPANY : {query}")
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        answer = st.session_state.gemini_client.generate_content(query)
        st.session_state.logger.info(f"BOT {st.session_state.session_id} : COMPANY : {answer.text}")
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(answer.text))


def show_summarized_notes():

    md_files = collect_md_files('transcribed_notes')
    selected_md_file = st.selectbox(
        "Select a 🤖 AI summarized transcript to view",
        md_files, 
        key="summarized_note_select", 
        index=None
    )
    if selected_md_file:
        st.session_state.logger.info(f"USER {st.session_state.session_id} : NOTE : {selected_md_file}")
        with open(str(selected_md_file), "r") as file:
            st.markdown(file.read())


def clean_agent_session():
    st.session_state.agent_session = {"query": {}, "plan": {}, "response": {}}


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

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = OpenAIEmbedding()

    if 'gemini_client' not in st.session_state:
        genai.configure(api_key=os.environ["API_KEY"])
        st.session_state.gemini_client = genai.GenerativeModel('gemini-pro')

    if 'openai_client' not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    if 'chat_messages' not in st.session_state:
        reset_chat_messages()
    
    if 'agent_session' not in st.session_state:
        clean_agent_session()

    st.sidebar.button(
        "Clean Agent Session", 
        on_click=clean_agent_session,
        use_container_width=True
    )

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

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies, tab_beta = st.tabs(
        [
            "👋 Welcome!", 
            "🏆 The Keynote", 
            "📕 My Takeaways", 
            "🎙️ Technical Talks", 
            "🏢 Companies", 
            "🤖 ALPHA-ViewAgent"
        ]
    )

    with tab_intro:
        intro()

    with tab_keynote:
        st.subheader("The Keynote by Jensen Huang")
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
        st.subheader("The Companies")
        company_show()

    with tab_beta:
        st.subheader("Beta-ViewAgent")
        try:
            alpha_viewagent()
        except Exception as e:
            st.error(f"Error: {e}")

    tools = [
        {
            "type": "function",
            "function": {
                "name": "keynote_rag",
                "description": "Ask a question about more information Jensen Huang's Keynote presentation at GTC 2024. The questions/query only applies to the keynote information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question for the RAG model that connets with Site's notes",
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
                "description": "Ask about what notes Site Wang wrote based on his experience at GTC 2024. These notes are all written by Site Wang himself with fresh opinion about several new AI topics about the conferece.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question for the RAG model that connets with Site's notes",
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]
    
    st.write('---')
    for message in st.session_state.chat_messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if query := st.chat_input("Ask a question", key="main_chat"):
    
        response = chat_completion_with_function_execution(
            st.session_state.chat_messages, 
            tools=tools,
            query=query
        )
        st.write(response)
        st.rerun()
        
main()