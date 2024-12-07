# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

Database Files
This folder contains all the SQL scripts needed to set up, manage, and reinitialize the database for this project. It is designed to support a multi-table relational database system for a language learning and mentorship platform. Below, we outline the purpose of the files, how they work, and how to reset and reinitialize the database.

How It Works
The database is designed with a relational structure to handle various aspects of the platform. Core tables include system_administrator, mentor, mentee, and badge, with supporting tables like learning_path, progress, and feedback to track user interactions and learning progress. Relationships between these tables ensure data consistency, such as linking a mentee to their assigned mentor and learning path. Bridge tables like admin_works_on and dm_view_path support many-to-many relationships where necessary.

Foreign key constraints are used extensively to maintain data integrity. For example, deleting a mentor will cascade updates to mentees linked to them, while setting certain fields to NULL ensures minimal disruption when relationships change.

How to Re-Bootstrap
To reset the database, execute the bootstrap.sql script in your MySQL client or terminal. This script will drop any existing database, recreate the schema, and populate it with sample data. If finer control is required, the schema and data scripts can be run separately in sequence (schema.sql first, followed by data.sql). Once executed, verify the setup by checking the tables and data within the global database.

