import streamlit as st

# Set page configuration
st.set_page_config(page_title="View Sessions", layout="wide")

# Page Title
st.title("My Sessions")
st.divider()

# Display Sessions
st.subheader("Session Details")
# Mock Data
sessions = [
    {
        "purpose": "Language practice",
        "date": "2024-11-01",
        "duration": "01:30:00",
        "mentor": "John Doe",
        "feedback": "Great progress made."
    },
    {
        "purpose": "Cultural immersion",
        "date": "2024-11-02",
        "duration": "02:00:00",
        "mentor": "Jane Smith",
        "feedback": "Needs improvement in grammar."
    },
    {
        "purpose": "Exam preparation",
        "date": "2024-11-03",
        "duration": "01:45:00",
        "mentor": "Jim Beam",
        "feedback": "Excellent comprehension."
    }
]

# Display each session
for session in sessions:
    st.write(f"**Purpose:** {session['purpose']}")
    st.write(f"**Date:** {session['date']}")
    st.write(f"**Duration:** {session['duration']}")
    st.write(f"**Mentor:** {session['mentor']}")
    st.write(f"**Feedback:** {session['feedback']}")
    st.divider()

