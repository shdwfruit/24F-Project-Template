import streamlit as st

# Set page configuration
st.set_page_config(page_title="View Vocabulary", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("View Vocabulary Practice")
st.divider()

# Mock Data for Vocabulary Practice
vocab = [
    {"context": "Daily activities vocabulary", "difficulty_level": "Beginner"},
    {"context": "Business vocabulary", "difficulty_level": "Intermediate"},
    {"context": "Technical terms", "difficulty_level": "Advanced"},
]

# Display Vocabulary
st.subheader("Vocabulary Practice")
for word in vocab:
    st.write(f"**Context:** {word['context']}")
    st.write(f"**Difficulty Level:** {word['difficulty_level']}")
    st.divider()
