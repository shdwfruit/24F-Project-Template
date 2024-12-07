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
        data = request.json
        mentor_id = data['mentor_id']
        admin_id = 1 # Use fixed admin_id = 1 (Donald Campbell)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        learning_language = data['learning_language']
        language_level = data['language_level']
        query_data = (mentor_id, admin_id, first_name, last_name, 
                email, learning_language, language_level)
        
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

        cursor.execute(insert_query, query_data)
        db.get_db().commit()
        
        # Return a 201 status to indicate resource creation
        response = make_response(jsonify({"message": "Mentee successfully registered!"}))
        response.status_code = 201
        return response

    except Exception as e:
        db.get_db().rollback()
        print(f"Error in create_mentee: {str(e)}")
        response = make_response(jsonify({"error": str(e)}))
        response.status_code = 500
        return response

    
@mentees.route('/verify', methods=['GET'])
def verify_mentee():
    """Verify mentee by email and return their info"""
    print("Received verify request")  # Debug print
    email = request.args.get('email')
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
        response = make_response(jsonify(result))
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

    query = '''
                SELECT mentor_id
                FROM mentee
                WHERE mentee_id = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    theData = cursor.fetchone()
    print(f"debug print: {theData}")  # Debug print

    if theData:
        # Return mentor_id as a JSON object
        response = jsonify(theData)
        response.status_code = 200
    else:
        # Return error if mentee_id is not found
        response = jsonify({"error": "Mentee not found"})
        response.status_code = 404