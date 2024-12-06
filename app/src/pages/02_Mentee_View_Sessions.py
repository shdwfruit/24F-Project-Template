import streamlit as st
import requests
from datetime import datetime

# Set page config
st.set_page_config(page_title="My Sessions", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("My Sessions")
st.divider()

# Initialize mentee_info variable
mentee_info = None

# Email verification section
if not mentee_info:
    st.write("### Retrieve your sessions by email address")
    with st.form("email_verification", clear_on_submit=True):
        email = st.text_input("Enter your email")
        submit_button = st.form_submit_button("Retrieve Sessions")

        if submit_button:
            try:
                # Verify mentee by email
                payload = {'email': email}
                response = requests.post('http://api:4000/me/verify', json=payload)

                if response.status_code == 200:
                    mentee_data = response.json()
                    if 'error' in mentee_data:
                        st.error("Email not found. Please verify your email address.")
                    else:
                        mentee_info = mentee_data
                        st.success("Email verified successfully!")
                else:
                    st.error(f"Server returned status code: {response.status_code}")
            except Exception as e:
                st.error(f"Could not verify email: {str(e)}")

# Show session management after verification
if mentee_info:
    st.write(f"Welcome, {mentee_info['first_name']}")

    # Create new session section
    st.write("### Schedule New Session")
    with st.form("create_session", clear_on_submit=True):
        # Purpose
        purpose = st.text_area("Session Purpose")

        # Date picker (only future dates)
        min_date = datetime.now().date()
        date = st.date_input("Session Date", min_value=min_date)

        # Duration dropdowns
        col1, col2 = st.columns(2)
        with col1:
            hours = st.selectbox("Hours", range(0, 5), key="hours_select")
        with col2:
            minutes = st.selectbox("Minutes", [0, 15, 30, 45], key="minutes_select")

        # Format duration for MySQL TIME
        duration = f"{hours:02d}:{minutes:02d}:00"

        if st.form_submit_button("Schedule Session"):
            try:
                # Get mentor ID
                mentor_response = requests.get(f'http://api:4000/me/get_mentor_id/{mentee_info["id"]}')
                if mentor_response.status_code == 200:
                    mentor_data = mentor_response.json()
                    mentor_id = mentor_data['mentor_id']

                    # Prepare payload for scheduling session
                    payload = {
                        'mentee_id': mentee_info['id'],
                        'mentor_id': mentor_id,
                        'purpose': purpose,
                        'date': date.strftime('%Y-%m-%d'),
                        'duration': duration
                    }

                    # Schedule session
                    response = requests.post('http://api:4000/s/create', json=payload)

                    if response.status_code == 200:
                        st.success("Session scheduled successfully!")
                    else:
                        st.error(f"Failed to schedule session. Server response: {response.text}")
                else:
                    st.error(f"Error fetching mentor ID: {mentor_response.text}")
            except Exception as e:
                st.error(f"Error scheduling session: {str(e)}")

    # Display existing sessions
    st.write("### My Sessions")
    try:
        response = requests.get(f"http://api:4000/s/mentee/{mentee_info['id']}")
        if response.status_code == 200:
            sessions = response.json()

            if not sessions:
                st.info("No sessions found.")
            else:
                for idx, session in enumerate(sessions):
                    with st.container():
                        col1, col2 = st.columns([2, 1])
                        with col1:
                            st.write(f"**Date:** {session['date']}")
                            st.write(f"**Duration:** {session['duration']}")
                            st.write(f"**Purpose:** {session['purpose']}")
                        with col2:
                            st.write(f"**Mentor:** {session['mentor_name']}")
                            st.write(f"**Mentor Email:** {session['mentor_email']}")
                        st.divider()
        else:
            st.error(f"Error loading sessions: {response.status_code}. {response.text}")
    except Exception as e:
        st.error(f"Error loading sessions: {str(e)}")

# Report an issue section
st.subheader("Report an issue")
description = st.text_area("Description (Functional, Visual, etc.)")
status = st.radio("Current Status", ["Active", "Inactive"])
if st.button('Report Issue'):
    if not description:
        st.error("Please enter a description")
    elif not status:
        st.error("Please choose a status")
    else:
        data = {
            "reported_by": mentee_info['id'],
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
