from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

#------------------------------------------------------------
# decision maker blueprint
# Contains routes for decision maker functionalities
decision_maker = Blueprint('decision_maker', __name__)
