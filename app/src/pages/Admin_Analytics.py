import streamlit as st
import requests

# Set page title
st.title("Analytics Dashboard")
st.divider()

# Display engagement data
st.write("### Engagement and Completion Rates")

engagement_data = {}

try:
    engagement_data = requests.get('http://web-api:4000/analytics/engagement_data').json()
except:
    st.write("**Important**: Could not connect to api")

for data in engagement_data:
    st.write(f"**Module Name:** {data['module_name']}")
    st.write(f"**Engaged Students:** {data['engaged_students']}")
    st.write(f"**Completed Students:** {data['completed_students']}")
    st.divider()

# Fetch progress data over time
@st.cache_data
def fetch_progress_data():
    cursor = db.get_db().cursor()
    query = """
    SELECT lp.module_name, p.status, p.completion_date
    FROM progress p
    JOIN learning_path lp ON p.path_id = lp.id
    WHERE p.completion_date IS NOT NULL
    ORDER BY p.completion_date ASC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Display progress data
st.write("### Progress Over Time")
progress_data = fetch_progress_data()
if progress_data:
    for data in progress_data:
        st.write(f"**Module Name:** {data['module_name']}")
        st.write(f"**Status:** {data['status']}")
        st.write(f"**Completion Date:** {data['completion_date']}")
        st.divider()
else:
    st.write("No progress data available.")

try:
    data = requests.get('http://api:4000/data').json()
except:
    st.write("**Important**: Could not connect to api")