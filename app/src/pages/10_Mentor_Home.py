import streamlit as st

# Set page configuration
st.set_page_config(page_title="Explore Language Partner", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("NU Global Connect")
st.write("I want to...")

# Mentor and Workshop Buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Find a Mentee", type="primary"):
        st.switch_page("pages/11_Mentor_FindMentee.py")

with col2:
    if st.button("View My Sessions", type="primary"):
        st.switch_page("pages/12_Mentor_View_Sessions.py")  # Add navigation logic here

with col3:
    if st.button("View My Mentee's Learning Path", type="primary"):
        st.switch_page("pages/13_Mentor_View_Mentee_Path.py")  # Add navigation logic here

st.divider()
