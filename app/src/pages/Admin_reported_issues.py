import streamlit as st
import requests

# set page layout
st.set_page_config(layout = 'wide')

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

st.title("View Reported Issues")
st.divider()

# Display reported issues
reported_issues = {}

try:
    reported_issues = requests.get('http://api:4000/ir/get_reports').json()
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

if len(reported_issues) > 0:
    st.write("### Open Reported Issues")
    for issue in reported_issues:
        st.write(f"**Issue ID:** {issue['id']}")
        st.write(f"**Description:** {issue['description']}")
        st.write(f"**Status:** {issue['status']}")
        st.write(f"**Timestamp:** {issue['timestamp']}")
        st.write(f"**Resolved By:** {issue['resolved_by'] if issue['resolved_by'] else 'Unresolved'}")
        st.divider()

    # Resolve an issue
    st.subheader("Resolve an Issue")
    issue_id_to_resolve = st.number_input("Enter Issue ID to Resolve", min_value=1, step=1)
    resolved_by_admin_id = st.number_input("Enter Admin ID", min_value=1, step=1)

    data = {
        "issue_id_to_resolve" : issue_id_to_resolve,
        "resolved_by_admin_id" : resolved_by_admin_id
    }

    response = {}

    if st.button("Resolve Issue"):
        try:
            response = requests.put('http://api:4000/ir/resolve', json=data)
            if response.status_code == 200:
                st.success(f"Issue {issue_id_to_resolve} has been resolved!")
            else:
                st.error("Invalid Admin or Issue ID was entered")
        except Exception as e:
            st.error("Could not connect to API")
else:
    st.write("### No Open Reported Issues")

