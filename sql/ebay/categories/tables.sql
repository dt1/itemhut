drop schema ebay_category cascade;

create schema ebay_category;

create table ebay_category.json_insert(
       jid serial primary key,
       v jsonb
);

create table ebay_category.categories (
       category_id int primary key,
       category_name varchar,
       category_level int,
       auto_pay_enabled varchar,
       best_offer_enabled varchar,
       category_parent_id int,
       leaf_category varchar,
       foreign key (auto_pay_enabled)
       	       references ebay_constraints.tf (tf),
       foreign key (best_offer_enabled)
       	       references ebay_constraints.tf (tf),
       foreign key (leaf_category)
       	       references ebay_constraints.tf (tf)
);

create table ebay_category.version_info (
       version int primary key,
       category_count int,
       update_time timestamp,
       download_time timestamp,
       ack varchar
);

create table ebay_category.typical_condition_ids (
  condition_id int primary key,
  typical_name varchar,
  typical_definition varchar
);
