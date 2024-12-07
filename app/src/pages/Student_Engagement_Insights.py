import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Student Engagement Insights", layout="wide")

# Page Title
st.title("Student Engagement Insights")
st.divider()

# Navigation Sidebar
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Main content
st.subheader("Insights on Student Engagement with Modules")

engagement_data = {}

try:
    engagement_data = requests.get('http://api:4000/dm/engagement').json()
except Exception as e:
    st.write("**Important**: Could not connect to API for engagement data")
    st.write(f"Error: {e}")

if engagement_data:
    for data in engagement_data:
        st.write(f"**Module Name:** {data['module_name']}")
        st.write(f"**Engaged Students:** {data['engaged_students']}")
        st.divider()
else:
    st.write("No data available for student engagement.")

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
