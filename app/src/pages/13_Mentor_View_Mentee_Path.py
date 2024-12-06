import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Mentor Dashboard", layout="wide")

# Page Title
st.title("Mentor Dashboard")
st.write("**Welcome, Mentor!**")
st.divider()

# Navigation Sidebar
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Tabbed learning path view
tabs = st.tabs(["Mentee Learning Paths"])
tab1 = tabs[0]

# Tab 1: Mentee Learning Paths
with tab1:
    st.subheader("View Mentee Learning Paths")

    mentee_id = st.number_input("Enter Mentee ID to View Learning Path", min_value=1, step=1, value=1)
    learning_path_data = {}

    try:
        # get learning path data for the specified mentee
        learning_path_data = requests.get(f'http://api:4000/lp/learnmentee/{mentee_id}').json()
    except Exception as e:
        st.write("**Important**: Could not connect to API for learning path data")
        st.write(f"Error: {e}")

    if learning_path_data:
        for path in learning_path_data:
            st.write(f"### {path['module_name']}")
            st.write(f"**Description:** {path['description']}")
            st.write(f"**Status:** {path['status']}")
            if path['completion_date']:
                st.write(f"**Completion Date:** {path['completion_date']}")
            else:
                st.write("**Completion Date:** Not Completed")

            st.write("**Milestones:**")
            for milestone in path["milestones"]:
                st.checkbox(milestone, value=(path["status"] == "Completed"))

            st.divider()
    else:
        st.write("No learning paths found for the specified mentee.")

#Report Issue Section 
st.subheader("Report an issue")
description = st.text_area("Description (Functional, Visual, etc.)")
status = st.radio("Current Status", ["Active", "Inactive"])
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
