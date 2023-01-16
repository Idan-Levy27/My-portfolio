import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your email address", key="email")
    raw_message = st.text_area("Your message", key="mess")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")