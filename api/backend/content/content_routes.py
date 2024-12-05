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

    query = '''SELECT id, path_id, updated_by, timestamp, description 
                FROM content_updates;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@contents.route('/update_content', methods=['GET'])