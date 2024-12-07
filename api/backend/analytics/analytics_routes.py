from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# analytics blueprint
# Contains: 
analytics = Blueprint('analytics', __name__)

#------------------------------------------------------------
# Routes for getting engagement data for each module
@analytics.route('/engagement_data', methods=['GET'])
def get_engagement_data():

    query = ''' SELECT lp.module_name, 
                COUNT(p.id) AS engaged_students,
                SUM(p.status = 'Completed') AS completed_students
                FROM learning_path lp
                LEFT JOIN progress p ON lp.id = p.path_id
                GROUP BY lp.module_name;
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

