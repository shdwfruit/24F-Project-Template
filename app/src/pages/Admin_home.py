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
        st.query_params(page="content_updates")

with col2:
    if st.button("View Reported Issues", type="primary"):
        st.query_params(page="reported_issues")

with col3:
    if st.button("View Analytics", type="primary"):
        st.query_params(page="analytics")

st.divider()

# Navigation Logic Based on Query Params
params = st.query_params()
page = params.get("page", [""])[0]

if page == "content_updates":
    st.experimental_set_query_params()
    from pages.admin_content_updates import content_updates_page
    content_updates_page()
elif page == "reported_issues":
    st.experimental_set_query_params()
    from pages.admin_reported_issues import reported_issues_page
    reported_issues_page()
elif page == "analytics":
    st.experimental_set_query_params()
    from pages.admin_analytics import analytics_page
    analytics_page()