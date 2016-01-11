create schema warehouse;

create table warehouse.warehouses (
       warehouse_id serial primary key,
       warehouse_name varchar unique,
       warehouse_street_address varchar,
       warehouse_state varchar,
       warehouse_zip varchar,
       warehouse_country varchar
);

create table warehouse.pallet_locations (
       pallet_location varchar primary key
       sku varchar,
       foreign key (sku)
               references products.sku_upc (sku)
);

create table warehouse.warehouse_pallet_loc (
       warehouse_id int,
       pallet_location varchar,
       foreign key (warehouse_id)
               references warehouse.warehouses (warehouse_id),
       foreign key (pallet_location)
               references warehouse.pallet_location (pallet_location)
);

