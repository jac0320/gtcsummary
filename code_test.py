import streamlit as st

CODE_STRING = """
import streamlit as st

st.write("Hello world from string!")

with open(str('summarized_notes/personal_notes/the_economics_of_ai.md'), "r") as file:
    st.markdown(file.read())
"""


def main():
    st.write("Hello world!")

    exec(CODE_STRING)


main()