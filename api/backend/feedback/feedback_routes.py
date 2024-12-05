from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# feedback blueprint
# Contains: 
feedbacks = Blueprint('feedback', __name__)

#------------------------------------------------------------
# Get feedback from mentors or mentees for sessions
@feedbacks.route('/feedback', methods=['GET'])