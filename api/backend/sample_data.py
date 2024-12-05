from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Number of rows to generate
num_rows = 40
num_admins = 10
num_badges = 10
num_mentors = 10
num_paths = 40

# Helper functions
def generate_language_level(table_type):
    levels = {
        "mentee": ["Beginner", "Intermediate", "Advanced", "Fluent"],
        "mentor": ["Advanced", "Fluent"],
        "practice": ["Beginner", "Intermediate", "Advanced", "Fluent"]
    }
    return random.choice(levels.get(table_type, []))

def generate_status():
    return random.choice(["Open", "Resolved", "Pending", "In Progress", "Completed", "Not Started"])

def generate_difficulty():
    return random.choice(["Beginner", "Intermediate", "Advanced", "Fluent"])

# Generate mock data for each table
def generate_system_admin_data():
    data = []
    for _ in range(num_admins):
        data.append({
            "email": fake.unique.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": random.choice(["System Admin", "Content Manager", "Support Specialist"]),
        })
    return data

def generate_mentee_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentor_id": random.randint(1, num_mentors),
            "admin_id": random.randint(1, num_admins),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "learning_language": random.choice(["Japanese", "Spanish", "Chinese", "French"]),
            "language_level": generate_language_level("mentee"),
        })
    return data

def generate_mentor_data():
    data = []
    for _ in range(num_mentors):
        data.append({
            "admin_id": random.randint(1, num_admins),
            "badge_id": random.randint(1, num_badges),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "teaching_language": random.choice(["Japanese", "Spanish", "Chinese", "French"]),
            "location": f"{fake.city()}, {fake.country()}",
            "language_level": generate_language_level("mentor"),
        })
    return data

def generate_learning_path_data():
    data = []
    for _ in range(num_paths):
        data.append({
            "mentee_id": random.randint(1, num_rows),
            "dm_id": random.randint(1, num_admins),
            "module_name": f"Module {random.randint(1, 5)}",
            "description": fake.text(max_nb_chars=50),
            "milestones": ", ".join([f"Milestone {i}" for i in range(1, 4)]),
            "status": generate_status(),
        })
    return data

def generate_progress_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentee_id": random.randint(1, num_rows),
            "path_id": random.randint(1, num_paths),
            "status": generate_status(),
            "completion_date": fake.date_between(start_date='-1y', end_date='today') if random.random() > 0.3 else None,
        })
    return data

def generate_issue_report_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "reported_by": random.randint(1, num_rows),
            "resolved_by": random.randint(1, num_admins) if random.random() > 0.5 else None,
            "status": generate_status(),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_content_update_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, num_paths),
            "updated_by": random.randint(1, num_admins),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_session_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentee_id": random.randint(1, num_rows),
            "mentor_id": random.randint(1, num_mentors),
            "purpose": fake.text(max_nb_chars=50),
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "duration": f"{random.randint(0, 3):02}:{random.randint(0, 59):02}:00",
        })
    return data

def generate_feedback_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "session_id": random.randint(1, num_rows),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_scenario_practice_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, num_paths),
            "description": fake.text(max_nb_chars=50),
            "difficulty_level": generate_difficulty(),
        })
    return data

def generate_vocab_practice_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, num_paths),
            "context": fake.text(max_nb_chars=50),
            "difficulty_level": generate_difficulty(),
        })
    return data

# Format data as SQL INSERT statements
def format_sql_inserts(table_name, data):
    sql = f"INSERT INTO {table_name} VALUES\n"
    rows = []
    for row in data:
        values = ', '.join([f"'{v}'" if v is not None else 'NULL' for v in row.values()])
        rows.append(f"({values})")
    sql += ',\n'.join(rows) + ";"
    return sql

# Generate and print SQL for each table
print("-- System Administrator Data")
print(format_sql_inserts("system_administrator", generate_system_admin_data()))

print("\n-- Mentee Data")
print(format_sql_inserts("mentee", generate_mentee_data()))

print("\n-- Mentor Data")
print(format_sql_inserts("mentor", generate_mentor_data()))

print("\n-- Learning Path Data")
print(format_sql_inserts("learning_path", generate_learning_path_data()))

print("\n-- Progress Data")
print(format_sql_inserts("progress", generate_progress_data()))

print("\n-- Issue Report Data")
print(format_sql_inserts("issue_report", generate_issue_report_data()))

print("\n-- Content Updates Data")
print(format_sql_inserts("content_updates", generate_content_update_data()))

print("\n-- Session Data")
print(format_sql_inserts("session", generate_session_data()))

print("\n-- Feedback Data")
print(format_sql_inserts("feedback", generate_feedback_data()))

print("\n-- Scenario Practice Data")
print(format_sql_inserts("scenario_practice", generate_scenario_practice_data()))

print("\n-- Vocabulary Practice Data")
print(format_sql_inserts("vocab_practice", generate_vocab_practice_data()))
