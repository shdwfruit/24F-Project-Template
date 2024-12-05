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

    # Fetch content updates
    @st.cache_data
    def fetch_content_updates():
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "SELECT id, path_id, updated_by, timestamp, description FROM content_updates;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
