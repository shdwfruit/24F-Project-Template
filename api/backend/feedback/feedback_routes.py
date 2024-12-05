from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# feedback blueprint
# Contains: 
feedbacks = Blueprint('feedback', __name__)

#------------------------------------------------------------
# Get feedback from mentors or mentees for sessions
@feedbacks.route('/feedback', methods=['GET'])
def get_feedback(session_id):
    """
    This route is used by mentors and mentees to leave feedback for each other.
    """

    query = f'''select *
                from feedback
                where session_id = {str(session_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response