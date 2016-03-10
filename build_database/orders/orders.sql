-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

drop schema orders cascade;
create schema if not exists orders;

create table orders.market_orders (
       internal_order_id serial primary key,
       market_order_id varchar not null,
       marketplace varchar not null,
       salesperson_id varchar,
       order_date date default now(),
       foreign key (marketplace)
               references marketplace.valid_markeplace
	       (marketplace)
	       on update cascade,
       foreign key (salesperson_id)
               references users.users (user_name)
	       on update cascade
);

create table orders.moi_company (
       internal_order_id int primary key,
       company_id int,
       company_contact_id int,
       foreign key (company_id, company_contact_id)
               references company.company_contact
	       (company_id, contact_id)
);

create table orders.market_order_skus (
       internal_order_id int,
       marketplace_sku varchar not null,
       primary key (internal_order_id, marketplace_sku),
       foreign key (internal_order_id)
               references orders.market_orders (internal_order_id)
	       on update cascade,
       foreign key (marketplace_sku)
               references marketplace.msku_sku (marketplace_sku)
);

create table orders.price_per_piece (
       internal_order_id int,
       marketplace_sku varchar not null,
       price_per_piece numeric check(price_per_piece > 0),
       qty int check(qty > 0),
       primary key(internal_order_id, marketplace_sku,
       	           price_per_piece),
       foreign key (internal_order_id, marketplace_sku)
               references orders.market_order_skus
	       (internal_order_id, marketplace_sku)
);

create table orders.shipto_companies (
       shipto_company_id serial primary key,
       shipto_company varchar,
       shipto_attn varchar,
       shipto_street varchar,
       shipto_city varchar,
       shipto_state varchar,
       shipto_zip varchar,
       shipto_country varchar,
       unique (shipto_company, shipto_attn, shipto_street,
       shipto_city, shipto_state, shipto_zip, shipto_country)
);

create table orders.shipto (
       shipto_id serial primary key,
       internal_order_id int,
       shipto_company_id int,
       ship_by_date date,
       deliver_by_date date,
       foreign key (internal_order_id, marketplace_sku)
               references orders.market_order_skus
	       (internal_order_id, marketplace_sku),
       foreign key (shipto_company_id)
               references orders.shipto_companies (shipto_company_id)
);

create table orders.shipto_marketplace_skus (
       shipto_id int,
       marketplace_sku varchar,
       sku_qty int check(sku_qty > 0),
       primary key (shipto_id, marketplace_sku),
       foreign key (marketplace_sku)
               references marketplace.msku_sku 
               (marketplace_sku)
               on update cascade,
       foreign key (shipto_id)
               references orders.shipto (shipto_id)
);

create table orders.valid_file_type (
       file_type varchar primary key
);

insert into orders.valid_file_type (file_type)
values ('Purchase Order'),
('Invoice'),
('B&W Proof'),
('Color Proof');

create table orders.shipto_files (
       shipto_id int,
       file_path varchar,
       file_type varchar,
       foreign key (shipto_id)
               references orders.shipto(shipto_id)
);


create or replace function orders.insert_shipto_customer
       (n_order_id int, n_shipto_company varchar,
       n_shipto_attn varchar,
       n_shipto_street varchar, n_shipto_city varchar,
       n_shipto_state varchar, n_shipto_zip varchar,
       n_shipto_country varchar, n_ship_by_date date,
       n_deliver_by_date date)
returns void
as
$$
declare
t_company_id int;

begin

insert into orders.shipto_companies (shipto_company,
       shipto_attn, shipto_street, shipto_city, shipto_state,
       shipto_zip, shipto_country)
values (n_shipto_company,
       n_shipto_attn, n_shipto_street, n_shipto_city, n_shipto_state,
       n_shipto_zip, n_shipto_country)
on conflict (shipto_company, shipto_attn, shipto_street,
   shipto_city, shipto_state, shipto_zip,
   shipto_country)
do nothing;

select shipto_company_id
from orders.shipto_companies
where (shipto_company, shipto_attn, shipto_street,
      shipto_city, shipto_state, shipto_zip,
      shipto_country) = (n_shipto_company, n_shipto_attn,
      n_shipto_street,
      n_shipto_city, n_shipto_state, n_shipto_zip,
      n_shipto_country)
into t_company_id;

create temp table tt as
select n_order_id orid, t_company_id comid, n_ship_by_date sdate,
       n_deliver_by_date ddate;

insert into orders.shipto (internal_order_id,
       shipto_company_id,
       ship_by_date, deliver_by_date)
select orid, comid, sdate, ddate
from tt tt
where not exists (
      select *
      from orders.shipto
      where internal_order_id = tt.orid
      and shipto_company_id = tt.comid
      and ship_by_date = tt.sdate
      and deliver_by_date = tt.ddate);

drop table tt;

end;
$$ language plpgsql;
