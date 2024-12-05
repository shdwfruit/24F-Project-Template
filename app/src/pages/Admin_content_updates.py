import streamlit as st
import requests

# Set page title
st.title("Manage Content Updates")
st.divider()

# Display content updates
content_updates = {}

try:
    content_updates = requests.get('http://api:4000/c/content_updates').json()
except Exception as e:
    st.write("**Important**: Could not connect to api")
    st.write(f"Error: {e}")

st.write("### Content Updates")
st.write(content_updates)

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
