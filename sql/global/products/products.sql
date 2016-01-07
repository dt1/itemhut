-- the base company skus.
-- ideally, we'd want UPC to be gtin-12, but some custom UPCs may be created for pieces or replacements, and "master" SKUs for product variations.
drop schema product cascade;

create schema product;

create table product.sku_types (
       sku_type varchar primary key
);

insert into product.sku_types (sku_type) values
('regular'),
('piece'),
('master')
('replacement-part');

create table product.sku_upc (
       sku varchar primary key,
       upc bigint unique,
       sku_type varchar default 'regular',
       foreign key (sku_type) references product.sku_types (sku_type)
);

create table product.variations (
       master_sku varchar,
       child_sku varchar,
       foreign key (master_sku) references product.sku_upc (sku),
       foreign key (child_sku) references product.sku_upc (sku)
);

create table product.descriptions (
       sku varchar primary key,
       product_name varchar,
       product_decription varchar,
       bullet_one varchar,
       bullet_two varchar,
       bullet_three varchar,
       bullet_four varchar,
       bullet_five varchar,
       foreign key (sku) references product.sku_upc (sku)
);

create table product.pictures (
       sku varchar primary key,
       main_picture varchar,
       picture_one varchar,
       picture_two varchar,
       picture_three varchar,
       picture_four varchar,
       picture_five varchar,
       picture_six varchar,
       picture_seven varchar,
       picture_eight varchar,
       picture_nine varchar,
       picture_ten varchar,
       picture_eleven varchar,
       picture_twelve varchar,
       swatch_picture varchar,
       foreign key (sku) references product.sku_upc (sku)
);
