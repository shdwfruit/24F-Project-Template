import streamlit as st
from modules.nav import SideBarLinks
import streamlit as st

# Initialize session state key if it doesn't exist
if 'id' not in st.session_state:
    st.session_state['id'] = None  # or a default value





# set page layout
st.set_page_config(layout = 'wide')

SideBarLinks(show_home=True)

st.title('About Us')

st.write('')
st.write('')
st.write(''' NU Global Connect is a data-driven application designed to prepare Northeastern students for international internships and co-ops by fostering cultural awareness and adaptability. With Northeasterns expanding global footprint—including 13 campuses across the U.S., U.K., and Canada, and over 70 Dialogue of Civilizations programs worldwide—students frequently engage in diverse cultural environments. However, many lack the
          structured resources needed to navigate new workplace cultures and communicate effectively in intercultural settings. This app bridges that gap by providing a comprehensive, personalized, and interactive approach to cultural preparedness. Leveraging student progress and engagement data, NU Global Connect adapts its content to ensure relevance and impact. It addresses critical pain points, such as limited access to tailored 
          cultural training and language practice tools specific to a students target country.Through features like interactive cultural etiquette modules, AI-driven language practice, and a progress-tracking dashboard, students gain practical skills in intercultural communication. The platform empowers them to transition seamlessly into international settings with confidence and competence.NU Global Connect caters to diverse user personas, 
          including students, language mentors, system administrators, and decision-makers. Tailored features like culture-specific training, personalized language matching, and competency tracking align with Northeasterns commitment to global experiential learning, ensuring smooth and successful student transitions across regions. ''')



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