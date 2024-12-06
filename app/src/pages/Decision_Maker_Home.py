import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Decision Maker Dashboard", layout="wide")

# Page Title
st.title("Decision Maker Dashboard")
st.write("**Welcome, Dr. Smith!**")
st.divider()

# Navigation Sidebar
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Tabbed Navigation for Decision Maker Functionalities
tab1, tab2, tab3, tab4 = st.tabs(
    ["Student Engagement Insights", "Progress Visualization", "Feedback Analysis", "Cultural Competence Trends"]
)

# Tab 1: Student Engagement Insights
with tab1:
    st.subheader("Insights on Student Engagement with Modules")

    engagement_data = {}

    try:
        engagement_data = requests.get('http://api:4000/dm/engagement').json()
    except Exception as e:
        st.write("**Important**: Could not connect to API for engagement data")
        st.write(f"Error: {e}")

    if engagement_data:
        for data in engagement_data:
            st.write(f"**Module Name:** {data['module_name']}")
            st.write(f"**Engaged Students:** {data['engaged_students']}")
            st.divider()
    else:
        st.write("No data available for student engagement.")

# Tab 2: Progress Visualization
with tab2:
    st.subheader("Visualization of Student Progress Over Time")

    mentee_id = st.number_input("Enter Mentee ID for Progress Visualization", min_value=1, step=1, value=1)
    progress_data = {}

    try:
        progress_data = requests.get(f'http://api:4000/dm/progress/{mentee_id}').json()
    except Exception as e:
        st.write("**Important**: Could not connect to API for progress data")
        st.write(f"Error: {e}")

    if progress_data:
        for data in progress_data:
            st.write(f"**Mentee ID:** {data['mentee_id']}")
            st.write(f"**Status:** {data['status']}")
            st.write(f"**Completion Date:** {data['completion_date']}")
            st.divider()
    else:
        st.write("No progress data available for visualization.")

# Tab 3: Feedback Analysis
with tab3:
    st.subheader("Review and Organize Student Feedback")

    feedback_data = {}

    try:
        feedback_data = requests.get('http://api:4000/dm/feedback').json()
    except Exception as e:
        st.write("**Important**: Could not connect to API for feedback data")
        st.write(f"Error: {e}")

    if feedback_data:
        for data in feedback_data:
            st.write(f"**Session ID:** {data['session_id']}")
            st.write(f"**Feedback:** {data['feedback']}")
            st.write(f"**Session Purpose:** {data['purpose']}")
            st.write(f"**Session Date:** {data['date']}")
            st.divider()
    else:
        st.write("No feedback data available.")

# Tab 4: Cultural Competence Trends
with tab4:
    st.subheader("Automated Reports on Cultural Competence Trends")

    competence_data = {}

    try:
        competence_data = requests.get('http://api:4000/dm/trends').json()
    except Exception as e:
        st.write("**Important**: Could not connect to API for competence trends data")
        st.write(f"Error: {e}")

    if competence_data:
        for data in competence_data:
            st.write(f"**Module Name:** {data['module_name']}")
            st.write(f"**Completions:** {data['completions']}")
            st.write(f"**Average Completion Time:** {data['avg_completion_time']} days")
            st.divider()
    else:
        st.write("No data available for cultural competence trends.")

# Divider
st.divider()
st.write("End of Decision Maker Dashboard")

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
