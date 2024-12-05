import streamlit as st

# Set page configuration
st.set_page_config(page_title="System Administrator Dashboard", layout="wide")

# Page Title
st.title("System Administrator Dashboard")
st.write("Welcome, Priya! Choose an action below:")

# Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Manage Content Updates", type="primary"):
        st.query_params["first_key"] = "content_updates"

with col2:
    if st.button("View Reported Issues", type="primary"):
        st.query_params["first_key"] = "reported_issues"

with col3:
    if st.button("View Analytics", type="primary"):
        st.query_params["first_key"] = "analytics"

st.divider()

# Navigation Logic Based on Query Params

if st.query_params["first_key"] == "content_updates":
    st.query_params["first_key"] = ""
    from pages.Admin_content_updates import content_updates_page
    content_updates_page()
elif st.query_params["first_key"] == "reported_issues":
    st.query_params["first_key"] = ""
    from pages.Admin_reported_issues import reported_issues_page
    reported_issues_page()
elif st.query_params["first_key"] == "analytics":
    st.query_params["first_key"] = ""
    from pages.Admin_Analytics import analytics_page
    analytics_page()