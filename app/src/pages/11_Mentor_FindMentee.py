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
