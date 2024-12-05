import streamlit as st

# Set page title
def content_updates_page():
    st.title("Manage Content Updates")
    st.divider()

    # Connect to the MySQL
    def connect_to_db():
        from flaskext.mysql import MySQL
        from pymysql import cursors
        
        # Initialize MySQL connection
        mysql = MySQL(cursorclass=cursors.DictCursor)
        app = {}
        mysql.init_app(app)
        return mysql.get_db()
