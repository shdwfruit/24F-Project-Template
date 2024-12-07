import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="System Administrator Dashboard", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("System Administrator Dashboard")
st.write("Welcome, Priya! Choose an action below:")

# Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Manage Content Updates", type="primary"):
        st.switch_page("pages/Admin_content_updates.py")

with col2:
    if st.button("View Reported Issues", type="primary"):
        st.switch_page("pages/Admin_reported_issues.py")

with col3:
    if st.button("View Analytics", type="primary"):
        st.switch_page("pages/Admin_Analytics.py")

st.divider()

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