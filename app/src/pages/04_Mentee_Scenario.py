import streamlit as st

# Set page configuration
st.set_page_config(page_title="View Scenarios", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("View Scenarios")
st.divider()

# Mock Data for Scenario Practice
scenarios = [
    {"description": "Basic conversation scenario", "difficulty_level": "Beginner"},
    {"description": "Negotiation scenario", "difficulty_level": "Intermediate"},
    {"description": "Technical presentation", "difficulty_level": "Advanced"},
]

# Display Scenarios
st.subheader("Scenario Practice")
for scenario in scenarios:
    st.write(f"**Description:** {scenario['description']}")
    st.write(f"**Difficulty Level:** {scenario['difficulty_level']}")
    st.divider()
