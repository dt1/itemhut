-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema marketplace;

create table marketplace.valid_markeplace (
       marketplace varchar primary key
);

insert into marketplace.valid_markeplace
       (marketplace)
values ('SAGE'),
('ASI'),
('direct');
