import streamlit as st

def initialize_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_to_memory(role, content):
    st.session_state.chat_history.append({
        "role": role,
        "content": content
    })

def get_memory():
    return st.session_state.chat_history