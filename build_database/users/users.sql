create schema users;

create table users.valid_user_roles (
       user_role varchar primary key
);

insert into users.valid_user_roles (user_role)
values ('user'), ('admin');

create table users.users (
       user_name varchar primary key,
       password varchar,
       user_role varchar,
       foreign key (user_role)
               references users.valid_user_roles (user_role)
);
