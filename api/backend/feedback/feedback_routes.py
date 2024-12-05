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
    This route is used by mentors/mentees retrieve feedback from each other.
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

#------------------------------------------------------------
# Add feedback from a mentee or mentor
@feedbacks.route('/feedback', methods=['POST'])
def add_feedback(session_id, feedback):
    """
    This route is used by mentors/mentees to leave feedback for each other.
    """


    query = f'''insert into feedback (session_id, feedback)
                values ({str(session_id)}, {str(feedback)})
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Feedback added successfully"}))
    response.status_code = 200
    return response
