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
    engagement_data = requests.get('http://localhost:4000/a/engagement_data').json()
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

for data in engagement_data:
    st.write(f"**Module Name:** {data['module_name']}")
    st.write(f"**Engaged Students:** {data['engaged_students']}")
    st.write(f"**Completed Students:** {data['completed_students']}")
    st.divider()

# Display progress data
st.write("### Progress Over Time")

progress_data = {}

try:
    progress_data = requests.get('http://localhost:4000/p/progress_data').json()
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

for data in progress_data:
    st.write(f"**Module Name:** {data['module_name']}")
    st.write(f"**Status:** {data['status']}")
    st.write(f"**Completion Date:** {data['completion_date']}")
    st.divider()