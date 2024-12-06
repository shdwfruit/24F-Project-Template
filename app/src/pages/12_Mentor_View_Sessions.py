import streamlit as st
from datetime import datetime
import requests

# Set page configuration
st.set_page_config(page_title="Manage Sessions", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("Manage My Sessions")
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

# Helper function to parse datetime from string
def parse_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")


# Initialize session state for the currently active session being edited
if "editing_session" not in st.session_state:
    st.session_state["editing_session"] = None

# Display Existing Sessions with Update Option
st.subheader("Your Sessions")
for idx, session in enumerate(sessions):
    st.write(f"**Purpose:** {session['purpose']}")
    st.write(f"**Date:** {session['date']}")
    st.write(f"**Duration:** {session['duration']}")
    st.write(f"**Mentor:** {session['mentor']}")
    st.write(f"**Feedback:** {session['feedback']}")

    # Update Session Button
    if st.button(f"Edit Session {idx + 1}"):
        st.session_state["editing_session"] = idx  # Track the session being edited

    # Check if the current session is being edited
    if st.session_state["editing_session"] == idx:
        st.write(f"### Editing Session {idx + 1}")
        updated_purpose = st.text_input(
            "Purpose", value=session["purpose"], key=f"purpose_{idx}"
        )
        updated_datetime = st.date_input(
            "Session Date",
            value=parse_datetime(session["date"]).date(),
            key=f"date_{idx}",
        )
        updated_time = st.time_input(
            "Session Time",
            value=parse_datetime(session["date"]).time(),
            key=f"time_{idx}",
        )
        updated_duration = st.text_input(
            "Duration (HH:MM:SS)",
            value=session["duration"],
            key=f"duration_{idx}",
        )
        updated_feedback = st.text_area(
            "Feedback", value=session["feedback"], key=f"feedback_{idx}"
        )

        # Combine updated date and time
        combined_updated_datetime = datetime.combine(
            updated_datetime, updated_time
        )

        # Save Updates Button
        if st.button(f"Save Updates for Session {idx + 1}", key=f"save_{idx}"):
            if combined_updated_datetime < datetime.now():
                st.error("The session date and time must be in the future.")
            elif not updated_duration.strip():
                st.error("Duration cannot be empty.")
            else:
                # Mock update to the session data
                session["purpose"] = updated_purpose
                session["date"] = combined_updated_datetime.strftime("%Y-%m-%d %H:%M")
                session["duration"] = updated_duration
                session["feedback"] = updated_feedback

                st.success(f"Session {idx + 1} updated successfully!")
                st.session_state["editing_session"] = None  # Clear editing state
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