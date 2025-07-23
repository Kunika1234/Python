import streamlit as st
from googlesearch import search

st.title("Google Search with Python")

query = st.text_input("Search on Google:")

if query:
    for result in search(query, num_results=3):
        st.write(result)