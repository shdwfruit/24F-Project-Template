import streamlit as st

# Set page configuration
st.set_page_config(page_title="Find a Mentor", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Find a Mentor")
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
        "keywords": keywords_list,
        "proficiency": proficiency,
        "languages": languages,
    }
    st.success("Filters applied. Mentor list updated!")  # Placeholder for filter logic

st.divider()
# Mock Mentor Data
mentors = [
    {"name": "John Doe", "description": "Fluent in English, located in London.", "badge": "Language Badge"},
    {"name": "Jane Smith", "description": "Advanced in Spanish, located in Barcelona.", "badge": "Culture Badge"},
    {"name": "Jim Beam", "description": "Fluent in French, located in Paris.", "badge": "Jack-of-all-Trades Badge"},
]


# Mentor List Display
st.subheader("Mentee Results")
mentor_cols = st.columns(3)

for i, mentor in enumerate(mentors):
    with mentor_cols[i % 3]:
        st.image("assets/user.png", width=150)
        st.write(f"### {mentor['name']}")
        st.write(mentor["description"])
        st.write(f"**Badge:** {mentor['badge']}")

# Add responsiveness based on screen size
st.divider()
st.write("End of results.")
