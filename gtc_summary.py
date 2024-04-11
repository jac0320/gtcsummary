import logging
import os
import sys
import re
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

PLAN_STEPS_TEMPLATE ="""
\{
    "steps": \{
        "1": "Step 1",
        "2": "Step 2",
        ...
    \}
\}
"""

SYSTEM_PROMPT = """
    You are an helper to assist Site Wang who just attended GTC 2024. Your job is to answer questions related to the conference and answer
    them on Site's behalf. Answer questions are based on Site's experience which will be provided as context. 
    Keep your answers relatable and friendly and based on facts provided in the context – do not hallucinate.
    Be patient with technical terms and always assume your audience is not familiar with the technical jargon.

    Site Wang was impressed by the keynote and the technical talks. He also found the companies that sponsored the event interesting.
    It was a great experience for him and he is looking forward to the next GTC event. 

    Site watched the entire keynote presentation delivered by Jensen Huang. He recorded the audio and used an AI model to transcript 
    and summarize it. Those note can be found under the strealit tab "The Keynote". He also built an AI agent to answer questions using
    a basic Retrieval-Augmented Generation(RAG) model. A user can use the chat interface to ask questions about the keynote.
    
    Site wrote his own notes about following topics and those notes can be found under the strealit tab "My Notes". The source of those 
    personal notes are in several markdown format under the folder "./summarized_notes/personal_notes/". The topics are:
    1. Retrieval vs. Generative
    2. The Need for Scalable Inferenc
    3. The Economics of AI
    4. Long-context vs. RAG
    5. Democratizing AI
    6. The World of Agents
    7. What the heck is this NIM?
    Under the "My Notes" tab, a user can also view the summarized notes of the recorded technical talks. Those transcripts were generated
    using an Whisper AI and Otter.ai tools. The notes are stored under "./summarised_notes".

    Site also put together a collection of technical talks that he found interesting. He scraped the titles and pdfs of the talks and
    used an AI agent to scan the first slide of the pdfs to extract the title of the slide. A user can search for a talk and read/download 
    the pdfs under the "Technical Talks" tab. The search is based on OpenAI embeddings. If a user wants to know more about a technical talk,
    he can select to view or download the content. All these pdf files are stored under the "talks" folder. The file name is different from 
    the title of the talk. You can find the mapping between pdf fileanmes to the talk title in the "./notebooks/talk_cleaned_titles_full.json".

    Site also scrapped the companies that sponsored the GTC using an AI agent. All of these companies were at the GTC exhibitor hall. A user 
    can search for a company and read a brief description of the company. If a user wants to know more about a company, he can ask more questions
    about the company. The AI agent will give a brief description of the company with the most recent information. The AI agent is powered
    by the most recent Google Gemini API. The companies data are stored under the "notebooks/company_full.json".
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

        # Recover for production
        plan = st.session_state.google_gemini.generate_content(
            f"""
                {SYSTEM_PROMPT}

                Given the available information above. Now, a user sends request: {query}
                Please provide a plan of steps to address the user question in the streamlit interface.

                We will later convert these steps into code. Emit the steps in the following dict format:
                {PLAN_STEPS_TEMPLATE}
            """,
            generation_config=genai.types.GenerationConfig(temperature=0.01)
        )

        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(plan.text))
        
        plan_dict = eval(plan.text.replace("`", ""))  # TODO add a post-processing step to ensure the string is cleaned

        # plan_dict = {
        #     "steps": {
        #         "1": "Import the necessary libraries.",
        #         "2": "Load the personal notes written by Site.",
        #         "3": "Select a random note from the list of notes.",
        #         "4": "Display the selected note in the streamlit interface as an info section."
        #     }
        # }
        
        # total_steps = len(plan_dict["steps"])
        
            
        step_code = st.session_state.google_gemini.generate_content(
            f"""
                {SYSTEM_PROMPT}

                Given the available information above. Now, a user sends request: {query}
                We want to address the user question in a streamlit interface.
                A plan has been generated:
                {str(plan_dict)}
                
                Please provide the code to address the user question in the streamlit interface.
                Strictly follow the plan layout. Directly emit executable python code.
            """,
            generation_config=genai.types.GenerationConfig(temperature=0.01)
        )
        with st.chat_message("agent", avatar="🤖"):
            st.write_stream(stream_data(step_code.text))
        print(step_code.text)
        pattern = r"```python(.*?)```"
        match = re.search(pattern, step_code.text, re.DOTALL)

        try:
            exec(match.group(1))
        except Exception as e:
            st.write(f"Error: {e}")
            prompt = f"""
                    {SYSTEM_PROMPT}

                    Given the available information above. Now, a user sends request: {query}
                    We want to address the user question in a streamlit interface.
                    A plan has been generated:
                    {str(plan_dict)}
                    
                    The following generated code snippet failed to execute to address the user question in the streamlit interface
                    {step_code.text}
                    Error: {e}

                    Please provide a new code snippet that fix it. Directly emit executable python code.
                """
            print(prompt)
            retry_code = st.session_state.google_gemini.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(temperature=0.1)
            )

            with st.chat_message("agent", avatar="🤖"):
                st.write_stream(stream_data(retry_code.text))


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