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