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
    # Get query parameters
    teaching_lang = request.args.get('teaching_language')
    lang_level = request.args.get('language_level')

    query = '''
        SELECT first_name, last_name, email, 
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