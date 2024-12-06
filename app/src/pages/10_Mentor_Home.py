import streamlit as st

# Set page configuration
st.set_page_config(page_title="Explore Language Partner", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("NU Global Connect")
st.write("I want to...")

# Mentor and Workshop Buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Find a Mentee", type="primary"):
        st.switch_page("pages/11_Mentor_FindMentee.py")

with col2:
    if st.button("View My Sessions", type="primary"):
        st.switch_page("pages/12_Mentor_View_Sessions.py")  # Add navigation logic here

with col3:
    if st.button("View My Mentee's Learning Path", type="primary"):
        st.switch_page("pages/13_Mentor_View_Mentee_Path.py")  # Add navigation logic here

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