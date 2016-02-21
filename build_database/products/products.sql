-- the base company skus.
-- ideally, we'd want UPC to be gtin-12, but some custom UPCs may be created
-- for pieces or replacements, and "master" SKUs for product variations.
drop schema if exists product cascade; -- for my testing

create schema if not exists product;

create table product.sku_types (
       sku_type varchar primary key
);

-- regular: all single-item SKUs. shoud have a gtin-12
-- master: for kits of products as packages; ie. shirt and tie
-- piece: for products that are pieces of a main item: ie. shoe laces
-- replacement part, such as a screw

insert into product.sku_types (sku_type) values
('regular'),
('piece'),
('master'),
('replacement-part');

-- in general, a kit or replacement part should not have a upc, but for listing purposes.

create table product.sku_upc (
       sku varchar primary key,
       upc bigint unique,
       sku_type varchar not null default 'regular',
       foreign key (sku_type) references product.sku_types (sku_type)
);

create table product.kits (
       master_sku varchar,
       child_sku varchar,
       child_sku_qty int check (child_sku_qty > 0),
       primary key(master_sku, child_sku),
       foreign key (master_sku)
       	       references product.sku_upc (sku)
	       on update cascade,
       foreign key (child_sku)
       	       references product.sku_upc (sku)
	       on update cascade
);

-- these are for replacement skus that are the same as the original sku
-- or for items that are mislabled.

create table product.alternate_skus (
       original_sku varchar,
       alternate_sku varchar primary key,
       foreign key (original_sku)
               references product.sku_upc (sku)
	       on update cascade,
       foreign key (alternate_sku)
               references product.sku_upc (sku)
	       on update cascade
);

-- the descriptions and pictures tables
-- are for "universal" view of all products
-- that aren't specific to each marketplace.
-- itemhut does not express an opinion on what is
-- correct here, but allows either instance.

create table product.descriptions (
       sku varchar primary key,
       product_name varchar not null,
       product_description varchar,
       bullet_one varchar,
       bullet_two varchar,
       bullet_three varchar,
       bullet_four varchar,
       bullet_five varchar,
       foreign key (sku)
       	       references product.sku_upc (sku)
	       on update cascade
);

create table product.images (
       sku varchar primary key,
       main_image varchar,
       image_one varchar,
       image_two varchar,
       image_three varchar,
       image_four varchar,
       image_five varchar,
       image_six varchar,
       image_seven varchar,
       image_eight varchar,
       image_nine varchar,
       image_ten varchar,
       image_eleven varchar,
       image_twelve varchar,
       swatch_image varchar,
       foreign key (sku)
       	       references product.sku_upc (sku)
	       on update cascade
);
