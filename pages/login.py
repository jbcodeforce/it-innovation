import streamlit as st
from menu import menu
import streamlit_authenticator as stauth

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role



st.selectbox(
    "Select your role:",
    [None, "guest", "logged"],
    key="_role",
    on_change=set_role,
)

menu()