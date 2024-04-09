import logging
import os
import sys
import time
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from llama_index.llms.openai import OpenAI
from perplexity import Perplexity

from static import *

from llama_index.core import (
    ServiceContext,
    VectorStoreIndex,
    SimpleDirectoryReader, 
    StorageContext,
    load_index_from_storage,
    Settings
)

from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

KEYNOTE_PERSIST_DIR = ".keynote_storage"
NOTES_PERSIST_DIR = ".notes_storage"
NOTES_DAT_DIR = "summarized_notes"


SYSTEM_PROMPT = """
    You are an helper to assis Site Wang who just attended GTC 2024 to answer questions related to the conference. 
    Assume that all questions are based on Site's experience which will be provided as context. 
    Keep your answers relatable and friendly and based on facts provided in the context – do not hallucinate.
    Be patient with technical terms and always assume your audience is not familiar with the technical jargon.
"""


def collect_md_files(folder_path):
    """
    Recursively collects all .md files from a specified folder.

    Parameters:
    - folder_path (str): The path to the folder from which to collect .md files.

    Returns:
    - list[str]: A list of full paths to the .md files found within the folder and its subfolders.
    """
    md_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)

    return md_files


def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)


def qa_chat_engine(doc_dir, persist_dir):
    
    if not os.path.exists(persist_dir):
        documents = SimpleDirectoryReader(doc_dir).load_data()  # load the documents and create the index
        if st.session_state.llm_name == "OpenAI":
            service_context = ServiceContext.from_defaults(llm=st.session_state.llm)
            index = VectorStoreIndex.from_documents(documents, service_context=service_context, similarity_top_k=5)    
        else:
            index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context, similarity_top_k=5)

    if st.session_state.llm_name != "OpenAI":  # additional steps for ollama - which I think I can remove
        Settings.embed_model = st.session_state.embeddings
        Settings.llm = Ollama(model="mistral", request_timeout=30.0)

    if 'chat_engine' not in st.session_state or st.session_state.chat_engine is None:
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question")

def keynote_qa():

    def reset_keynote_messages():
        st.session_state.keynote_messages = [
            {"role": "agent", "content": "Hello! I may know a bit about Jensen Huang's 2024 GTC Keynote. Ask me anything."},
        ]
        st.session_state.chat_engine = None

    if 'keynote_messages' not in st.session_state:
        reset_keynote_messages()
    
    qa_chat_engine("keynote", KEYNOTE_PERSIST_DIR)

    for message in st.session_state.keynote_messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if query := st.chat_input("Ask a question"):
        st.session_state.keynote_messages.append({"role": "user", "content": query})
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        response = st.session_state.chat_engine.chat(query)
        st.session_state.keynote_messages.append({"role": "agent", "content": response.response})
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(response.response))
        st.rerun()

    st.button("Start New Chat 🧹", on_click=reset_keynote_messages, use_container_width=True)


def ama_qa():

    def reset_ama_messages():
        st.session_state.ama_messages = [
            {"role": "agent", "content": "Hello! You can ask what else did Site learn from GTC 2024?"},
        ]
        st.session_state.ama_chat_engine = None

    if 'ama_messages' not in st.session_state:
        reset_ama_messages()

    qa_chat_engine("summarized_notes", NOTES_PERSIST_DIR)

    for message in st.session_state.ama_messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if query := st.chat_input("Ask a question", key="ama"):
        st.session_state.ama_messages.append({"role": "user", "content": query})
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        response = st.session_state.ama_chat_engine.chat(query)
        st.session_state.ama_messages.append({"role": "agent", "content": response.response})
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(response.response))
        st.rerun()

    st.button("Start New Chat 🧹", key='ama_clean', on_click=reset_ama_messages, use_container_width=True)


def talk_show():

    user_search = st.text_input("Search for a talk", key='talk_search')
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/talk_cleaned_titles_full.json', orient='index')
    df = df.rename(columns={'cleaned_title': 'Title'})

    if 'embds' not in df.columns:
        df['embds'] = df['Title'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))

    st.dataframe(df.sort_values('distance')[['Title']], use_container_width=True, hide_index=True)

    titles = df.Title.tolist()
    selected_title = st.selectbox("Select a talk to view PDF", titles, key='talk_select', index=None)
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

    user_search = st.text_input("Descibe what you wish to know", key='company_search')
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/company_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['description'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
    st.dataframe(df.sort_values('distance')[['name', 'description']], use_container_width=True, hide_index=True)
    
    st.write("---")
    if query := st.chat_input("Tell me more about Unstructured ai company?", key='company_chat'):
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        perplexity = Perplexity()
        answer = perplexity.search(query)
        answer_str = None
        for ans in answer:
            if isinstance(ans, dict) and 'answer' in ans:
                answer_str = ans['answer']
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(answer_str))


def show_summarized_notes():

    md_files = collect_md_files('summarized_notes')
    selected_md_file = st.selectbox("Select a summarized transcript to view", md_files, index=None)
    if selected_md_file:
        with open(str(selected_md_file), "r") as file:
            st.markdown(file.read())


def main():

    st.title("GTC 2024 | A Summary")

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

    st.session_state.llm_name = st.sidebar.selectbox("LLM Model", ["OpenAI", "Ollama"], index=0)
    
    if st.session_state.llm_name == "OpenAI":
        st.session_state.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=SYSTEM_PROMPT)
    else:
        st.session_state.llm = Ollama(model="mistral", request_timeout=30.0)

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies = st.tabs(
        ["👋 Welcome!", "🏆 The Keynote", "📕 My Notes", "🎙️ Technical Talks", "🏢 Companies", ]
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
        st.subheader("The Summary")
        notes_summary()
        notes_pictures()
        st.write('---')
        show_summarized_notes()
        st.write('---')
        ama_qa()

    with tab_talks:
        st.info("Search for Collected Technical Talks and Read/Downlaod PDFs")
        talk_show()

    with tab_companies:
        st.subheader("The Companies")
        company_show() # https://www.nvidia.com/gtc/sponsors/#/
        



main()