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