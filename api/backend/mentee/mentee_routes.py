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
        
        cursor.execute(insert_query, (
            details['mentor_id'],
            admin_id,
            details['first_name'],
            details['last_name'],
            details['email'],
            details['learning_language'],
            details['language_level']
        ))
        
        db.get_db().commit()
        
        response = make_response(jsonify({"message": "Mentee successfully registered!"}))
        response.status_code = 201
        return response
        
    except Exception as e:
        db.get_db().rollback()
        print(f"Error in create_mentee: {str(e)}")  # Debug print
        response = make_response(jsonify({"error": str(e)}))
        response.status_code = 500
        return response