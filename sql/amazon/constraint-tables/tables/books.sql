
create table amazon_book_loader.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_book_loader.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_book_loader.valid_binding (
     binding varchar primary key
);

create table amazon_book_loader.valid_edition (
     edition varchar primary key
);

create table amazon_book_loader.valid_condition_type (
     condition_type varchar primary key
);

create table amazon_book_loader.valid_product_tax_code (
     product_tax_code varchar primary key
);

create table amazon_book_loader.valid_expedited_shipping (
     expedited_shipping varchar primary key
);

create table amazon_book_loader.valid_will_ship_internationally (
     will_ship_internationally varchar primary key
);

create table amazon_book_loader.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_book_loader.valid_package_dimensions_unit_of_measure (
     package_dimensions_unit_of_measure varchar primary key
);

create table amazon_book_loader.valid_package_weight_unit_of_measure (
     package_weight_unit_of_measure varchar primary key
);

create table amazon_book_loader.valid_unknown_subject (
     unknown_subject varchar primary key
);

create table amazon_book_loader.valid_language_value (
     language_value varchar primary key
);

create table amazon_book_loader.valid_format (
     format varchar primary key
);
