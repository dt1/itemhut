-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

drop schema if exists vendor cascade;

create schema if not exists vendor;

create table vendor.vendors (
       vendor_id varchar primary key,
       vendor_name varchar not null,
       phone varchar,
       fax varchar,
       website varchar,
       email varchar,
       street varchar,
       city varchar,
       state varchar,
       zip varchar,
       country varchar
);

create table vendor.contacts (
       contact_id serial primary key,
       name varchar not null,
       title varchar,
       phone varchar,
       alt_phone varchar,
       email varchar
);

create table vendor.vendor_contact (
       vendor_id varchar,
       contact_id int,
       primary key (vendor_id, contact_id),
       foreign key (vendor_id)
               references vendor.vendors (vendor_id)
	       on update cascade,
       foreign key (contact_id)
               references vendor.contacts (contact_id)
);

create table vendor.vendor_products (
       vendor_id varchar,
       upc bigint primary key,
       foreign key (vendor_id)
               references vendor.vendors (vendor_id)
	       on update cascade,
       foreign key (upc)
               references product.sku_upc (upc)
	       on update cascade
);
