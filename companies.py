import streamlit as st
import pandas as pd
import numpy as np


def company_tab():

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


def company_rerank(user_search, k=5):

    if user_search is None or user_search == "":
        return "Please provide a company name to search for"

    st.session_state.logger.info(f"USER {st.session_state.session_id} : COMPANY_SEARCH : {user_search}")
    user_search_embds = st.session_state.embeddings.get_text_embedding(user_search)

    df = pd.read_json('notebooks/company_full.json')
    if 'embds' not in df.columns:
        df['embds'] = df['description'].apply(lambda x: st.session_state.embeddings.get_text_embedding(x))

    st.write("Companies ranked based on your search || Extracted using AI from https://www.nvidia.com/gtc/sponsors/#/ ")
    embeddings_array = np.stack(df['embds'].values)  # Convert embeddings list to a NumPy array for efficient computation
    df['distance'] = np.sqrt(np.sum((embeddings_array - user_search_embds) ** 2, axis=1))

    rerank_table = df.sort_values('distance')[['name', 'description']].head(k).to_markdown(index=False)
    st.session_state.chat_messages.append({"role": "assistant", "content": rerank_table})


def company_info_search(user_search):

    if user_search is None or user_search == "":
        return "Please provide a company name to search for"
    response = st.session_state.gemini_client.generate_content(user_search)
    st.session_state.chat_messages.append({"role": "assistant", "content": response.text})