from flask import Flask

from backend.db_connection import db
from backend.analytics.analytics_routes import analytics
from backend.content.content_routes import contents
from backend.decision_maker.decision_maker_routes import decision_maker
from backend.feedback.feedback_routes import feedbacks
from backend.issue_reports.issue_reports_routes import issue_reports
from backend.mentee.mentee_routes import mentees
from backend.mentor.mentor_routes import mentors
from backend.progress.progress_routes import progress
from backend.sessions.session_routes import sessions
from backend.system_admin.system_admin_routes import sys_admin

import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup 
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT').strip())
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()  # Change this to your DB name

    # Initialize the database object with the settings above. 
    app.logger.info('current_app(): starting the database connection')
    db.init_app(app)


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.logger.info('current_app(): registering blueprints with Flask app object.')   
    app.register_blueprint(analytics,   url_prefix='/a')
    app.register_blueprint(contents,   url_prefix='/c')
    app.register_blueprint(decision_maker,    url_prefix='/dm')
    app.register_blueprint(feedbacks,   url_prefix='/f')
    app.register_blueprint(issue_reports,   url_prefix='/ir')
    app.register_blueprint(mentees,   url_prefix='/me')
    app.register_blueprint(mentors,   url_prefix='/mo')
    app.register_blueprint(progress,   url_prefix='/p')
    app.register_blueprint(sessions,   url_prefix='/s')
    app.register_blueprint(sys_admin,   url_prefix='/sys')

    # Don't forget to return the app object
    return app

