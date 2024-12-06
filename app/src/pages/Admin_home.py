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

# Navigation Logic Based on Query Params

if st.query_params["first_key"] == "content_updates":
    st.query_params["first_key"] = ""
    from pages.Admin_content_updates import content_updates_page
    content_updates_page()
elif st.query_params["first_key"] == "reported_issues":
    st.query_params["first_key"] = ""
    from pages.Admin_reported_issues import view_reported_issues_page
    view_reported_issues_page()
elif st.query_params["first_key"] == "analytics":
    st.query_params["first_key"] = ""
    from pages.Admin_Analytics import view_analytics_page
    view_analytics_page()