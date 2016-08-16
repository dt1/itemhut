-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema users;

create table users.valid_user_roles (
       user_role varchar primary key
);

insert into users.valid_user_roles (user_role)
values ('user'),
('admin'),
('products'),
('incoming'),
('warehouses'),
('vendors'),
('orders'),
('customers'),
('original admin');

create table users.valid_user_types (
       user_type varchar primary key
);

insert into users.valid_user_types (user_type)
values ('sales');

create table users.users (
       user_name varchar primary key,
       password varchar,
       person_name varchar,
       user_type varchar,
       user_role varchar,
       foreign key (user_role)
               references users.valid_user_roles (user_role),
       foreign key (user_type)
               references users.valid_user_types (user_type)
);

create or replace function users.update_user
       (n_orig_username varchar, n_username varchar,
       n_real_name varchar,
       n_user_type varchar, n_user_role varchar)
returns void
as
$$
declare
t_user_role varchar := (select user_role
	                from users.users
			where user_name = trim(n_orig_username));

begin
if t_user_role = 'original admin'
   then
   update users.users
   set user_name = trim(n_username),
   person_name = trim(n_real_name),
   user_type = trim(n_user_type)
   where user_name = trim(n_orig_username);
else
   update users.users
   set user_name = trim(n_username),
   person_name = trim(n_real_name),
   user_type = trim(n_user_type),
   user_role = trim(n_user_role)
   where user_name = trim(n_orig_username);
end if;

end;
$$ language plpgsql;
