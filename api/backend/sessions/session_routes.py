from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

sessions = Blueprint('sessions', __name__)

@sessions.route('/mentee/<int:mentee_id>', methods=['GET'])
def get_mentee_sessions(mentee_id):
    """Get all sessions for a mentee"""
    query = '''
        SELECT s.id, s.purpose, s.date, s.duration,
               m.first_name, m.last_name, m.email
        FROM session s
        JOIN mentor m ON s.mentor_id = m.id
        WHERE s.mentee_id = %s
        ORDER BY s.date DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (mentee_id,))
    results = cursor.fetchall()
    print(f"Raw results: {results}")  # Debug the raw output
    for row in results:
        print(f"Row content: {row}, Type: {type(row)}")  # Debug print
    
    sessions = []
    for row in results:
        sessions.append({
            "id": row['id'],
            "purpose": row['purpose'],
            "date": row['date'].strftime('%Y-%m-%d'),
            "duration": str(row['duration']),
            "mentor_name": f"{row['first_name']} {row['last_name']}",
            "mentor_email": row['email']
        })
    
    response = make_response(jsonify(sessions))
    response.status_code = 200
    return response

@sessions.route('/mentor/<int:mentor_id>', methods=['GET'])
def get_mentor_sessions(mentor_id):
    """Get all sessions for a mentor"""
    query = '''
        SELECT s.id, s.purpose, s.date, s.duration,
               m.first_name, m.last_name, m.email
        FROM session s
        JOIN mentor m ON s.mentor_id = m.id
        WHERE s.mentor_id = %s
        ORDER BY s.date DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (mentor_id,))
    results = cursor.fetchall()
    print(f"Raw results: {results}")  # Debug the raw output
    for row in results:
        print(f"Row content: {row}, Type: {type(row)}")  # Debug print
    
    sessions = []
    for row in results:
        sessions.append({
            "id": row['id'],
            "purpose": row['purpose'],
            "date": row['date'].strftime('%Y-%m-%d'),
            "duration": str(row['duration']),
            "mentor_name": f"{row['first_name']} {row['last_name']}",
            "mentor_email": row['email']
        })
    
    response = make_response(jsonify(sessions))
    response.status_code = 200
    return response

@sessions.route('/create', methods=['POST'])
def create_session():
    """Create a new session"""
    try:
        details = request.json
        print(f"Received details: {details}")  # Debug print
        
        # Validate and convert IDs to integers
        try:
            mentee_id = int(details['mentee_id'])
            mentor_id = int(details['mentor_id'])
            query = '''
                INSERT INTO session (
                    mentee_id,
                    mentor_id,
                    purpose,
                    date,
                    duration
                ) VALUES (%s, %s, %s, %s, %s)
            '''
        
            cursor = db.get_db().cursor()
            cursor.execute(query, (
                mentee_id,  # Using converted integer
                mentor_id,  # Using converted integer
                details['purpose'],
                details['date'],
                details['duration']
            ))
        
            db.get_db().commit()
        
            response = make_response(jsonify({"message": "Session created successfully!"}))
            response.status_code = 200
            return response
        
        except (ValueError, TypeError) as e:
            print(f"ID conversion error: {str(e)}")  # Debug print
            response = make_response(jsonify({
                "error": "Invalid ID format. Mentee ID and Mentor ID must be numbers."
            })) 
            response.status_code = 400
            return response
        
    except Exception as e:
        db.get_db().rollback()
        print(f"Error in create_session: {str(e)}")  # Debug print
        response = make_response(jsonify({"error": str(e)}))
        response.status_code = 500
        return response