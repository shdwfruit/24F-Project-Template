import streamlit as st

# Set page configuration
st.set_page_config(page_title="Explore Language Partner", layout="wide")

from modules.nav import SideBarLinks
SideBarLinks(show_home=True)

# Page Title
st.title("NU Global Connect")
st.write("I want to...")

# Mentor and Workshop Buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Find a Mentor", type="primary"):
        st.switch_page("pages/01_Mentee_FindMentor.py")

with col2:
    if st.button("View My Sessions", type="primary"):
        st.switch_page("pages/02_Mentee_View_Sessions.py")  # Add navigation logic here

with col3:
    if st.button("View My Learning Path", type="primary"):
        st.switch_page("pages/03_Mentee_View_Learningpath.py")  # Add navigation logic here

st.divider()

# Upcoming Workshops Section
st.subheader("Upcoming Workshops")
st.write("""
- Discover the culture of your next co-op destination.
- Connect with mentors and peers.
- Strengthen your soft skills for a global career.
""")

st.write('')

# Mock Data for Workshops
mock_workshops = [
    {"title": "Cross-Cultural Communication", "host": "Alejandro Martinez", "description": "Learn how to communicate effectively across cultures."},
    {"title": "Resume Building for Global Careers", "host": "Emma Lee", "description": "Enhance your resume for international opportunities."},
    {"title": "Preparing for Your First Co-op", "host": "Sophia Chan", "description": "Get tips on excelling in your first co-op."}
]

# Display Workshops
cols = st.columns(len(mock_workshops))
for i, workshop in enumerate(mock_workshops):
    with cols[i]:
        st.image("assets/user.png", width=100)  # Profile Picture
        st.write(f"### {workshop['title']}")
        st.write(f"**Host:** {workshop['host']}")
        st.write(workshop['description'])
