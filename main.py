import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Idan Levy")
    content = """Hi, I am Idan a Python programmer"""
    st.info(content)

apps_info = "Below you can find some of the apps I have built in Python. " \
            "Feel free to contact me!"

st.subheader(apps_info)