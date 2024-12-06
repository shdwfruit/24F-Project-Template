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

# Get the mentee's ID from session state
mentee_id = st.session_state.get('mentee_info', {}).get('id', None)

if mentee_id is None:
    st.error("Mentee ID not found in session. Please log in.")
else:
    # Fetch learning path data for the mentee
    try:
        response = requests.get(f'http://api:4000/lp/learnmentee/{mentee_id}')
        response.raise_for_status()  # Raise exception for HTTP errors
        learning_paths = response.json()
    except requests.exceptions.RequestException as e:
        st.error("Could not connect to API for learning path data.")
        st.write(f"Error: {e}")
        learning_paths = []

    # Display each module
    if learning_paths:
        for path in learning_paths:
            st.write(f"### {path['module_name']}")
            st.write(f"**Description:** {path['description']}")
            st.write(f"**Status:** {path['status']}")

            st.write("**Milestones:**")
            # Parse and display milestones
            milestones = path['milestones'].split(", ")
            for milestone in milestones:
                st.checkbox(milestone, value=(path["status"] == "Completed"))

            st.divider()
    else:
        st.info("No learning paths found for your account.")

# Report an Issue Section
st.subheader("Report an issue")
description = st.text_area("Description (Functional, Visual, etc.)")
status = st.radio("Current Status", ["Active", "Inactive"])
reported_by = mentee_id

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
