-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema if not exists orders;

create table orders.msku_sku (
       marketplace_sku varchar primary key,
       sku varchar,
       foreign key (sku)
               references product.sku_upc (sku)
	       on update cascade
);

create table orders.market_orders (
       market_order_id varchar primary key,
       marketplace varchar not null default 'main',
       company_id int,
       contact_id int,
       order_date date default now(),
       foreign key (marketplace_sku)
               references orders.msku_sku (msku),
       foreign key (company_id)
               references company.companies (company_id)
       foreign key (contact_id)
               references company.contacts (contact_id)
);

create table orders.orders (
       order_id bigserial primary key,
       market_order_id varchar unique,
       salesperson_id varchar not null,
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
	       on update cascade,
       foreign key (salesperson_id)
               references users.users (user_id)
	       on update cascade
);

create table orders.market_order_skus (
       market_order_id varchar,
       marketplace_sku varchar not null,
       primary key (market_order_id, marketplace_sku)
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
	       on update cascade,
       foreign key (marketplace_sku)
               references product.sku_upc (sku)
);

create table orders.price_per_piece (
       market_order_id varchar,
       marketplace_sku varchar not null,
       price_per_piece numeric,
       qty int check(qty > 0),
       primary key(market_order_id, marketplace_sku,
       	           price_per_piece, qty),
       foreign key (market_order_id, marketplace_sku)
               references orders.market_order_skus
	       (market_order_id, marketplace_sku)
);

create table orders.shipto (
       market_order_id varchar,
       marketplace_sku varchar,
       shipto_company varchar,
       shipto_attn varchar,
       shipto_street varchar,
       shipto_city varchar,
       shipto_state varchar,
       shipto_zip varchar,
       shipto_country varchar,
       sku_qty int check(sku_qty > 0),
       foreign key (market_order_id, marketplace_sku)
               references orders.market_order_skus
	       (market_order_id, marketplace_sku)
);

create table orders.files (
       market_order_id varchar,
       file_path varchar,
       file_type varchar,
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
);
