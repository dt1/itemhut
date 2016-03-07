-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

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
       person_name varchar,
       foreign key (user_role)
               references users.valid_user_roles (user_role)
);
