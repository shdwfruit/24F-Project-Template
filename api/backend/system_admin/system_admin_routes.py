from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

#------------------------------------------------------------
# system administrator blueprint
# Contains routes for system administrator functionalities
sys_admin = Blueprint('system_admin', __name__)

#------------------------------------------------------------
# system administrator routes

# Route: View module usage and completion data
@sys_admin.route('/analytics/engagement', methods=['GET'])
def get_module_engagement():
    query = '''
        SELECT path_id, COUNT(*) AS completions
        FROM progress
        WHERE status = 'Completed'
        GROUP BY path_id
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# Route: View reported issues (bugs and feedback)
@sys_admin.route('/issues/reports', methods=['GET'])
def get_reported_issues():
    query = '''
        SELECT ir.id, ir.description, ir.status, sa.first_name AS resolved_by
        FROM issue_report ir
        LEFT JOIN system_administrator sa ON ir.resolved_by = sa.id
        WHERE ir.status = 'Open'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

    return response
