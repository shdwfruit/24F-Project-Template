
NU Global Connect - CS 3200 Fall 2024 Project

This repository contains the project NU Global Connect, a data-driven application designed to help Northeastern students prepare for international internships and co-ops by enhancing cultural awareness and adaptability.
Project Overview

NU Global Connect is a data-driven application designed to prepare Northeastern students for international internships and co-ops by fostering cultural awareness and adaptability. With Northeastern’s expanding global footprint—including 13 campuses across the U.S., U.K., and Canada, and over 70 Dialogue of Civilizations programs worldwide—students frequently engage in diverse cultural environments. However, many lack the structured resources needed to navigate new workplace cultures and communicate effectively in intercultural settings.
This app bridges that gap by providing a comprehensive, personalized, and interactive approach to cultural preparedness. Leveraging student progress and engagement data, NU Global Connect adapts its content to ensure relevance and impact. It addresses critical pain points, such as limited access to tailored cultural training and language practice tools specific to a student’s target country.

Through features like interactive cultural etiquette modules, AI-driven language practice, and a progress-tracking dashboard, students gain practical skills in intercultural communication. The platform empowers them to transition seamlessly into international settings with confidence and competence.

NU Global Connect caters to diverse user personas, including students, language mentors, system administrators, and decision-makers. Tailored features like culture-specific training, personalized language matching, and competency tracking align with Northeastern’s commitment to global experiential learning, ensuring smooth and successful student transitions across regions.

Team Members
Yu-Hsiang Huang (Point Person) - huang.yu-h@northeastern.edu
Rick Xie - xie.ri@northeastern.edu
Arnav Mehta - mehta.arn@northeastern.edu
Honglin Chen - chen.hongli@northeastern.edu
Damanbir Anand - anand.da@northeastern.edu


Project Components
The project is divided into three main components, each running in a separate Docker container:
-Streamlit Application (./app) - Front-end interface for users.
-Flask REST API (./api) - Back-end services for handling business logic and database interactions.
-MySQL Database (./database-files) - Storage for all application data, including users, sessions, feedback, and analytics.


Prerequisites
Ensure you have the following installed:
-Docker and Docker Compose
-Python (minimum version 3.9)
-Git client 

Project Setup
Follow these steps to set up and run the project locally:
Clone the repository:
bash
Copy code
git clone https://github.com/<your-team-repo>.git
cd <your-team-repo>


Navigate to the api/ folder and create a .env file based on .env.template:
bash
Copy code
cp api/.env.template api/.env
Update the .env file with the necessary database credentials.
Start all services using Docker Compose:
bash
Copy code
docker compose up -d


Access the application:

Streamlit App: http://localhost:8501
Flask API: http://localhost:5000
Features and Functionality


Application Features

User Personas description:

Mentees: Students preparing for global experiences can access cultural learning paths, vocabulary practice, and mentor sessions.

Mentors: Experienced peers who guide mentees in language and cultural preparation.
System Administrators: Maintain the app and monitor performance, content updates, and bug reports.

Decision Makers: Analyze progress data and refine cultural modules to improve outcomes.

Persona functions - 

Emma (Mentee):
- Search for mentors.
- Access scenario practice and vocabulary modules.
- Track the learning progress with feedback.

Alejandro (Mentor):
- Match with mentees.
- Provide feedback and track mentee progress.
- Get recognition for mentoring hours.

Priya (System Administrator):
- Manage the content updates.
- Monitor and resolve issue reports.
- View engagement analytics.

Dr. Smith (Decision Maker):
- Analyze student engagement and module performance.
- Receive feedback to improve the curriculum.
- Generate insightful reports on student progress.



REST API
The REST API is organized into Blueprints based on personas:
Mentors: Fetch and manage mentor-related data.
Sessions: Handle scheduling, updates, and cancellations.
Feedback: Manage session feedback.
Analytics: Provide insights into engagement and progress.
Refer to the api/ folder for the complete API documentation.


Streamlit Front-End
The application includes the following pages:
Landing Page: Role selection for mentees, mentors, administrators, and decision-makers.
Feature Pages: Custom functionality for each persona, including:
Session scheduling and management
Interactive cultural scenarios
Analytics dashboards


Sample Data
Mockaroo-generated sample data is included in the database-files/ folder. It contains:
30-40 rows for strong entities (e.g., mentors, mentees).
40-50 rows for weak entities.
100+ rows for bridge tables (e.g., sessions, progress).
Controlling the Containers
Use the following commands to manage Docker containers:
Start all services: docker compose up -d
Stop services: docker compose stop
Restart specific containers (e.g., database): docker compose up db -d
Shut down and remove containers: docker compose down



Demo Video
Project Demo Video
https://drive.google.com/drive/folders/1vmEUh4RKqtVfES-Y3iJpvTwH0yeDs6aN?usp=sharing
The video includes:
A brief introduction to the project and team.
Overview of the REST API and implemented routes.
A demo of the Streamlit front-end and interaction with the database.

Additional Video on possible user interview
https://www.youtube.com/shorts/9mEPp0gXgt8

-----------------------------------------------------------------------

# Fall 2024 CS 3200 Project Template Repository

