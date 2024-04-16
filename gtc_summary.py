import logging
import os
import sys
import pandas as pd
import numpy as np
import streamlit as st

from streamlit_pdf_viewer import pdf_viewer
from llama_index.llms.openai import OpenAI as llamaindex_OpenAI
from openai import OpenAI
import google.generativeai as genai

from writings import *
from templates import *
from utils import *
from constants import OPENAI_API_KEY

from rag import keynote_qa
from view_agent import alpha_viewagent

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.ollama import Ollama

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


st.set_page_config(
    page_title="GTC 2024", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)


def talk_show():

    user_search = st.text_input("Describe what you want to learn for a talk", key='talk_search', value=None)
    
    if user_search is not None:
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
        selected_file = df.loc[df['Title'] == selected_title].index[0]
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
        user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/company_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['description'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    st.write("Companies ranked based on your search || Extracted by AI from https://www.nvidia.com/gtc/sponsors/#/ ")
    if user_search is not None:    
        embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
        df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
        st.dataframe(df.sort_values('distance')[['name', 'description']], use_container_width=True, hide_index=True)
    else:
        st.dataframe(df[['name', 'description']], use_container_width=True, hide_index=True)
    
    st.write("---")
    if query := st.chat_input("Tell me more about Unstructured ai company?", key='company_chat'):
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        answer = st.session_state.gemini_client.generate_content(query)
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
        with open(str(selected_md_file), "r") as file:
            st.markdown(file.read())


def clean_agent_session():
    st.session_state.agent_session = {"query": {}, "plan": {}, "response": {}}


def main():

    st.title("GTC 2024 : Learning Notes 🤖📚")

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = OpenAIEmbedding()
    
    if 'gemini_client' not in st.session_state:
        genai.configure(api_key=os.environ["API_KEY"])
        st.session_state.gemini_client = genai.GenerativeModel('gemini-pro')

    if 'openai_client' not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    if 'agent_session' not in st.session_state:
        clean_agent_session()
    
    st.sidebar.button(
        "Clean Agent Session", 
        on_click=clean_agent_session,
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
        st.write('---')
        keynote_qa()

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
        

main()