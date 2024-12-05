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
