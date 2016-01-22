drop schema if exists warehouse cascade;

create schema if not exists warehouse;

create table warehouse.warehouses (
       warehouse_id serial primary key,
       warehouse_name varchar unique not null,
       warehouse_street_address varchar,
       warehouse_state varchar,
       warehouse_zip varchar,
       warehouse_country varchar
);

create table warehouse.pallets (
       pallet_id serial primary key
);

create table warehouse.pallet_locations (
       pallet_location_id serial primary key,
       pallet_location_name varchar
);

create table warehouse.warehouse_pallet_loc (
       warehouse_id int,
       pallet_location_id int primary key,
       foreign key (warehouse_id)
               references warehouse.warehouses (warehouse_id),
       foreign key (pallet_location_id)
               references warehouse.pallet_locations (pallet_location_id)
);

create table warehouse.pallet_palletloc (
       pallet_location_id int,
       pallet_id int primary key,
       foreign key (pallet_location_id)
               references warehouse.pallet_locations (pallet_location_id),
       foreign key (pallet_id)
               references warehouse.pallets (pallet_id)

);

create table warehouse.picking_locations (
       picking_location_id serial primary key,
       picking_location_name varchar,
       sku varchar,
       qty int check (qty > 0),
       foreign key (sku)
               references product.sku_upc (sku)
);

create table warehouse.warehouse_picking_loc (
       warehouse_id int,
       picking_location_id int primary key,
       foreign key (warehouse_id)
               references warehouse.warehouses (warehouse_id),
       foreign key (picking_location_id)
               references warehouse.picking_locations (picking_location_id)
);

create table warehouse.cases (
       case_id serial primary key,
       upc bigint not null,
       qty int check (qty > 0),
       foreign key (upc)
               references product.sku_upc (upc)
);

create table warehouse.pallet_case (
       pallet_id int,
       case_id int primary key,
       foreign key (pallet_id)
               references warehouse.pallets (pallet_id),
       foreign key (case_id)
               references warehouse.cases (case_id)
);

create table warehouse.pickers (
       picker_id serial primary key
);

create table warehouse.picker_picked (
       picker_id int,
       picking_location_id int,
       qty int check (qty > 0),
       datetime timestamp default now(),
       foreign key (picker_id)
               references warehouse.pickers (picker_id),
       foreign key (picking_location_id)
               references warehouse.picking_locations (picking_location_id)
);

create table warehouse.qc_station (
       qc_station_id serial primary key,
       qc_station_name varchar
);

create table warehouse.warehouse_qc_station (
       warehouse_id int,
       qc_station_id int primary key,
       foreign key (warehouse_id)
               references warehouse.warehouses (warehouse_id),
       foreign key (qc_station_id)
               references warehouse.qc_station (qc_station_id)
);

-- add FK to some employee table

create table warehouse.qc_person (
       qc_person_id serial primary key
);

create table warehouse.qc_log (
       qc_station_id int,
       qc_person_id int,
       upc bigint,
       passed boolean default true,
       notes varchar,
       timedate timestamp,
       foreign key (qc_station_id)
               references warehouse.qc_station (qc_station_id),
       foreign key (qc_person_id)
               references warehouse.qc_person (qc_person_id)
);
