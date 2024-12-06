import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="My Learning Path", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("My Learning Path")
st.divider()

# Buttons for Scenario and Vocabulary Practice
col1, col2 = st.columns(2)
with col1:
    if st.button("Access Scenario Practice"):
        st.switch_page("pages/04_Mentee_Scenario.py")

with col2:
    if st.button("Access Vocabulary Practice"):
        st.switch_page("pages/05_Mentee_Vocab.py")


st.subheader("Report an issue")
description = st.text_area("Description (Functional, Visual, etc.)")
status = st.radio("Current Status", 
                  ["Active", "Inactive"])
reported_by = st.session_state['id']
if st.button('Report Issue'):
    if not description:
        st.error("Please enter a description")
    elif not status:
        st.error("Please choose a status")
    else:
        data = {
            "reported_by": reported_by,
            "status": status,
            "description": description
        }
        
        try:
            response = requests.post('http://api:4000/ir/report_issue', json=data)
            if response.status_code == 200:
                st.success("Issue successfully reported!")
                st.balloons()
            else:
                st.error("Error reporting issue")
        except Exception as e:
            st.error(f"Error connecting to server: {str(e)}")