This repo is a template for your semester project.  It includes most of the infrastructure setup (containers) and sample code and data throughout.  Explore it fully and ask questions.

## Prerequisites

- A GitHub Account
- A terminal-based or GUI git client
- VSCode with the Python Plugin
- A distrobution of Python running on your laptop (Choco (for Windows), brew (for Macs), miniconda, Anaconda, etc). 

## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory

## Suggestion for Learning the Project Code Base

If you are not familiar with web app development, this code base might be confusing. You will probably want two versions though:
1. One version for you to explore, try things, break things, etc. We'll call this your **Personal Repo** 
1. One version of the repo that your team will share.  We'll call this the **Team Repo**. 


### Setting Up Your Personal Repo

1. In GitHub, click the **fork** button in the upper right corner of the repo screen. 
1. When prompted, give the new repo a unique name, perhaps including your last name and the word 'personal'. 
1. Once the fork has been created, clone YOUR forked version of the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. Start the docker containers. 

### Setting Up Your Team Repo 

Before you start: As a team, one person needs to assume the role of *Team Project Repo Owner*. 

1. The Team Project Repo Owner needs to fork this template repo into their own GitHub account **and give the repo a name consistent with your project's name**.  If you're worried that the repo is public, don't.  Every team is doing a different project. 
1. In the newly forked team repo, the Team Project Repo Owner should go to the **Settings** tab, choose **Collaborators and Teams** on the left-side panel. Add each of your team members to the repository with Write access. 
1. Each of the other team members will receive an invitation to join.  Obviously accept the invite. 
1. Once that process is complete, each team member, including the repo owner, should clone the Team's Repo to their local machines (in a different location than your Personal Project Repo).  

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 


## Handling User Role Access and Control

In most applications, when a user logs in, they assume a particular role.  For instance, when one logs in to a stock price prediction app, they may be a single investor, a portfolio manager, or a corporate executive (of a publicly traded company).  Each of those *roles* will likely present some similar features as well as some different features when compared to the other roles. So, how do you accomplish this in Streamlit?  This is sometimes called Role-based Access Control, or **RBAC** for short. 

The code in this project demonstrates how to implement a simple RBAC system in Streamlit but without actually using user authentication (usernames and passwords).  The Streamlit pages from the original template repo are split up among 3 roles - Political Strategist, USAID Worker, and a System Administrator role (this is used for any sort of system tasks such as re-training ML model, etc.). It also demonstrates how to deploy an ML model. 

Wrapping your head around this will take a little time and exploration of this code base.  Some highlights are below. 

### Getting Started with the RBAC 
1. We need to turn off the standard panel of links on the left side of the Streamlit app. This is done through the `app/src/.streamlit/config.toml` file.  So check that out. We are turning it off so we can control directly what links are shown. 
1. Then I created a new python module in `app/src/modules/nav.py`.  When you look at the file, you will se that there are functions for basically each page of the application. The `st.sidebar.page_link(...)` adds a single link to the sidebar. We have a separate function for each page so that we can organize the links/pages by role. 
1. Next, check out the `app/src/Home.py` file. Notice that there are 3 buttons added to the page and when one is clicked, it redirects via `st.switch_page(...)` to that Roles Home page in `app/src/pages`.  But before the redirect, I set a few different variables in the Streamlit `session_state` object to track role, first name of the user, and that the user is now authenticated.  
1. Notice near the top of `app/src/Home.py` and all other pages, there is a call to `SideBarLinks(...)` from the `app/src/nav.py` module.  This is the function that will use the role set in `session_state` to determine what links to show the user in the sidebar. 
1. The pages are organized by Role.  Pages that start with a `0` are related to the *Political Strategist* role.  Pages that start with a `1` are related to the *USAID worker* role.  And, pages that start with a `2` are related to The *System Administrator* role. 


## Deploying An ML Model (Totally Optional for CS3200 Project)

*Note*: This project only contains the infrastructure for a hypothetical ML model. 

1. Build, train, and test your ML model in a Jupyter Notebook. 
1. Once you're happy with the model's performance, convert your Jupyter Notebook code for the ML model to a pure python script.  You can include the `training` and `testing` functionality as well as the `prediction` functionality.  You may or may not need to include data cleaning, though. 
1. Check out the  `api/backend/ml_models` module.  In this folder, I've put a sample (read *fake*) ML model in `model01.py`.  The `predict` function will be called by the Flask REST API to perform '*real-time*' prediction based on model parameter values that are stored in the database.  **Important**: you would never want to hard code the model parameter weights directly in the prediction function.  tl;dr - take some time to look over the code in `model01.py`.  
1. The prediction route for the REST API is in `api/backend/customers/customer_routes.py`. Basically, it accepts two URL parameters and passes them to the `prediction` function in the `ml_models` module. The `prediction` route/function packages up the value(s) it receives from the model's `predict` function and send its back to Streamlit as JSON. 
1. Back in streamlit, check out `app/src/pages/11_Prediction.py`.  Here, I create two numeric input fields.  When the button is pressed, it makes a request to the REST API URL `/c/prediction/.../...` function and passes the values from the two inputs as URL parameters.  It gets back the results from the route and displays them. Nothing fancy here. 





 
