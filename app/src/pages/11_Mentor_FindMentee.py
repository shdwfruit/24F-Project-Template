import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(page_title="Find a Mentee", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Find a Mentee")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("### Your Language Proficiency")
    proficiency = st.multiselect(
        "Select Proficiency Levels",
        options=["Beginner", "Intermediate", "Advanced"],
        default=["Beginner", "Intermediate", "Advanced"],
    )

with col2:
    st.write("### Select Language")
    languages = st.multiselect(
        "Select Languages",
        options=["Japanese", "Spanish", "Chinese"],
        default=["Japanese", "Spanish", "Chinese"],
    )

# "Search" Button
if st.button("Search"):
    st.session_state["filters"] = {
        "proficiency": proficiency,
        "languages": languages,
    }
    st.success("Filters applied. Mentor list updated!")  # Placeholder for filter logic

st.divider()

#get mentors from the database
mentor_data = []  # Placeholder for mentor data
try:
    response = requests.get("http://api:4000/mo/get_mentees")
    response.raise_for_status()  # Raise an error for bad status codes
    mentor_data = response.json()
except requests.exceptions.RequestException as e:
    st.write("**Important**: Could not connect to API")
    st.write(f"Error: {e}")



# Mentor List Display
st.subheader("Mentee Results")
mentor_cols = st.columns(3)

for i, mentor in enumerate(mentor_data):
    with mentor_cols[i % 3]:
        st.image("assets/user.png", width=150)
        st.write(f"### {mentor['name']}")
        st.write(mentor["description"])
        st.write(f"**Badge:** {mentor['badge']}")

# Add responsiveness based on screen size
st.divider()
st.write("End of results.")
