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

for content in content_updates:
    st.write(f"**Description:** {content['description']}")
    st.write(f"**Path ID:** {content['path_id']}")
    st.write(f"**Timestamp:** {content['timestamp']}")
    st.write(f"**Updated By:** {content['updated_by']}")
    st.divider()

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
                    st.balloons()
                else:
                    st.error(f"Error adding content: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
                
st.divider()

# Delete a content update
st.subheader("Delete a Content Update")
delete_id = st.number_input("Content Update ID to Delete", min_value=1, step=1)
if st.button("Delete Content Update"):
    try:
        response = requests.delete(f'http://api:4000/c/delete/{delete_id}')
        if response.status_code == 200:
            st.success(f"Content ID: {delete_id} has been deleted!")
        else:
            st.error("Invalid Content ID was entered")
    except Exception as e:
        st.error("Could not connect to API")

st.subheader("Report an issue")
description = st.text_area("Description (Functional, Visual, etc.)")
status = st.radio("Current Status", 
                  ["Active", "Inactive"])
reported_by = st.session_state['id']
if st.button('Report Issue'):
    if not description:
        st.error("Please enter a description")
    elif not status:
        st.error("Please choose a status")
    else:
        data = {
            "reported_by": reported_by,
            "status": status,
            "description": description
        }
        
        try:
            response = requests.post('http://api:4000/ir/report_issue', json=data)
            if response.status_code == 200:
                st.success("Issue successfully reported!")
                st.balloons()
            else:
                st.error("Error reporting issue")
        except Exception as e:
            st.error(f"Error connecting to server: {str(e)}")