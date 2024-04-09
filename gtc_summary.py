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


def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)


def keynote_qa():

    def reset_keynote_messages():
        st.session_state.keynote_messages = [
            {"role": "agent", "content": "Hello! I may know a bit about Jensen Huang's 2024 GTC Keynote. Ask me anything."},
        ]
        st.session_state.chat_engine = None

    if 'keynote_messages' not in st.session_state:
        reset_keynote_messages()

    # check if storage already exists
    if not os.path.exists(KEYNOTE_PERSIST_DIR):
        # load the documents and create the index
        documents = SimpleDirectoryReader("keynote").load_data()
        # index = VectorStoreIndex.from_documents(documents)
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(
                model="gpt-3.5-turbo", 
                temperature=0.5, 
                system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."
                )
            )
        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        index.storage_context.persist(persist_dir=KEYNOTE_PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=KEYNOTE_PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # embedding model
    # Settings.embed_model = st.session_state.embeddings

    # ollama
    # Settings.llm = Ollama(model="mistral", request_timeout=30.0)

    if 'chat_engine' not in st.session_state or st.session_state.chat_engine is None:
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question")

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

    # check if storage already exists
    if not os.path.exists(NOTES_PERSIST_DIR):
        # load the documents and create the index
        documents = SimpleDirectoryReader("keynote").load_data()
        # index = VectorStoreIndex.from_documents(documents)
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(
                model="gpt-3.5-turbo", 
                temperature=0.5, 
                system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."
                )
            )
        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        index.storage_context.persist(persist_dir=KEYNOTE_PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=NOTES_PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

    # embedding model
    # Settings.embed_model = st.session_state.embeddings

    # ollama
    # Settings.llm = Ollama(model="mistral", request_timeout=30.0)

    if 'ama_chat_engine' not in st.session_state or st.session_state.ama_chat_engine is None:
        st.session_state.ama_chat_engine = index.as_chat_engine(chat_mode="condense_question")

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


def main():

    st.title("GTC 2024 | A Summary")

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies = st.tabs(
        ["👋 Welcome!", "🏆 The Keynote", "📕 Ask My Notes", "🎙️ Technical Talks", "🏢 Companies", ]
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
        ama_qa()

    with tab_talks:
        st.info("Search for Collected Technical Talks and Read/Downlaod PDFs")
        talk_show()
        # Try to see if there is a way to summarize the technical keynotes - with abstract information also extracted

    with tab_companies:
        st.subheader("The Companies")
        company_show()
        # https://www.nvidia.com/gtc/sponsors/#/



main()