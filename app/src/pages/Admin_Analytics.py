import streamlit as st

# Set page title
def view_analytics_page():
    st.title("Analytics Dashboard")
    st.divider()

    # Fetch engagement data
    @st.cache_data
    def fetch_engagement_data():
        cursor = db.get_db().cursor()
        query = """
        SELECT lp.module_name, 
               COUNT(p.id) AS engaged_students,
               SUM(p.status = 'Completed') AS completed_students
        FROM learning_path lp
        LEFT JOIN progress p ON lp.id = p.path_id
        GROUP BY lp.module_name;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    # Display engagement data
    st.write("### Engagement and Completion Rates")
    engagement_data = fetch_engagement_data()
    if engagement_data:
        for data in engagement_data:
            st.write(f"**Module Name:** {data['module_name']}")
            st.write(f"**Engaged Students:** {data['engaged_students']}")
            st.write(f"**Completed Students:** {data['completed_students']}")
            st.divider()
    else:
        st.write("No analytics data available.")

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
