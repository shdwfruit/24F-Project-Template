from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# learning path blueprint
# Contains: 
learning_paths = Blueprint('learning_paths', __name__)

#------------------------------------------------------------
# Routes for learning paths
@learning_paths.route('/mentee/<int:mentee_id>', methods=['GET'])
def get_learning_path(mentee_id):
    """
    This route is used by mentors to get the learning path 
    of a specific mentee.
    """
    query = '''
        SELECT module_name, description, milestones, status, completion_date
        FROM learning_path
        WHERE mentee_id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (mentee_id,))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response




