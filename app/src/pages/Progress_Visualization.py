import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Progress Visualization", layout="wide")

# Page Title
st.title("Progress Visualization")
st.divider()

# Navigation Sidebar
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Main content
st.subheader("Visualization of Student Progress Over Time")

mentee_id = st.number_input("Enter Mentee ID for Progress Visualization", min_value=1, step=1, value=1)
progress_data = {}

try:
    progress_data = requests.get(f'http://api:4000/dm/progress/{mentee_id}').json()
except Exception as e:
    st.write("**Important**: Could not connect to API for progress data")
    st.write(f"Error: {e}")

if progress_data:
    for data in progress_data:
        st.write(f"**Mentee ID:** {data['mentee_id']}")
        st.write(f"**Status:** {data['status']}")
        st.write(f"**Completion Date:** {data['completion_date']}")
        st.divider()
else:
    st.write("No progress data available for visualization.")

# Report an issue section
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
