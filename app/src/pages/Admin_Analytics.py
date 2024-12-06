import streamlit as st
import requests

# set page layout
st.set_page_config(layout = 'wide')

# Set page title
st.title("Analytics Dashboard")
st.divider()

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Display engagement data
st.write("### Engagement and Completion Rates")

engagement_data = {}

try:
    engagement_data = requests.get('http://api:4000/a/engagement_data').json()
    with st.expander("All Engagement Data"):
        for data in engagement_data:
            st.write(f"**Module Name:** {data['module_name']}")
            st.write(f"**Engaged Students:** {data['engaged_students']}")
            st.write(f"**Completed Students:** {data['completed_students']}")
            st.divider()
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

st.divider()

# Display progress data
st.write("### Progress Over Time")

progress_data = {}

try:
    progress_data = requests.get('http://api:4000/p/progress_data').json()
    with st.expander("All Progress Data"):
        for data in progress_data:
            st.divider()
            st.write(f"**Module Name:** {data['module_name']}")
            st.write(f"**Status:** {data['status']}")
            st.write(f"**Completion Date:** {data['completion_date']}")
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

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