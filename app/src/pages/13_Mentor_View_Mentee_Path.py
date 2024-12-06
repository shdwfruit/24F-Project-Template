import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="View Learning Path", layout="wide")
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)
# Page Title
st.title("My Mentee's Learning Path")
st.divider()
# Replace mock data with API call to get learning paths
mentee_id = st.session_state.get('mentee_id', 1)  # Example mentee_id for testing
try:
    learning_paths = requests.get(f'http://api:4000/lp/mentee/{mentee_id}').json()
except Exception as e:
    st.error(f"Error connecting to server: {str(e)}")
    learning_paths = []
# Display learning paths
for path in learning_paths:
    st.write(f"### {path['module_name']}")
    st.write(f"**Description:** {path['description']}")
    st.write(f"**Status:** {path['status']}")
    if path['completion_date']:
        st.write(f"**Completion Date:** {path['completion_date']}")
    else:
        st.write("**Completion Date:** Not Completed")
    st.write("**Milestones:**")
    for milestone in path["milestones"]:
        st.checkbox(milestone, value=(path["status"] == "Completed"))
    st.divider()

# Display each module
for path in learning_paths:
    st.write(f"### {path['module_name']}")
    st.write(f"**Description:** {path['description']}")
    st.write(f"**Status:** {path['status']}")
    if path['completion_date']:
        st.write(f"**Completion Date:** {path['completion_date']}")
    else:
        st.write("**Completion Date:** Not Completed")

    st.write("**Milestones:**")
    for milestone in path["milestones"]:
        st.checkbox(milestone, value=(path["status"] == "Completed"))

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


