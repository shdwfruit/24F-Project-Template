from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# session blueprint
# Contains: 
sessions = Blueprint('session', __name__)

#------------------------------------------------------------
# Get sessions for mentors and mentees
@sessions.route('/sessions/<int:user_id>', methods=['GET'])
def get_sessions(user_id):
    """
    This route is used by mentors/mentees to retrieve their sessions.
    """

    query = f'''select *
                from session
                where mentor_id = {str(user_id)}
                    or mentee_id = {str(user_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Create a new session
@sessions.route('/sessions', methods=['POST'])
def create_session(mentor_id, mentee_id, session_date, session_time):
    """
    This route is used by mentors/mentees to create a new session.
    """

    query = f'''insert into session (mentor_id, mentee_id, session_date, session_time)
                values ({str(mentor_id)}, {str(mentee_id)}, {str(session_date)}, {str(session_time)})
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Session created successfully!!"}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update session details
@sessions.route('/sessions', methods=['PUT'])
def update_session(session_id, session_date, session_time):
    """
    This route is used by mentors/mentees to update a session.
    """

    query = f'''update session
                set session_date = {str(session_date)},
                    session_time = {str(session_time)}
                where session_id = {str(session_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Session updated successfully!!"}))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Delete a session
@sessions.route('/sessions', methods=['DELETE'])
def delete_session(session_id):
    """
    This route is used by mentors/mentees to delete a session.
    """

    query = f'''delete from session
                where session_id = {str(session_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Session deleted successfully!!"}))
    response.status_code = 200
    return response