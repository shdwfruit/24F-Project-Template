import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Find a Mentee", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Find a Mentee")
st.divider()

# Selection dropdowns
language = st.selectbox(
    "Select Learning Language",
    options=["Japanese", "Spanish", "Chinese", "French"]
)

level = st.selectbox(
    "Select Language Level",
    options=["Beginner", "Intermediate", "Advanced", "Fluent"]
)

# Display mentee data
if st.button("Search"):
    try:
        mentee_data = requests.get(
            'http://api:4000/mo/get_mentees',
            params={
                'learning_language': language,
                'language_level': level
            }
        ).json()
        
        if not mentee_data:
            st.info("Currently no mentee match")
        else:
            for mentee in mentee_data:
                st.write(f"**Name:** {mentee['first_name']} {mentee['last_name']}")
                st.write(f"**Email:** {mentee['email']}")
                st.write(f"**Learning Language:** {mentee['learning_language']}")
                st.write(f"**Language Level:** {mentee['language_level']}")
                st.divider()
                
    except Exception as e:
        st.write("**Important**: Could not connect to API")
        st.write(f"Error: {e}")

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