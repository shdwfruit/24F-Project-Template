SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `global` ;
CREATE SCHEMA IF NOT EXISTS `global` DEFAULT CHARACTER SET latin1 ;
USE `global` ;

-- system admin table
create table system_administrator (
    id int auto_increment primary key,
    email varchar(75) unique,
    first_name varchar(30),
    last_name varchar(30),
    role varchar(100)
);

-- badge table
create table badge (
    id int auto_increment primary key,
    title varchar(50),
    criteria text
);

-- mentor table
create table mentor (
    id int auto_increment primary key,
    admin_id int not null,
    badge_id int,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(75) unique,
    teaching_language varchar(50),
    location varChar(100),
    language_level enum('Advanced', 'Fluent'),
    foreign key (admin_id) references system_administrator(id)
        on update cascade
        on delete restrict,
    foreign key (badge_id) references badge(id)
        on update cascade
        on delete set null
);

-- mentee table
create table mentee (
    id int auto_increment primary key,
    mentor_id int not null,
    admin_id int not null,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(75) unique,
    learning_language varchar(50),
    language_level enum('Beginner', 'Intermediate', 'Advanced', 'Fluent'),
    foreign key (mentor_id) references mentor(id)
        on update cascade
        on delete restrict,
    foreign key (admin_id) references system_administrator(id)
        on update cascade
        on delete restrict
);

-- decision maker table
create table decision_maker (
    id int auto_increment primary key,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(75) unique
);

-- issue report table
create table issue_report (
    id int auto_increment primary key,
    reported_by int not null,
    resolved_by int,
    status varchar(50),
    timestamp timestamp default current_timestamp not null,
    description text,
    foreign key (reported_by) references mentee(id)
        on update cascade
        on delete restrict,
    foreign key (resolved_by) references system_administrator(id)
        on update cascade
        on delete restrict
);

-- learning path table
create table learning_path (
    id int auto_increment primary key,
    mentee_id int,
    dm_id int,
    module_name varchar(50),
    description text,
    milestones text,
    last_updated timestamp default current_timestamp on update current_timestamp,
    status varchar(50),
    foreign key (mentee_id) references mentee(id)
        on update cascade
        on delete set null,
    foreign key (dm_id) references decision_maker(id)
        on update cascade
        on delete restrict
);

-- progress table
create table progress (
    id int auto_increment primary key,
    mentee_id int not null,
    path_id int not null,
    status varchar(50),
    completion_date datetime,
    foreign key (mentee_id) references mentee(id)
        on update cascade
        on delete cascade,
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete restrict
);

-- content updates table
create table content_updates (
    id int auto_increment primary key,
    path_id int not null,
    updated_by int not null,
    timestamp timestamp default current_timestamp,
    description text,
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete cascade,
    foreign key (updated_by) references system_administrator(id)
        on update cascade
        on delete restrict
);

-- session table
create table session (
    id int auto_increment primary key,
    mentee_id int not null,
    mentor_id int not null,
    purpose text,
    date date default null,
    duration time default '00:00:00',
    foreign key (mentee_id) references mentee(id)
        on update cascade
        on delete restrict,
    foreign key (mentor_id) references mentor(id)
        on update cascade
        on delete restrict
);

-- feedback table
create table feedback (
    id int auto_increment primary key,
    session_id int not null,
    description text,
    foreign key (session_id) references session(id)
        on update cascade
        on delete cascade
);

-- scenario practice table
create table scenario_practice (
    id int auto_increment primary key,
    path_id int not null,
    description text,
    difficulty_level enum('Beginner', 'Intermediate', 'Advanced', 'Fluent'),
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete restrict
);

-- vocabulary practice table
create table vocab_practice (
    id int auto_increment primary key,
    path_id int not null,
    context text,
    difficulty_level enum('Beginner', 'Intermediate', 'Advanced', 'Fluent'),
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete restrict
);

-- Bridge tables:
-- Works on table between admin and issue report
create table admin_works_on (
    report_id int not null,
    admin_id int not null,
    foreign key (report_id) references issue_report(id)
        on update cascade
        on delete cascade,
    foreign key (admin_id) references system_administrator(id)
        on update cascade
        on delete restrict
);

-- change table between content update and learning path
create table update_to_path (
    update_id int not null,
    path_id int not null,
    foreign key (update_id) references content_updates(id)
        on update cascade
        on delete cascade,
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete cascade
);

-- created by table between admin and content update
create table admin_content_update (
    admin_id int not null,
    update_id int not null,
    foreign key (admin_id) references system_administrator(id)
        on update cascade
        on delete cascade,
    foreign key (update_id) references content_updates(id)
        on update cascade
        on delete cascade
);

