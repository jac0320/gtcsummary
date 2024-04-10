import os

import streamlit as st

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