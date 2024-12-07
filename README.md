
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


Personas and Application Features

Mentees (Emma): Students of Northeastern preparing for the various international experiential learning opportunities provided, such as Dialogues of Civilizations, International Co-ops and study abroad experiences. To ensure these students have a compelling and successful experiential learning experience abroad, they joined NU GlobalConnect to participate in modules and workshops, and more importantly provide them to engage with a mentor who has been in a similar experience before,  which enable them to have greater cultural awareness during their time abroad, which further gives them the opportunity to explore further opportunities, interpret their surroundings and more. 

    Key Functions: 
    1. Find a mentor: Mentees can search for appropriate mentors, which have the skillset and the past experiences who can advise them further on their journey. For example a mentee who is pursuing a Spring Co-op in Japan may look for a mentor who has previously done a Co-op in Japan and can teach him almost everything from what weather may the mentee expect to what is the right business etiquettes to follow in the Japanese work environment. 
    2. View my Sessions: Mentees can register for a new session with their associated mentor and also view upcoming sessions for easy access and efficient management. 
    3. View my learning path: The mentees can further view their learning path, where they can see which modules they are currently enrolled in, and can further report an issue which would be sent to the system administrator to be solved.

2. Mentor (Alejandro): Mentors are essentially student-volunteers at Northeastern who wish to provide their guidance based on their international experiences through Northeastern’s comprehensive set of international experiences that offer a unique opportunity to experientially learn. An example of a mentor would be a sophomore who spent his freshman year in London as a London Scholar guiding an incoming London scholar. The sophomore can further guide the freshman on what kind of opportunities and environment the freshman can experience during his time in London. A key difference in London’s academic system is that they do not have weekly or bi-weekly assignments, grades are typically dependent on a project and a final exam. The mentor can guide their mentees on how to navigate through a new and unique academic system, allowing them to excel during their time in London. 

    Key Features
    1. Find a mentee: Mentors can look for mentees, who they can effectively guide so that the mentees can maximize their international experiential learning experience. 
    2. View My Sessions: Mentors can further view and manage their sessions. This page also allows them to view the immediate feedback they provided to the mentees, which can act as a quick reminder of what stage their mentees are, or what work is still required.
    3. View Mentee’s Learning Path: A unique feature NU GlobalConnect implements is allowing Mentor’s to view the Mentee’s learning path. This enables them to understand the student’s aim, workload and more. 

3. System Administrator (Priya): Software Engineer at Northeastern who manages the platform to ensure that its running smoothly, and handle any key issues and also access key analytics. 

	Key Features: 
    1. Manage Content Updates: The system administrator can manage the contents part of the modules to ensure that the content being delivered by the NU GLobal Connect system towards the Mentors and Mentees is appropriate and accurate in nature. 
    2. View Reported Issues: As a system administrator, the software engineer can access, resolve and delete the reported issues by mentees and mentors using NU GlobalConnect.  Furthermore, they can also report issues that can be seen by other administrators to resolve. 

4. Decision Maker (Dr. Smith): In charge of global experiences at Northeastern, the decision maker views key data and analytics part of NU GlobalConnect, allowing them to make data-driven decisions that can improve the international experiences Northeastern provides as part of its wide range of experiential learning opportunities. For instance, in a feedback provided if a student says he would like a module that can teach him about housing abroad or business etiquettes in a different country, the decision maker can implement a new module which allows students to engage in their preferred topics. 

	Key Features: 
Engagement Insights: Here the decision maker can view the number of engaged students for each module to understand the popularity and need for each module. 
Progress Visualizations: Decision makers have the chance to access the progress for a specific mentee through their unique id. 
Feedback Analysis: Decision makers can also see feedback on particular sessions, workshops and modules which allows them to gauge on what needs to be improved and what is currently working well. 
Cultural Competence Trends: Here, the decision maker can view how many completions each module has and the average completion time in days, which allows the decision maker to manage how difficult and reasonable modules are for mentees. 


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
https://drive.google.com/file/d/1MigqumdnJMjeYmH1eF6pVWJv95to5wd8/view?usp=sharing
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





 
