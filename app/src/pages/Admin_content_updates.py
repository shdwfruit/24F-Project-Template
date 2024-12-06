import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks

# set page layout
st.set_page_config(layout = 'wide')

# Set page title
st.title("Manage Content Updates")
st.divider()

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

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

with st.form("Add a New Content Update"):
    path_id = st.number_input("Learning Path ID", min_value=1, step=1)
    description = st.text_area("Description")
    submit_button = st.form_submit_button("Add Content")

    # Validate all fields are filled when form is submitted
    if submit_button:
        if not path_id:
            st.error("Please enter a path_id")
        elif not description:
            st.error("Please enter a content description")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            update_data = {
                "path_id": path_id,
                "updated_by": st.session_state['id'],
                "description": description
            }
            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Content submitted with data: {update_data}")
            
            # Now, we try to make a POST request to the proper end point
            try:
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.post('http://api:4000/c/update_content', json=update_data)
                if response.status_code == 200:
                    st.success("Content added successfully!")
                else:
                    st.error(f"Error adding content: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")

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
    st.success("Content updae updated successfully!")
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
