from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# progress blueprint
# Contains: 
progress = Blueprint('progress', __name__)

#------------------------------------------------------------
# Retrieve mentee progress data over time
@progress.route('/progress/<mentee_id>', methods=['GET'])
def get_progress(mentee_id):
    """
    This route is used by mentors to retrieve progress data for a mentee.
    """

    query = f'''select *
                from progress
                where mentee_id = {str(mentee_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Update progress status and completion date
@progress.route('/progress/<progress_id>', methods=['PUT'])
def update_progress(progress_id, progress_status, completion_date):
    """
    This route is used by mentors to update progress data for a mentee.
    """

    query = f'''update progress
                set progress_status = {str(progress_status)},
                    completion_date = {str(completion_date)}
                where progress_id = {str(progress_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Progress updated successfully!!"}))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Delete progress record
@progress.route('/progress/<progress_id>', methods=['DELETE'])
def delete_progress(progress_id):
    """
    This route is used by mentors to delete progress data for a mentee.
    """

    query = f'''delete from progress
                where progress_id = {str(progress_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Progress deleted successfully!!"}))
    response.status_code = 200
    return response

@progress.route('/progress_data')
def get_progress_data():

    query = '''
    SELECT lp.module_name, p.status, p.completion_date
    FROM progress p
    JOIN learning_path lp ON p.path_id = lp.id
    WHERE p.completion_date IS NOT NULL
    ORDER BY p.completion_date ASC;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    return response