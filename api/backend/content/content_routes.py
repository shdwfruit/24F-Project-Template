from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# content blueprint
# Contains: 
contents = Blueprint('content', __name__)

#------------------------------------------------------------

@contents.route('/content_updates', methods=['GET'])
def get_content_updates():

    query = '''
                SELECT id, path_id, updated_by, timestamp, description 
                FROM content_updates;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@contents.route('/update_content', methods=['POST'])
def update_contents():

    data = request.json
    current_app.logger.info(data)

    #extracting the variable
    path_id = data['path_id']
    updated_by = data['updated_by']
    description = data['description']

    query = '''
                INSERT INTO content_updates (path_id, updated_by, description)
                VALUES
                (%s, %s, %s);
        '''
    
    cursor = db.get_db().cursor()
    data = (path_id, updated_by, description)
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Content updated added successfully!"}))
    response.status_code = 200
    return response

@contents.route('/delete/<int:id>', methods=['DELETE'])
def delete_report(id):

    query = ''' 
                DELETE FROM content_updates 
                WHERE id = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, id)
    db.get_db().commit()

    if cursor.rowcount > 0:
        response = make_response(jsonify({"message": "Content ID: {id} successfully deleted!"}))
        response.status_code = 200
    else: 
        response = make_response(jsonify({"error": "Invalid Content ID was entered."}), 400)

    return response

@contents.route('/get_vocab', methods=['GET'])
def get_vocab():

    query = '''
                SELECT difficulty_level, context
                FROM vocab_practice
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@contents.route('/get_scenarios', methods=['GET'])
def get_scenarios():

    query = '''
                SELECT description, difficulty_level
                FROM scenario_practice
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response