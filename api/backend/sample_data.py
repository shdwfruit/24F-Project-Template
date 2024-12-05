from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Number of rows to generate
num_rows = 40

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
    for _ in range(10):
        data.append({
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": random.choice(["System Admin", "Content Manager", "Support Specialist"]),
        })
    return data

def generate_mentee_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentor_id": random.randint(1, 10),
            "admin_id": random.randint(1, 10),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "learning_language": random.choice(["Japanese", "Spanish", "Chinese", "French"]),
            "language_level": generate_language_level("mentee"),
        })
    return data

def generate_mentor_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "admin_id": random.randint(1, 10),
            "badge_id": random.randint(1, 10),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "teaching_language": random.choice(["Japanese", "Spanish", "Chinese", "French"]),
            "location": f"{fake.city()}, {fake.country()}",
            "language_level": generate_language_level("mentor"),
        })
    return data

def generate_learning_path_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentee_id": random.randint(1, 40),
            "dm_id": random.randint(1, 10),
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
            "mentee_id": random.randint(1, 40),
            "path_id": random.randint(1, 40),
            "status": generate_status(),
            "completion_date": fake.date_between(start_date='-1y', end_date='today') if random.random() > 0.3 else None,
        })
    return data

def generate_issue_report_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "reported_by": random.randint(1, 40),
            "resolved_by": random.randint(1, 10) if random.random() > 0.5 else None,
            "status": generate_status(),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_content_update_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, 40),
            "updated_by": random.randint(1, 10),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_session_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "mentee_id": random.randint(1, 40),
            "mentor_id": random.randint(1, 40),
            "purpose": fake.text(max_nb_chars=50),
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "duration": f"{random.randint(0, 3):02}:{random.randint(0, 59):02}:00",
        })
    return data

def generate_feedback_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "session_id": random.randint(1, 40),
            "description": fake.text(max_nb_chars=100),
        })
    return data

def generate_scenario_practice_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, 40),
            "description": fake.text(max_nb_chars=50),
            "difficulty_level": generate_difficulty(),
        })
    return data

def generate_vocab_practice_data():
    data = []
    for _ in range(num_rows):
        data.append({
            "path_id": random.randint(1, 40),
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
print("\n-- Vocabulary Practice Data")
print(format_sql_inserts("vocab_practice", generate_vocab_practice_data()))
