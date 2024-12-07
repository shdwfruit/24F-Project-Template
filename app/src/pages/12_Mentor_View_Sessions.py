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

# Helper function to parse datetime from string
def parse_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

# Initialize session state for the currently active session being edited
if "editing_session" not in st.session_state:
    st.session_state["editing_session"] = None

try:
    response = requests.get(f'http://api:4000/s/mentee/{st.session_state.id}').json()
    # Display Existing Sessions with Update Option
    st.subheader("Your Sessions")
    for idx, session in enumerate(response):
        st.divider()
        st.write(f"**Purpose:** {session['purpose']}")
        st.write(f"**Date:** {session['date']}")
        st.write(f"**Duration:** {session['duration']}")
        st.write(f"**Mentor:** {session['mentor_name']}")
except Exception as e:
    st.error(f"Error connecting to server: {str(e)}")

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