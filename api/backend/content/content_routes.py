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

    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    path_id = the_data['path_id']
    updated_by = the_data['updated_by']
    description = the_data['description']

    query = f'''
                INSERT INTO content_updates (path_id, updated_by, description)
                VALUES
                ({str(path_id)}, {str(updated_by)}, {description});
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Content updated added successfully!"}))
    response.status_code = 200
    return response


