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


# Route: Create a new issue report
@sys_admin.route('/issues/reports', methods=['POST'])
def create_issue_report():
    details = request.json
    reported_by = details.get('reported_by')
    description = details.get('description')

    query = '''
        INSERT INTO issue_report (reported_by, description, status)
        VALUES (%s, %s, 'Open')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (reported_by, description))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Issue report created successfully!'}))
    response.status_code = 201
    return response


# Route: Update issue report status
@sys_admin.route('/issues/reports/<int:report_id>', methods=['PUT'])
def update_issue_status(report_id):
    details = request.json
    new_status = details.get('status')
    resolved_by = details.get('resolved_by')

    query = '''
        UPDATE issue_report
        SET status = %s, resolved_by = %s
        WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_status, resolved_by, report_id))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Issue report updated successfully!'}))
    response.status_code = 200
    return response


# Route: Delete an issue report
@sys_admin.route('/issues/reports/<int:report_id>', methods=['DELETE'])
def delete_issue_report(report_id):
    query = '''
        DELETE FROM issue_report
        WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (report_id,))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Issue report deleted successfully!'}))
    response.status_code = 200
    return response


# Route: Retrieve a list of content updates
@sys_admin.route('/content/updates', methods=['GET'])
def get_content_updates():
    query = '''
        SELECT cu.id, cu.description, cu.timestamp, sa.first_name AS updated_by
        FROM content_updates cu
        JOIN system_administrator sa ON cu.updated_by = sa.id
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# Route: Add a new content update
@sys_admin.route('/content/updates', methods=['POST'])
def create_content_update():
    details = request.json
    path_id = details.get('path_id')
    updated_by = details.get('updated_by')
    description = details.get('description')

    query = '''
        INSERT INTO content_updates (path_id, updated_by, description)
        VALUES (%s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (path_id, updated_by, description))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Content update created successfully!'}))
    response.status_code = 201
    return response


# Route: Modify a content update
@sys_admin.route('/content/updates/<int:update_id>', methods=['PUT'])
def update_content_update(update_id):
    details = request.json
    new_description = details.get('description')

    query = '''
        UPDATE content_updates
        SET description = %s, timestamp = CURRENT_TIMESTAMP
        WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_description, update_id))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Content update modified successfully!'}))
    response.status_code = 200
    return response


# Route: Delete a content update
@sys_admin.route('/content/updates/<int:update_id>', methods=['DELETE'])
def delete_content_update(update_id):
    query = '''
        DELETE FROM content_updates
        WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (update_id,))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Content update deleted successfully!'}))
    response.status_code = 200
    return response
