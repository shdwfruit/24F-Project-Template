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

@issue_reports.route('/resolve', methods=['PUT'])
def resolve_issue():

    data = request.get_json()

    resolved_by = data.get('resolved_by_admin_id')
    id = data.get('issue_id_to_resolve')

    query = ''' 
                UPDATE issue_report 
                SET status = 'Resolved', resolved_by = %s 
                WHERE id = %s;
    '''

    cursor = db.get_db().cursor()
    data = (resolved_by, id)
    cursor.execute(query, data)
    db.get_db().commit()

    if cursor.rowcount > 0:
        response = make_response(jsonify({"message": "Issue {id} successfully resolved!"}))
        response.status_code = 200
    else: 
        response = make_response(jsonify({"error": "Invalid Admin or Issue ID was entered."}), 400)

    return response

@issue_reports.route('/report_issue', methods=['POST'])
def add_report():

    data = request.json
    current_app.logger.info(data)

    #extracting the variable
    reported_by = data['reported_by']
    resolved_by = data['resolved_by']
    status = data['status']
    description = data['description']



    query = '''
                INSERT INTO issue_reports (reported_by, resolved_by, status, description)
                VALUES
                (%s, %s, %s, %s);
        '''
    
    cursor = db.get_db().cursor()
    data = (reported_by, resolved_by, status, description)
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Report added successfully!"}))
    response.status_code = 200
    return response

@issue_reports.route('/delete/<int:id>', methods=['DELETE'])
def delete_report(id):

    query = ''' 
                DELETE FROM issue_report 
                WHERE id = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, id)
    db.get_db().commit()

    if cursor.rowcount > 0:
        response = make_response(jsonify({"message": "Issue {id} successfully deleted!"}))
        response.status_code = 200
    else: 
        response = make_response(jsonify({"error": "Invalid Issue ID was entered."}), 400)

    return response