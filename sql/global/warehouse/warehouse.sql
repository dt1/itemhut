create schema warehouse;

create table warehouse.warehouses (
       warehouse_id serial primary key,
       warehouse_name varchar unique,
       warehouse_street_address varchar,
       warehouse_state varchar,
       warehouse_zip varchar,
       warehouse_country varchar
);

create table warehouse.pallets (
       pallet_id serial primary key
);

create table warehouse.cases (
       case_id serial primary key,
       sku varchar,
       qty int check (qty > 0),
       foreign key (sku)
               references products.sku_upc (sku)
);

create table warehouse.pallet_case (
       pallet_id int,
       case_id int,
       primary key (pallet_id, case_id),
       foreign key (pallet_id)
               references warehouse.pallets (pallet_id),
       foreign key (case_id)
               references warehouse.cases (case_id)	       
);

create table warehouse.pallet_locations (
       pallet_location varchar primary key
       pallet_id varchar,
       foreign key (pallet_id)
               references warehouse.pallets (pallet_id)
);

create table warehouse.warehouse_pallet_loc (
       warehouse_id int,
       pallet_location varchar,
       foreign key (warehouse_id)
               references warehouse.warehouses (warehouse_id),
       foreign key (pallet_location)
               references warehouse.pallet_location (pallet_location)
);

create table warehouse.picking_locations (
       picking_location varchar primary key,
       sku varchar primary key,
       qty int check (qty > 0),
       foreign key (sku)
               references products.sku_upc (sku)
);

create table warehouse.pickers (
       picker_id serial primary key,
       picker_first_name varchar,
       picker_last_name varchar
);

create table warehouse.picker_picked (
       picker_id int,
       picking_location int,
       qty int,
       datetime timetamp default now(),
       foreign key (picker_id)
               references warehouse.picker_id (picker_id),
       foreign key (picking_location)
               references warehouse.picking_locations (picking_location)	      
);


