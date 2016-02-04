drop schema ebcats cascade;
create schema ebcats;

-- for information on product conditions:
-- http://developer.ebay.com/DevZone/finding/CallRef/Enums/conditionIdList.html?rmvSB=true

-- Item Condition ID
-- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, ConditionID}'
-- from ebords.json_insert;


-- Item Condition ID
-- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, ConditionDisplayName}'
-- from ebords.json_insert;

create table ebcats.json_insert_categories(
  jid serial primary key,
  v jsonb
);

create table ebcats.json_insert_category_features(
  jid serial primary key,
  v jsonb
);


create table ebcats.version_info(
  version int primary key,
  category_count int,
  update_time timestamp,
  download_time timestamp,
  ack varchar,
  jid int,
  foreign key (jid) references ebcats.json_insert_categories (jid)
);

create table ebcats.categories(
  category_id int primary key,
  category_name varchar,
  category_level int,
  auto_pay_enabled boolean,
  best_offer_enabled boolean,
  category_parent_id int,
  leaf_category boolean,
);


create table ebcats.typical_condition_ids(
  condition_id int primary key,
  typical_name varchar,
  typical_definition varchar
);

create table ebcats.category_condition_ids(
       condition_id int,
       category_id int,
       display_name varchar,
       primary key (condition_id, category_id),
       foreign key (condition_id)
       	       references ebcats.typical_condition_ids (condition_id)
	       on update cascade,
       foreign key (category_id)
               references ebcats.categories (category_id)
	       on update cascade
);


create table ebcats.category_features(
       category_id int primary key,
       best_offer_auto_decline_enabled boolean,
       best_offer_counter_enabled boolean,
       free_gallery_plus_enabled boolean,
       best_offer_auto_accept_enabled boolean,
       best_offer_enabled boolean,
       pro_pack_plus_enabled boolean,
       global_shipping_enabled boolean,
       free_picture_pack_enabled boolean,
       value_pack_enabled boolean,
       chinese int,
       dutch int,
       live int,
       ad_type int,
       stores_fixed_price int,
       personal_offer int,
       fixed_price_item int,
       lead_generation int,
       shopping int,
       foreign key (category_id)
       	       references ebcats.categories (category_id)
	       on update cascade
);
