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

    # Display content updates
    content_updates = fetch_content_updates()
    if content_updates:
        st.write("### Content Updates")
        st.write(content_updates)
    else:
        st.write("No content updates found.")

    st.divider()

    # Add a new content update
    st.subheader("Add a New Content Update")
    path_id = st.number_input("Learning Path ID", min_value=1, step=1)
    description = st.text_area("Description")
    if st.button("Add Content Update"):
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "INSERT INTO content_updates (path_id, updated_by, description) VALUES (%s, %s, %s);"
        cursor.execute(query, (path_id, 1, description))  # Replace "1" with the appropriate admin_id
        connection.commit()
        cursor.close()
        connection.close()
        st.success("Content update added successfully!")
        st.experimental_rerun()

    st.divider()

    # Update an existing content update
    st.subheader("Update an Existing Content Update")
    update_id = st.number_input("Content Update ID to Modify", min_value=1, step=1)
    new_description = st.text_area("New Description")
    if st.button("Update Content Update"):
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "UPDATE content_updates SET description = %s WHERE id = %s;"
        cursor.execute(query, (new_description, update_id))
        connection.commit()
        cursor.close()
        connection.close()
        st.success("Content update updated successfully!")
        st.experimental_rerun()

    st.divider()

    # Delete a content update
    st.subheader("Delete a Content Update")
    delete_id = st.number_input("Content Update ID to Delete", min_value=1, step=1)
    if st.button("Delete Content Update"):
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "DELETE FROM content_updates WHERE id = %s;"
        cursor.execute(query, (delete_id,))
        connection.commit()
        cursor.close()
        connection.close()
        st.success("Content update deleted successfully!")
        st.experimental_rerun()
