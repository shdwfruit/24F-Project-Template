import streamlit as st
import requests
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="My Sessions", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Initialize session state for mentee info
if 'mentee_info' not in st.session_state:
    st.session_state['mentee_info'] = None

# Page Title
st.title("My Sessions")
st.divider()

# Email verification section
if not st.session_state.mentee_info:
    st.write("### Retrieve your sessions by email address")
    with st.form("email_verification", clear_on_submit=True):
        email = st.text_input("Enter your email")
        submit_button = st.form_submit_button("Retrieve Sessions")
        
        mentee_info = requests.get('http://api:4000/me/get_id', email)
        st.session_state.mentee_info = mentee_info

        if submit_button:
            try:
                payload = {'email': email}
                
                response = requests.post('http://api:4000/me/verify',json=payload)
                
                if response.status_code == 200:
                    mentee_data = response.json()
                    if 'error' in mentee_data:
                        st.error("Email not found. Please verify your email address.")
                    else:
                        st.session_state.mentee_info = mentee_data
                        st.success("Email verified successfully!")
                        st.rerun()  # Changed from experimental_rerun
                else:
                    st.error(f"Server returned status code: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Could not verify email: {str(e)}")

# Show session management after verification
elif st.session_state.mentee_info:
    st.write(f"Welcome, {st.session_state.mentee_info.get('first_name', '')} {st.session_state.mentee_info.get('last_name', '')}")
    
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
            
            st.write("Debug - Session State Info:")
            st.write(st.session_state.mentee_info)
            st.write("Debug - ID value:", st.session_state.mentee_info)
            st.write("Debug - ID type:", type(st.session_state.mentee_info))
            try:
                payload = {
                        'mentee_id': st.session_state.mentee_info['id'],
                        'mentor_id': st.session_state.mentee_info['id'],
                        'purpose': purpose,
                        'date': date.strftime('%Y-%m-%d'),
                        'duration': duration
                }
                st.write(f"Debug - Sending payload: {payload}")
                response = requests.post(
                    'http://api:4000/s/create',
                    json=payload
                )
                st.write(f"Debug - Response status: {response.status_code}")  # Debug print
                st.write(f"Debug - Response content: {response.text}")
                if response.status_code == 200:
                    st.success("Session scheduled successfully!")
                else:
                    st.error(f"Failed to schedule session. Server response: {response.text}")
            except Exception as e:
                st.error(f"Error scheduling session: {str(e)}")

                
    # Display existing sessions
    st.write("### My Sessions")
    try:
        response = requests.get(
            f"http://api:4000/s/mentee/{st.session_state.mentee_info['id']}"
        )
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
                    
    except Exception as e:
        st.error(f"Error loading sessions: {str(e)}")

    # Logout with unique key
    if st.button("Logout", key="logout_button"):
        st.session_state.mentee_info = None
        st.rerun()

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