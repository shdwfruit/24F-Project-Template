from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# mentor blueprint
# Contains: 
mentors = Blueprint('mentor', __name__)


#------------------------------------------------------------
# mentor routes
# Get mentors by language level, location, and teaching language
@mentors.route('/get_mentees', methods=['GET'])
def get_mentees():
    """
    This route is used by mentor to find mentees.
    """
    # Get query parameters
    learning_lang = request.args.get('learning_language')
    lang_level = request.args.get('language_level')

    query = '''
        SELECT first_name, last_name, email, 
               learning_language, language_level
        FROM mentee
        WHERE learning_language = %s 
        AND language_level = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (learning_lang, lang_level))
    theData = cursor.fetchall()

    

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
   


