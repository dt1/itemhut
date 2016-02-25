-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema if not exists orders;

create table orders.msku_sku (
       marketplace_sku varchar primary key,
       sku varchar,
       foreign key (sku)
               references product.sku_upc (sku)
);

create table orders.market_orders (
       market_order_id varchar primary key,
       marketplace varchar not null default 'testing',
       marketplace_sku varchar not null,
       qty_sold int check(qty_sold > 0),
       order_date date default now(),
       foreign key (marketplace_sku)
               references orders.msku_sku (msku)
);

create table orders.orders (
       order_id bigserial primary key,
       market_order_id varchar unique,
       foreign key (market_order_id)
               references orders.market_orders (market_order_id)
);

