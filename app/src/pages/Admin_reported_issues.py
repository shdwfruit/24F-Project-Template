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
if st.button("Resolve Issue"):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "UPDATE issue_report SET status = 'Resolved', resolved_by = %s WHERE id = %s;"
    cursor.execute(query, (resolved_by_admin_id, issue_id_to_resolve))
    connection.commit()
    cursor.close()
    connection.close()
    st.success(f"Issue {issue_id_to_resolve} resolved successfully!")
    st.experimental_rerun()
