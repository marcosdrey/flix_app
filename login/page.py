import streamlit as st
from .service import login


def show_login():
    st.title('Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button('Login'):
        login(username, password)
