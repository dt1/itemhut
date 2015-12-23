drop schema ebay_category_features cascade;

create schema ebay_category_features;

create table ebay_category_features.json_insert (
       jid int primary key,
       v jsonb
);

create table ebay_category_features.info (
       category_version int primary key,
       ack varchar,
       update_time timestamp,
       download_time timestamp,
       version int,
       build varchar
);

create table ebay_category_features.default_tf (
       key varchar primary key,
       value varchar,
       foreign key (value)
                references constraints.tf (tf)
);

create table ebay_category_features.default_gallery_durations (
       gallery_feature_duration varchar primary key
);

create table ebay_category_features.default_listing_durations (
       duration_type varchar primary key,
       duration_value int
);


create table ebay_category_features.default_groups (
       key varchar primary key,
       value varchar,
       foreign key (value)
	        references ebay_constraints.category_groups (groups)
);

create table ebay_category_features.default_payment_methods (
       payment_method varchar primary key
);


create table ebay_category_features.default_subscriptions (
       key varchar primary key,
       value varchar,
       foreign key (value)
		references ebay_constraints.subscriptions
		(subscription)
);

create table ebay_category_features.default_counts (
       key varchar primary key,
       value int
);

create table ebay_category_features.default_prices (
       key varchar primary key,
       value numeric
);


create table ebay_category_features.default_dis_en_abled (
       key varchar primary key,
       value varchar,
       foreign key (value)
	      references ebay_constraints.dis_en_abled (dis_en_abled)
);
