import streamlit as st

def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None or st.session_state.role == "guest":
        unauthenticated_menu()
        return
    print(st.session_state.role)
    authenticated_menu()

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("Home.py", label="Home")
    st.sidebar.page_link("pages/1_Services.py", label="Services")
    st.sidebar.page_link("pages/login.py", label="Log in")

def authenticated_menu():
    st.sidebar.page_link("Home.py", label="Home")
    st.sidebar.page_link("pages/1_Services.py", label="Services")
    st.sidebar.page_link("pages/2_About.py", label="About")
    st.sidebar.page_link("pages/logout.py", label="Logout")

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None or st.session_state.role == "guest":
        st.switch_page("Home.py")
    menu()