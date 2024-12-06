import streamlit as st
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="View Sessions", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("My Sessions")
st.divider()

# Mock Data for Sessions and Mentors
mock_mentor = {"id": 1, "name": "John Doe"}  # Single mentor assigned to the mentee
sessions = [
    {
        "purpose": "Language practice",
        "date": "2024-11-01 10:00",
        "duration": "01:30:00",
        "mentor": "John Doe",
        "feedback": "Great progress made.",
    },
    {
        "purpose": "Cultural immersion",
        "date": "2024-11-02 14:00",
        "duration": "02:00:00",
        "mentor": "John Doe",
        "feedback": "Needs improvement in grammar.",
    },
]

# Display Existing Sessions
st.subheader("Your Sessions")
for session in sessions:
    st.write(f"**Purpose:** {session['purpose']}")
    st.write(f"**Date:** {session['date']}")
    st.write(f"**Duration:** {session['duration']}")
    st.write(f"**Mentor:** {session['mentor']}")
    st.write(f"**Feedback:** {session['feedback']}")
    st.divider()

# Request a New Session Section
st.subheader("Request a New Session")

# Dropdown for Mentor Selection
mentor_name = st.selectbox(
    "Select your mentor", [mock_mentor["name"], "No mentor assigned"]
)

# Input for Session Purpose
session_purpose = st.text_input("Session Purpose", placeholder="Enter the purpose of the session")

# Date-Time Picker with Future Validation
session_datetime = st.date_input("Session Date", min_value=datetime.today().date())
session_time = st.time_input("Session Time", value=datetime.now().time())

# Combine date and time
combined_datetime = datetime.combine(session_datetime, session_time)

# Display Combined Date-Time and Check if in the Future
if combined_datetime < datetime.now():
    st.warning("The session date and time must be in the future.")

# Fixed Duration for Sessions
session_duration = "01:00:00"  # Default to 1 hour

# Request Session Button
if st.button("Request Session"):
    if mentor_name == "No mentor assigned":
        st.error("Please select a mentor to request a session.")
    elif session_purpose.strip() == "":
        st.error("Please enter a purpose for the session.")
    elif combined_datetime < datetime.now():
        st.error("The session date and time must be in the future.")
    else:
        # Mock Database Update
        st.success(
            f"Session requested successfully with {mentor_name}!\n"
            f"**Purpose:** {session_purpose}\n"
            f"**Date and Time:** {combined_datetime.strftime('%Y-%m-%d %H:%M')}\n"
            f"**Duration:** {session_duration}"
        )
        # In real implementation, this is where you'd connect to the database or API.
