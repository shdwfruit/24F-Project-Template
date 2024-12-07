# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Mentee ------------------------
def MenteeHomeNav():
    st.sidebar.page_link("pages/00_Mentee_Home.py", label="Mentee Home")

#### ------------------------ Mentor ------------------------
def MentorHomeNav():
    st.sidebar.page_link("pages/10_Mentor_Home.py", label="Mentor Home")

#### ------------------------ Admin ------------------------
def AdminHomeNav():
    st.sidebar.page_link("pages/Admin_home.py", label="Admin Home")

#### ------------------------ DM ------------------------
def DMHomeNav():
    st.sidebar.page_link("pages/Decision_Maker_Home.py", label="Decision Maker Home")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")
        if "id" not in st.session_state:
            st.session_state.id = '0'

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'mentee':
            # role functions, add later
            MenteeHomeNav()

        if st.session_state['role'] == 'mentor':
            # role functions, add later
            MentorHomeNav()

        if st.session_state['role'] == 'administrator':
            # role functions, add later
            AdminHomeNav()

        if st.session_state['role'] == 'decision_maker':
            # role functions, add later
            DMHomeNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.switch_page("Home.py")