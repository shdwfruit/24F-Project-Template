import streamlit as st

# Set page title
def view_reported_issues_page():
    st.title("View Reported Issues")
    st.divider()

    # Connect to the shared MySQL
    def connect_to_db():
        from flaskext.mysql import MySQL
        from pymysql import cursors

        # Initialize MySQL connection
        mysql = MySQL(cursorclass=cursors.DictCursor)
        app = {}  # Mock app for demo
        mysql.init_app(app)
        return mysql.get_db()

    # Fetch reported issues
    @st.cache_data
    def fetch_reported_issues():
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT ir.id, ir.description, ir.status, ir.timestamp, 
               sa.first_name AS resolved_by
        FROM issue_report ir
        LEFT JOIN system_administrator sa ON ir.resolved_by = sa.id
        WHERE ir.status = 'Open';
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    # Display reported issues
    reported_issues = fetch_reported_issues()
    if reported_issues:
        st.write("### Open Reported Issues")
        for issue in reported_issues:
            st.write(f"**Issue ID:** {issue['id']}")
            st.write(f"**Description:** {issue['description']}")
            st.write(f"**Status:** {issue['status']}")
            st.write(f"**Timestamp:** {issue['timestamp']}")
            st.write(f"**Resolved By:** {issue['resolved_by'] if issue['resolved_by'] else 'Unresolved'}")
            st.divider()
    else:
        st.write("No open reported issues found.")