-- can view table between decision maker and (feedback and learning path)
create table dm_view_path (
    dm_id int not null,
    feedback_id int not null,
    path_id int not null,
    foreign key (dm_id) references decision_maker(id)
        on update cascade
        on delete restrict,
    foreign key (feedback_id) references feedback(id)
        on update cascade
        on delete cascade,
    foreign key (path_id) references learning_path(id)
        on update cascade
        on delete restrict
);

-- insert data into system_administrator table
insert into system_administrator (email, first_name, last_name, role)
values
('admin1@example.com', 'Alice', 'Smith', 'System Admin'),
('admin2@example.com', 'Bob', 'Jones', 'Content Manager'),
('admin3@example.com', 'Charlie', 'Brown', 'Support Specialist');

-- insert data into badge table
insert into badge (title, criteria)
values
('Language Badge', 'As a non-native speaker, be fluent in a chosen language'),
('Culture Badge', 'As a non-native person, be well-versed in a chosen foreign culture'),
('Jack-of-all-Trades Badge', 'Speak multiple non-native languages');

-- insert data into mentor table
insert into mentor (admin_id, badge_id, first_name, last_name, email, teaching_language, location, language_level)
values
(1, 1, 'John', 'Doe', 'mentor1@example.com', 'English', 'United Kingdom, London', 'Fluent'),
(2, 2, 'Jane', 'Smith', 'mentor2@example.com', 'Spanish', 'Spain, Barcelona', 'Advanced'),
(3, 3, 'Jim', 'Beam', 'mentor3@example.com', 'French', 'France, Paris', 'Fluent');

-- insert data into mentee table
insert into mentee (mentor_id, admin_id, first_name, last_name, email, learning_language, language_level)
values
(1, 1, 'Michael', 'Johnson', 'mentee1@example.com', 'English', 'Beginner'),
(2, 2, 'Sarah', 'Lee', 'mentee2@example.com', 'Spanish', 'Intermediate'),
(3, 3, 'Tom', 'Clark', 'mentee3@example.com', 'French', 'Advanced');

-- insert data into decision_maker table
insert into decision_maker (first_name, last_name, email)
values
('Guy', 'Random', 'dm1@example.com'),
('Mark', 'Fontenot', 'dm2@example.com'),
('Teaching', 'Assistants', 'dm3@example.com');

-- insert data into issue_report table
insert into issue_report (reported_by, resolved_by, status, description)
values
(1, 1, 'Open', 'Issue with login'),
(2, 2, 'Resolved', 'System bug fixed'),
(3, 3, 'Pending', 'New feature request');

-- insert data into learning_path table
insert into learning_path (mentee_id, dm_id, module_name, description, milestones, status)
values
(1, 1, 'Module 1', 'Introductory course', 'Milestone 1, Milestone 2', 'In Progress'),
(2, 2, 'Module 2', 'Intermediate course', 'Milestone A, Milestone B', 'Completed'),
(3, 3, 'Module 3', 'Advanced course', 'Milestone X, Milestone Y', 'Not Started');

-- insert data into progress table
insert into progress (mentee_id, path_id, status, completion_date)
values
(1, 1, 'In Progress', '2024-10-15'),
(2, 2, 'Completed', '2024-10-16'),
(3, 3, 'Not Started', NULL);

-- insert data into content_updates table
insert into content_updates (path_id, updated_by, description)
values
(1, 1, 'Updated milestones'),
(2, 2, 'Added new module content'),
(3, 3, 'Revised objectives');

-- insert data into session table
insert into session (mentee_id, mentor_id, purpose, date, duration)
values
(1, 1, 'Language practice', '2024-11-01', '01:30:00'),
(2, 2, 'Cultural immersion', '2024-11-02', '02:00:00'),
(3, 3, 'Exam preparation', '2024-11-03', '01:45:00');

-- insert data into feedback table
insert into feedback (session_id, description)
values
(1, 'Great progress made'),
(2, 'Needs improvement in grammar'),
(3, 'Excellent comprehension');

-- insert data into scenario_practice table
insert into scenario_practice (path_id, description, difficulty_level)
values
(1, 'Basic conversation scenario', 'Beginner'),
(2, 'Negotiation scenario', 'Intermediate'),
(3, 'Technical presentation', 'Advanced');

-- insert data into vocab_practice table
insert into vocab_practice (path_id, context, difficulty_level)
values
(1, 'Daily activities vocabulary', 'Beginner'),
(2, 'Business vocabulary', 'Intermediate'),
(3, 'Technical terms', 'Advanced');

