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