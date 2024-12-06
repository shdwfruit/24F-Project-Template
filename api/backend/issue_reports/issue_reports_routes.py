from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# issue reports blueprint
# Contains: 
issue_reports = Blueprint('issue_reports', __name__)

#------------------------------------------------------------

@issue_reports.route('/get_reports', methods=['GET'])
def fetch_reported_issues():

    query = '''
            SELECT ir.id, ir.description, ir.status, ir.timestamp, 
                    sa.first_name AS resolved_by
            FROM issue_report ir
            LEFT JOIN system_administrator sa ON ir.resolved_by = sa.id
            WHERE ir.status = 'Open';
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response