-- insert data into works_on table
insert into admin_works_on (report_id, admin_id)
values
(1, 1),
(2, 2),
(3, 3);

-- insert data into change table
insert into update_to_path (update_id, path_id)
values
(1, 1),
(2, 2),
(3, 3);

-- insert data into created_by table
insert into admin_content_update (admin_id, update_id)
values
(1, 1),
(2, 2),
(3, 3);

-- insert data into can_view table
insert into dm_view_path (dm_id, feedback_id, path_id)
values
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

-- CRUD statements for each user story in each persona
-- Query for Persona 1: Mentee (Emma)
-- User Story 1: Search for mentors
select *
from mentor
where language_level = 'Intermediate'
  and location like '%Japan%'
  and teaching_language = 'Japanese';

-- User Story 2: Access simulated cultural scenarios and interactive modules
select *
from scenario_practice sp
where sp.path_id = 1
  and sp.difficulty_level = 'Intermediate';

-- User Story 3: Structured learning path with milestones
select lp.module_name, lp.milestones, lp.status
from learning_path lp
where lp.mentee_id = 1;

-- User Story 4: View progress over time with mentor feedback
select p.completion_date, p.status, f.description as feedback
from progress p
left join feedback f on p.id = f.session_id
where p.mentee_id = 1;

-- User Story 5: Access vocabulary and professional phrases
select context, difficulty_level
from vocab_practice
where path_id = 1
  and difficulty_level = 'Intermediate';

-- User Story 6: Request and schedule sessions with mentors
insert into session (mentee_id, mentor_id, purpose, date, duration)
values (1, 1, 'Discuss workplace culture in Japan', '2024-11-21', '01:00:00');

-- Query for Persona 2: Mentor (Alejandro)
-- User Story 1: Matching system for mentees
select *
from mentee
where learning_language = 'Spanish'
  and language_level = 'Intermediate';

-- User Story 2: Access a curriculum library
select *
from learning_path lp
where lp.mentee_id = 2;

-- User Story 3: Track mentoring hours and receive recognition
select mentor_id, count(*) as total_sessions, sum(duration) as total_hours
from session
where mentor_id = 1
group by mentor_id;

-- User Story 4: Monitor mentee progress
select p.status, p.completion_date, lp.module_name
from progress p
join learning_path lp on p.path_id = lp.id
where lp.mentee_id = 2;

-- User Story 5: Document session plans and notes
insert into feedback (session_id, description)
values (2, 'Discussed regional dialect nuances and formalities.');

-- User Story 6: Receive feedback from mentees
select f.description, f.session_id
from feedback f
join session s on f.session_id = s.id
where s.mentor_id = 1;

-- Query for Persona 3: System Administrator (Priya)
-- User Story 1: Access module usage and completion data
select path_id, count(*) as completions
from progress
where status = 'Completed'
group by path_id;

-- User Story 2: Intuitive dashboard navigation
select *
from admin_works_on
where admin_id = 1;

-- User Story 3: Facilitate quick content updates
insert into content_updates (path_id, updated_by, description)
values (1, 1, 'Added updated case study for Japanese culture.');

-- User Story 4: View reported bugs and user feedback
select ir.description, ir.status, sa.first_name as resolved_by
from issue_report ir
left join system_administrator sa on ir.resolved_by = sa.id
where ir.status = 'Open';

-- User Story 5: Remove visual clutter
DELETE
from feedback
where description is null;

-- User Story 6: Automated tools for testing and updates
select path_id, count(*) as total_updates
from content_updates
where timestamp > '2024-11-01'
group by path_id;

-- Query for Persona 4: Decision Maker (Dr. Smith)
-- User Story 1: Insights on student engagement with modules
select lp.module_name, count(p.id) as engaged_students
from learning_path lp
left join progress p on lp.id = p.path_id
group by lp.module_name;

-- User Story 2: Visualization of student progress over time
select mentee_id, status, completion_date
from progress
where path_id = 1;

-- User Story 3: Review and organize student feedback
select f.description, f.session_id
from feedback f
join session s on f.session_id = s.id
where s.date > '2024-11-01';

-- User Story 4: Automated reports on cultural competence trends
select lp.module_name, count(p.id) as completions, avg(p.completion_date) as avg_completion_time
from learning_path lp
join progress p on lp.id = p.path_id
group by lp.module_name;

-- User Story 5: Track completion rates by student demographics
select mentee_id, count(p.id) as total_completions
from progress p
group by mentee_id;

-- User Story 6: Correlations between module performance and success
select lp.module_name, p.status, s.purpose
from learning_path lp
join progress p on lp.id = p.path_id
join session s on p.mentee_id = s.mentee_id;