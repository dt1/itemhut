-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

drop schema orders cascade;
create schema if not exists orders;

create table orders.msku_sku (
       marketplace_sku varchar primary key,
       sku varchar not null,
       marketplace varchar not null,
       foreign key (sku)
               references product.sku_upc (sku)
	       on update cascade,
       foreign key (marketplace)
               references marketplace.valid_markeplace
	       (marketplace)
	       on update cascade
);

create table orders.market_orders (
       market_order_id varchar primary key,
       marketplace varchar not null default 'main',
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
       market_order_id varchar primary key,
       company_id int,
       company_contact_id int,
       foreign key (company_id, company_contact_id)
               references company.company_contact
	       (company_id, contact_id)
);

create table orders.market_order_skus (
       market_order_id varchar,
       marketplace_sku varchar not null,
       primary key (market_order_id, marketplace_sku),
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
	       on update cascade,
       foreign key (marketplace_sku)
               references orders.msku_sku (marketplace_sku)
);

create table orders.price_per_piece (
       market_order_id varchar,
       marketplace_sku varchar not null,
       price_per_piece numeric check(price_per_piece > 0),
       qty int check(qty > 0),
       primary key(market_order_id, marketplace_sku,
       	           price_per_piece),
       foreign key (market_order_id, marketplace_sku)
               references orders.market_order_skus
	       (market_order_id, marketplace_sku)
);

create table orders.shipto (
       market_order_id varchar,
       marketplace_sku varchar,
       sku_qty int check(sku_qty > 0),
       shipto_company varchar,
       shipto_attn varchar,
       shipto_street varchar,
       shipto_city varchar,
       shipto_state varchar,
       shipto_zip varchar,
       shipto_country varchar,
       foreign key (market_order_id, marketplace_sku)
               references orders.market_order_skus
	       (market_order_id, marketplace_sku)
);

create table orders.valid_file_type (
       file_type varchar primary key
);

insert into orders.valid_file_type (file_type)
values ('Purchase Order'),
('Invoice'),
('B&W Proof'),
('Color Proof');

create table orders.files (
       market_order_id varchar,
       file_path varchar,
       file_type varchar,
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
);
