import streamlit as st

# Set page configuration
st.set_page_config(page_title="System Administrator Dashboard", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Set page title
st.title("Manage Content Updates")
st.divider()

# Page Title
st.title("System Administrator Dashboard")
st.write("Welcome, Priya! Choose an action below:")

# Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Manage Content Updates", type="primary"):
        st.switch_page("pages/Admin_content_updates.py")

with col2:
    if st.button("View Reported Issues", type="primary"):
        st.switch_page("pages/Admin_reported_issues.py")

with col3:
    if st.button("View Analytics", type="primary"):
        st.switch_page("pages/Admin_Analytics.py")

st.divider()