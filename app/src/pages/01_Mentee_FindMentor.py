import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Find a Mentor", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Find a Mentor")
st.divider()

# Selection dropdowns
language = st.selectbox(
    "Select Teaching Language",
    options=["Japanese", "Spanish", "Chinese", "French"]
)

level = st.selectbox(
    "Select Language Level",
    options=["Advanced", "Fluent"]
)

# Display mentor data
if st.button("Search"):
    try:
        mentor_data = requests.get(
            'http://api:4000/me/mentors',
            params={
                'teaching_language': language,
                'language_level': level
            }
        ).json()
        
        if not mentor_data:
            st.info("Currently no mentor match")
        else:
            for mentor in mentor_data:
                st.write(f"**Name:** {mentor['first_name']} {mentor['last_name']}")
                st.write(f"**Email:** {mentor['email']}")
                st.write(f"**Teaching Language:** {mentor['teaching_language']}")
                st.write(f"**Language Level:** {mentor['language_level']}")
                st.divider()
                
    except Exception as e:
        st.write("**Important**: Could not connect to api")
        st.write(f"Error: {e}")