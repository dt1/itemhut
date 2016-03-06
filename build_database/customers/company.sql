-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema if not exists company;

create table company.companies (
       company_id serial primary key,
       company_uid varchar unique,
       company_name varchar unique not null,
       company_phone varchar,
       company_phone2 varchar,
       company_fax varchar,
       company_email varchar,
       company_street varchar,
       company_state varchar,
       company_zip varchar,
       company_country varchar
);

create table company.branches (
       main_company int,
       branch_company int primary key,
       foreign key (main_company)
               references company.companies (company_id),
       foreign key (branch_company)
               references company.companies (company_id)
);

create table company.contacts (
       contact_id serial primary key,
       contact_name varchar,
       contact_position varchar,
       contact_phone varchar,
       contact_phone2 varchar,
       contact_email varchar
);

create table company.company_contact (
       company_id int,
       contact_id int,
       foreign key (company_id)
               references company.companies (company_id),
       foreign key (contact_id)
               references company.contacts (contact_id)
);
