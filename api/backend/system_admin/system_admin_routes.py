from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

#------------------------------------------------------------
# system administrator blueprint
# Contains routes for system administrator functionalities
sys_admin = Blueprint('system_admin', __name__)
