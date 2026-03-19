import streamlit as st

st.title("Upload a text file")

text_file=st.file_uploader("Upload a text file ", type="txt")

if text_file is not None:
    content=text_file.read().decode("utf-8")
    st.text(content)