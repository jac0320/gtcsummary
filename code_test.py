import streamlit as st

TEST_CODE = """
import streamlit as st

# Step 1: Add a sidebar with a "My Notes" tab
st.sidebar.title("My Notes")

# Step 2: List the topics that Site wrote notes on
topics = ["Retrieval vs. Generation", "The Need for Scalable Inference", "The Economics of AI", "Long-context vs. RAG", "Democratizing AI", "The World of Agents", "What the heck is this NIM?"]
for topic in topics:
    st.sidebar.markdown(f"- [{topic}](#{topic.replace(' ', '-')})")

# Step 3: Display the notes for the selected topic
if "topic" in st.experimental_get_query_params():
    topic = st.experimental_get_query_params()["topic"][0]
    notes = st.markdown(f"## {topic}")
else:
    notes = st.markdown("## My Notes")
"""

def main():

    st.code(TEST_CODE, language="python")
    exec(TEST_CODE)

main()