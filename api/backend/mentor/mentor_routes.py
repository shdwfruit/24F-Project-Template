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
@mentors.route('/mentors', methods=['GET'])
def get_mentors(lang, lang_lvl, location):
    """
    This route is used by mentee to find mentors.
    """

    query = f'''select *
                from mentor
                where language_level = {str(lang_lvl)}
                    and location = {str(location)}
                    and teaching_language = {str(lang)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

