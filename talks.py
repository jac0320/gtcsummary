import pandas as pd
import numpy as np
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from utils import collect_md_files
from constants import GTCSUMMARY_SEARCH_API_KEY, GTCSUMMARY_SEARCH_ENGINE_ID
from googleapiclient.discovery import build
from utils import find_most_similar_index


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



def talk_rerank(user_search, k=5):

    if user_search is None or user_search == "":
        return "Please provide a talk topic to search for"

    st.session_state.logger.info(f"USER {st.session_state.session_id} : COMPANY_SEARCH : {user_search}")
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/pdf_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['Title'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    st.write("Talks ranked based on your search || Extracted using AI from https://www.nvidia.com/en-us/on-demand/ ")
    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))

    rerank_table = df.sort_values('distance')[['Title']].head(k).to_markdown(index=False)
    st.session_state.chat_messages.append({"role": "assistant", "content": rerank_table})


def talk_info_search(search_title):

    if search_title is None or search_title == "":
        return "Please provide a talk title to search for"
    
    user_search_embds = st.session_state.embeddings.get_text_embedding(search_title)
    
    service = build("customsearch", "v1", developerKey=GTCSUMMARY_SEARCH_API_KEY)
    results = service.cse().list(q=search_title, cx=GTCSUMMARY_SEARCH_ENGINE_ID, num=5).execute()
    
    titles = [st.session_state.embeddings.get_text_embedding(i['title']) for i in results['items']]

    target = find_most_similar_index(user_search_embds, titles)
    target_url = results['items'][target]['link']

    response = f"Here is the link to the talk if you want to learn more: {target_url}"
    st.session_state.chat_messages.append({"role": "assistant", "content": response})