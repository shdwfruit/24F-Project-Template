import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Cultural Competence Trends", layout="wide")

# Page Title
st.title("Cultural Competence Trends")
st.divider()

# Navigation Sidebar
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Main content
st.subheader("Automated Reports on Cultural Competence Trends")

competence_data = {}

try:
    competence_data = requests.get('http://api:4000/dm/trends').json()
except Exception as e:
    st.write("**Important**: Could not connect to API for competence trends data")
    st.write(f"Error: {e}")

if competence_data:
    for data in competence_data:
        st.write(f"**Module Name:** {data['module_name']}")
        st.write(f"**Completions:** {data['completions']}")
        st.write(f"**Average Completion Time:** {data['avg_completion_time']} days")
        st.divider()
else:
    st.write("No data available for cultural competence trends.")

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