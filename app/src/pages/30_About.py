import streamlit as st
from modules.nav import SideBarLinks

# set page layout
st.set_page_config(layout = 'wide')

SideBarLinks(show_home=True)

st.title('Warehouse Manager Portal')

st.write('')
st.write('')
st.write('### Reports')

if st.button('Show All Reorders',
        type = 'primary',
        use_container_width=True):
    st.switch_page('pages/41_Reorders.py')

if st.button('Show Low Stock',
        type = 'primary',
        use_container_width=True):
    st.switch_page('pages/42_Low_Stock.py')

st.write('')
st.write('')
st.write('### New Products and Categories')

if st.button('Add New Product Category',
        type = 'primary',
        use_container_width=True):
    st.switch_page('pages/43_New_Cat.py')

if st.button('Add New Product',
        type = 'primary',
        use_container_width=True):
    st.switch_page('pages/44_New_Product.py')

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