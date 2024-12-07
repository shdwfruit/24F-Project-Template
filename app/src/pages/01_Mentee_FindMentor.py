import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Find a Mentor", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Find a Mentor")
st.divider()

# Initialize session state
if 'selected_mentor' not in st.session_state:
   st.session_state.selected_mentor = None
if 'mentor_data' not in st.session_state:
   st.session_state.mentor_data = None
if 'show_search_results' not in st.session_state:
   st.session_state.show_search_results = False

def select_mentor(mentor):
    st.session_state.selected_mentor = mentor
    st.session_state.show_search_results = False

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
       st.session_state.mentor_data = requests.get(
           'http://api:4000/me/mentors',
           params={
               'teaching_language': language,
               'language_level': level
           }
       ).json()
       st.session_state.show_search_results = True
       
   except Exception as e:
       st.write("**Important**: Could not connect to api")
       st.write(f"Error: {e}")

# Show search results
if st.session_state.show_search_results:
    if not st.session_state.mentor_data:
        st.info("Currently no mentor match")
    else:
        for mentor in st.session_state.mentor_data:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Name:** {mentor['first_name']} {mentor['last_name']}")
                st.write(f"**Email:** {mentor['email']}")
                st.write(f"**Teaching Language:** {mentor['teaching_language']}")
                st.write(f"**Language Level:** {mentor['language_level']}")
                st.divider()
            with col2:
                st.button(
                "Select Mentor",
                key=f"select_{mentor['id']}",
                on_click=select_mentor,
                args=(mentor,))

# Show registration form if mentor is selected
if st.session_state.selected_mentor:
    st.write("### Register as Mentee")
    st.write(f"Selected Mentor: {st.session_state.selected_mentor['first_name']} {st.session_state.selected_mentor['last_name']}")
   
    with st.form("mentee_registration"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        learning_language = st.selectbox(
            "Learning Language", 
            options=[st.session_state.selected_mentor['teaching_language']]
        )
        language_level = st.selectbox(
            "Language Level",
            options=["Beginner", "Intermediate", "Advanced", "Fluent"]
        )
        
        if st.form_submit_button("Register"):
            try:
                mentor_id = st.session_state.selected_mentor['id']
                if not mentor_id:
                    st.error()
                    st.stop()
                payload = {
                    'mentor_id': mentor_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'learning_language': learning_language,
                    'language_level': language_level
                }

                response = requests.post(
                    'http://api:4000/me/create',
                    json=payload
                )
               
                if response.status_code == 200:
                    st.success("Successfully registered as a mentee!")
                    # Clear the selected mentor and reset search
                    st.session_state.selected_mentor = None
                    st.session_state.show_search_results = False
                else:
                    st.error(f"Registration failed. Please try again. Server response: {response.text}")
                   
            except Exception as e:
                st.write("**Important**: Could not connect to api")
                st.write(f"Error: {e}")