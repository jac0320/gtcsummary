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

from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.ollama import Ollama


def initialize_rag_chat_engine(doc_dir, persist_dir, prefix="", prompt=""):
    if f'{prefix}_chat_engine' in st.session_state:
        return
    
    if not os.path.exists(persist_dir):
        documents = SimpleDirectoryReader(doc_dir, recursive=True).load_data()
        if st.session_state.llm_name == "OpenAI":
            service_context = ServiceContext.from_defaults(llm=st.session_state.llm)
            index = VectorStoreIndex.from_documents(documents, service_context=service_context, similarity_top_k=10)    
        else:
            index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context, similarity_top_k=1)
    
    if st.session_state.llm_name != "OpenAI":
        Settings.embed_model = st.session_state.embeddings
        Settings.llm = Ollama(model="mistral", request_timeout=30.0)
    
    if f'{prefix}_chat_engine' not in st.session_state or st.session_state[f'{prefix}_chat_engine'] is None:
        # Increase token limit and add error handling
        memory = ChatMemoryBuffer.from_defaults(token_limit=8000)  # Increased from 3900
        try:
            st.session_state[f'{prefix}_chat_engine'] = index.as_chat_engine(
                memory=memory,
                system_prompt=(
                    prompt + f"\n Here is the general context {SYSTEM_PROMPT}"
                    "Here are the relevant documents for the context:\n"
                    "{context_str}"
                    "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
                ),
                chat_mode="condense_plus_context",
                verbose=False
            )
        except ValueError as e:
            if "Initial token count exceeds token limit" in str(e):
                # If still too large, try with a smaller context window
                memory = ChatMemoryBuffer.from_defaults(token_limit=4000)
                st.session_state[f'{prefix}_chat_engine'] = index.as_chat_engine(
                    memory=memory,
                    system_prompt=(
                        prompt + f"\n Here is the general context {SYSTEM_PROMPT}"
                        "Here are the relevant documents for the context:\n"
                        "{context_str}"
                        "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
                    ),
                    chat_mode="condense_plus_context",
                    verbose=False
                )
            else:
                raise e


def personal_note_rag(query):
    prefix = "personal_notes"
    st.session_state.logger.info(f"USER {st.session_state.session_id} : PERSONAL NOTE : {query}")
    try:
        response = st.session_state[f'{prefix}_chat_engine'].chat(query)
        st.session_state.logger.info(f"BOT {st.session_state.session_id} : PERSONAL NOTE : {response.response}")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
    except ValueError as e:
        if "Initial token count exceeds token limit" in str(e):
            st.error("The conversation history is too long. Starting a new conversation.")
            st.session_state[f'{prefix}_chat_engine'] = None
            initialize_rag_chat_engine("personal_notes", "personal_notes_index", prefix="personal_notes")
            response = st.session_state[f'{prefix}_chat_engine'].chat(query)
            st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
        else:
            raise e


def keynote_rag(query):
    prefix = "keynote"
    st.session_state.logger.info(f"USER {st.session_state.session_id} : KEYNOTE : {query}")
    try:
        response = st.session_state[f'{prefix}_chat_engine'].chat(query)
        st.session_state.logger.info(f"BOT {st.session_state.session_id} : KEYNOTE : {response.response}")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
        st.rerun()
    except ValueError as e:
        if "Initial token count exceeds token limit" in str(e):
            st.error("The conversation history is too long. Starting a new conversation.")
            st.session_state[f'{prefix}_chat_engine'] = None
            initialize_rag_chat_engine("keynote", "keynote_index", prefix="keynote")
            response = st.session_state[f'{prefix}_chat_engine'].chat(query)
            st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
            st.rerun()
        else:
            raise e


def transcribed_notes_rag(query):
    prefix = "transcribed_notes"
    st.session_state.logger.info(f"USER {st.session_state.session_id} : TRANSCRIBED TALKS : {query}")
    try:
        response = st.session_state[f'{prefix}_chat_engine'].chat(query)
        st.session_state.logger.info(f"BOT {st.session_state.session_id} : TRANSCRIBED TALKS : {response.response}")
        st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
    except ValueError as e:
        if "Initial token count exceeds token limit" in str(e):
            st.error("The conversation history is too long. Starting a new conversation.")
            st.session_state[f'{prefix}_chat_engine'] = None
            initialize_rag_chat_engine("transcribed_notes", "transcribed_notes_index", prefix="transcribed_notes")
            response = st.session_state[f'{prefix}_chat_engine'].chat(query)
            st.session_state.chat_messages.append({"role": "assistant", "content": response.response})
        else:
            raise e
