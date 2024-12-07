from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# mentee blueprint
mentees = Blueprint('mentee', __name__)

#------------------------------------------------------------
# mentee routes

@mentees.route('/mentors', methods=['GET'])
def get_mentors():
    """
    This route is used by mentees to find mentors based on 
    teaching language and language level.
    """
    teaching_lang = request.args.get('teaching_language')
    lang_level = request.args.get('language_level')

    query = '''
        SELECT id, first_name, last_name, email, 
               teaching_language, language_level
        FROM mentor
        WHERE teaching_language = %s 
        AND language_level = %s
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (teaching_lang, lang_level))
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@mentees.route('/create', methods=['POST'])
def create_mentee():
    """
    Create a new mentee with a fixed admin (Donald Campbell, id=1)
    """
    try:
        cursor = db.get_db().cursor()
        details = request.json
        mentor_id = details[mentor_id]
        first_name = details[first_name]
        last_name = details[last_name]
        email = details[email]
        learning_language = details[learning_language]
        language_level = details[language_level]
        data = (mentor_id, admin_id, first_name, last_name, 
                email, learning_language, language_level)
        
        # Use fixed admin_id = 1 (Donald Campbell)
        admin_id = 1
        
        # Insert new mentee
        insert_query = '''
            INSERT INTO mentee (
                mentor_id, 
                admin_id, 
                first_name, 
                last_name, 
                email, 
                learning_language, 
                language_level
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''

        cursor.execute(insert_query, data)
        db.get_db().commit()
        
        response = make_response(jsonify({"message": "Mentee successfully registered!"}))
        response.status_code = 200
        return response
        
    except Exception as e:
        db.get_db().rollback()
        print(f"Error in create_mentee: {str(e)}")  # Debug print
        response = make_response(jsonify({"error": str(e)}))
        response.status_code = 500
        return response
    
@mentees.route('/verify', methods=['POST'])
def verify_mentee():
    """Verify mentee by email and return their info"""
    print("Received verify request")  # Debug print
    email = request.json.get('email')
    print(f"Email received: {email}")  # Debug print
    
    query = '''
        SELECT id, first_name, last_name, email, mentor_id
        FROM mentee
        WHERE email = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    print(f"Database result: {result}")  # Debug print
    
    if result:
        # Convert result to dictionary with descriptive keys
        columns = ['id', 'first_name', 'last_name', 'email', 'mentor_id']
        response_data = dict(zip(columns, result))
        print(f"Sending response: {response_data}")  # Debug print
        response = make_response(jsonify(response_data))
        response.status_code = 200
    else:
        response = make_response(jsonify({"error": "Mentee not found"}))
        response.status_code = 404  # Changed to 404 for "not found"
    
    return response

@mentees.route('/get_id', methods=['GET'])
def get_mentee_id():

    email = request.json()

    query = '''
        SELECT id
        FROM mentee
        WHERE email = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (email,))
    data = cursor.fetchall()
    if data:
        response = make_response(jsonify(data))
        response.status_code = 200
    else:
        response = make_response(jsonify({"error": "Mentee not found"}))
        response.status_code = 404  # Changed to 404 for "not found"
    return response

@mentees.route('/get_mentor_id/<int:id>', methods=['GET'])
def get_mentor_with_mentee_id(id):

    query = f'''
                SELECT mentor_id
                FROM mentee
                WHERE mentee_id = {id};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response