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