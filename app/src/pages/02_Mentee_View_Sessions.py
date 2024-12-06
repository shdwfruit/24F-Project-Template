import streamlit as st
import requests
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="My Sessions", layout='wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Initialize session state for mentee info
if 'mentee_info' not in st.session_state:
    st.session_state.mentee_info = None

# Page Title
st.title("My Sessions")
st.divider()

# Email verification section
if not st.session_state.mentee_info:
    st.write("### Please Verify Your Email")
    with st.form("email_verification", clear_on_submit=True):
        email = st.text_input("Enter your email")
        submit_button = st.form_submit_button("Verify")
        
        if submit_button:
            try:
                payload = {'email': email}
                
                response = requests.post(
                    'http://api:4000/me/verify',
                    json=payload
                )
                
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
            try:
                response = requests.post(
                    'http://api:4000/s/create',
                    json={
                        'mentee_id': st.session_state.mentee_info['id'],
                        'mentor_id': st.session_state.mentee_info['mentor_id'],
                        'purpose': purpose,
                        'date': date.strftime('%Y-%m-%d'),
                        'duration': duration
                    }
                )
                if response.status_code == 201:
                    st.success("Session scheduled successfully!")
                else:
                    st.error("Failed to schedule session. Please try again.")
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