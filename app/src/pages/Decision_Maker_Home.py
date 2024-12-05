import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Decision Maker Dashboard", layout="wide")

# Page Title
st.title("Decision Maker Dashboard")
st.write("**Welcome, Dr. Smith!**")
st.divider()

# Mock Data for Front-end Trial 
engagement_data = [
    {"module_name": "Module 1", "engaged_students": 20},
    {"module_name": "Module 2", "engaged_students": 35},
    {"module_name": "Module 3", "engaged_students": 15},
]

progress_data = [
    {"mentee_id": 1, "status": "Completed", "completion_date": "2024-10-15"},
    {"mentee_id": 2, "status": "In Progress", "completion_date": "2024-11-10"},
    {"mentee_id": 3, "status": "Not Started", "completion_date": None},
]

feedback_data = [
    {"session_id": 1, "description": "Excellent comprehension demonstrated."},
    {"session_id": 2, "description": "Needs improvement in technical accuracy."},
    {"session_id": 3, "description": "Great progress on cultural awareness."},
]

competence_data = [
    {"module_name": "Module 1", "completions": 15, "avg_completion_time": 7},
    {"module_name": "Module 2", "completions": 25, "avg_completion_time": 5},
    {"module_name": "Module 3", "completions": 10, "avg_completion_time": 10},
]

# Tabbed Navigation for Decision Maker Functionalities
tab1, tab2, tab3, tab4 = st.tabs(
    ["Student Engagement Insights", "Progress Visualization", "Feedback Analysis", "Cultural Competence Trends"]
)

# Tab 1: Student Engagement Insights
with tab1:
    st.subheader("Insights on Student Engagement with Modules")

    # Display engagement data
    if engagement_data:
        st.write("**Engagement Overview**")
        df_engagement = pd.DataFrame(engagement_data)
        st.dataframe(df_engagement, use_container_width=True)
    else:
        st.write("No data available for student engagement.")

# Tab 2: Progress Visualization
with tab2:
    st.subheader("Visualization of Student Progress Over Time")

    # Display progress data
    if progress_data:
        df_progress = pd.DataFrame(progress_data)
        st.write("**Progress Data**")
        st.dataframe(df_progress, use_container_width=True)

        # Visualization: Progress over time (example: status count)
        progress_counts = df_progress["status"].value_counts()
        st.bar_chart(progress_counts)
    else:
        st.write("No progress data available for visualization.")

            filtered_feedback = df_feedback[df_feedback["description"].str.contains(feedback_filter, case=False, na=False)]
            st.write(f"Filtered Feedback for: {feedback_filter}")
            st.dataframe(filtered_feedback, use_container_width=True)
    else:
        st.write("No feedback data available.")

# Tab 4: Cultural Competence Trends
with tab4:
    st.subheader("Automated Reports on Cultural Competence Trends")

    # Display cultural competence trends
    if competence_data:
        df_competence = pd.DataFrame(competence_data)
        st.write("**Cultural Competence Trends**")
        st.dataframe(df_competence, use_container_width=True)

        # Visualization: Trends in average completion time
        st.bar_chart(df_competence.set_index("module_name")["avg_completion_time"])
    else:
        st.write("No data available for cultural competence trends.")

# Divider
st.divider()
st.write("End of Decision Maker Dashboard")
