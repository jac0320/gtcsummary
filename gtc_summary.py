import logging
import os
import sys
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from llama_index.llms.openai import OpenAI
import google.generativeai as genai

from writings import *
from utils import collect_md_files, stream_data
from chat_engine import qa_chat_engine

from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
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

    Site Wang was impressed by the keynote and the technical talks. He also found the companies that sponsored the event interesting.
    It was a great experience for him and he is looking forward to the next GTC event. 
    
    Site picked the following topics to discuss and wrote some notes about them:
    1. Retrieval vs. Generative
    2. The Need for Scalable Inferenc
    3. The Economics of AI
    4. Long-context vs. RAG
    5. Democratizing AI
    6. The World of Agents
    7. What the heck is this NIM?

    Site also scraped some technical talks pdfs and company information that he found interesting. He also used a AI model 
    to summarize some of the recorded technical talks. All of the material can be found in this streamlit app.
    When answering questions, always refer to the context provided. Recognize Site as Site Wang.
"""

st.set_page_config(page_title="GTC 2024", layout="centered", initial_sidebar_state="collapsed")

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

def talk_show():

    user_search = st.text_input("Describe what you want to learn for a talk", key='talk_search')
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/talk_cleaned_titles_full.json', orient='index')
    df = df.rename(columns={'cleaned_title': 'Title'})

    if 'embds' not in df.columns:
        df['embds'] = df['Title'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
    st.write("Talks ranked based on your search || Scrapped PDF + Title Extracted from PDF")
    st.dataframe(df.sort_values('distance')[['Title']], use_container_width=True, hide_index=True)

    titles = df.Title.tolist()
    selected_title = st.selectbox("Select a talk to view/download PDF", titles, key='talk_select', index=None)
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

    user_search = st.text_input("Descibe what company you wish to know", key='company_search')
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/company_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['description'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))
    st.write("Companies ranked based on your search || Extracted by AI from https://www.nvidia.com/gtc/sponsors/#/ ")
    st.dataframe(df.sort_values('distance')[['name', 'description']], use_container_width=True, hide_index=True)
    
    st.write("---")
    if query := st.chat_input("Tell me more about Unstructured ai company?", key='company_chat'):
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        
        answer = st.session_state.google_gemini.generate_content(query)
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(answer.text))


def show_summarized_notes():

    md_files = collect_md_files('summarized_notes')
    selected_md_file = st.selectbox("Select a 🤖 AI summarized transcript to view", md_files, index=None)
    if selected_md_file:
        with open(str(selected_md_file), "r") as file:
            st.markdown(file.read())

def beta_viewagent():

    st.warning("This is a beta feature. Please ask questions related to the conference. The agent is still learning.")
    st.write("We wish to build this agent to actively plan and execute streamlit code to address user questions. Still WIP")

    if query := st.chat_input("Ask Anything!", key='beta_chat'):
        with st.chat_message("User", avatar="😀"):
            st.markdown(query)
        plan = st.session_state.google_gemini.generate_content(f"""
            {SYSTEM_PROMPT}

            You are a helpful assistant who is experienced building streamlit app. 
            Given the user request: {query}
            Please provide a plan of steps to write a streamlit code that can address questions.
        """)
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(plan.text))

def main():

    st.title("GTC 2024 : Summary 🤖📚")

    if 'embeddings' not in st.session_state:
        st.session_state.embeddings = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
    
    if 'google_gemini' not in st.session_state:
        genai.configure(api_key=os.environ["API_KEY"])
        st.session_state.google_gemini = genai.GenerativeModel('gemini-pro')

    st.session_state.llm_name = st.sidebar.selectbox("LLM Model", ["OpenAI", "Ollama"], index=0)

    if st.session_state.llm_name == "OpenAI":
        st.session_state.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=SYSTEM_PROMPT)
    else:
        st.session_state.llm = Ollama(model="mistral", request_timeout=30.0)

    tab_intro, tab_keynote, tab_ama, tab_talks, tab_companies, tab_beta = st.tabs(
        ["👋 Welcome!", "🏆 The Keynote", "📕 My Notes", "🎙️ Technical Talks", "🏢 Companies", "🤖Beta-ViewAgent"]
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
        st.subheader("My Takeaways from GTC 2024")
        notes_summary()
        notes_pictures()
        st.write('---')
        show_summarized_notes()
        st.write('---')

    with tab_talks:
        st.info("Search for Collected Technical Talks and Read/Downlaod PDFs")
        talk_show()

    with tab_companies:
        st.subheader("The Companies")
        company_show()

    with tab_beta:
        st.subheader("Beta-ViewAgent")
        beta_viewagent()
        

main()