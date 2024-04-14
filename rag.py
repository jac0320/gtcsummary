import streamlit as st
import os

from constants import *
from utils import stream_data
from templates import SYSTEM_PROMPT

from llama_index.core import (
    ServiceContext,
    VectorStoreIndex,
    SimpleDirectoryReader, 
    StorageContext,
    load_index_from_storage,
    Settings
)

from llama_index.llms.ollama import Ollama


def qa_chat_engine(doc_dir, persist_dir):
    
    if not os.path.exists(persist_dir):
        documents = SimpleDirectoryReader(doc_dir, recursive=True).load_data()  # load the documents and create the index
        if st.session_state.llm_name == "OpenAI":
            service_context = ServiceContext.from_defaults(llm=st.session_state.llm)
            index = VectorStoreIndex.from_documents(documents, service_context=service_context, similarity_top_k=10)    
        else:
            index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context, similarity_top_k=10)

    if st.session_state.llm_name != "OpenAI":  # additional steps for ollama - which I think I can remove
        Settings.embed_model = st.session_state.embeddings
        Settings.llm = Ollama(model="mistral", request_timeout=30.0)

    if 'chat_engine' not in st.session_state or st.session_state.chat_engine is None:
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question")

    
def keynote_qa():

    def reset_keynote_messages():
        st.session_state.keynote_messages = [
            {'role': "system", "content": SYSTEM_PROMPT},
            {"role": "agent", "content": "Hello! I may know a bit about Jensen Huang's 2024 GTC Keynote. Ask me anything."},
        ]
        st.session_state.chat_engine = None

    if 'keynote_messages' not in st.session_state:
        reset_keynote_messages()
    
    qa_chat_engine("keynote", KEYNOTE_PERSIST_DIR)

    for message in st.session_state.keynote_messages: # Display the prior chat messages
        if message["role"] == "system":
            continue
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