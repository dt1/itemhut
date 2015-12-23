
create table amazon_swvg.valid_feed_product_type (
     feed_product_type varchar primary key
);

create table amazon_swvg.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_swvg.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_swvg.valid_condition_type (
     condition_type varchar primary key
);

create table amazon_swvg.valid_currency (
     currency varchar primary key
);

create table amazon_swvg.valid_product_tax_code (
     product_tax_code varchar primary key
);

create table amazon_swvg.valid_offering_can_be_gift_messaged (
     offering_can_be_gift_messaged varchar primary key
);

create table amazon_swvg.valid_offering_can_be_giftwrapped (
     offering_can_be_giftwrapped varchar primary key
);

create table amazon_swvg.valid_is_discontinued_by_manufacturer (
     is_discontinued_by_manufacturer varchar primary key
);

create table amazon_swvg.valid_missing_keyset_reason (
     missing_keyset_reason varchar primary key
);

create table amazon_swvg.valid_item_weight_unit_of_measure (
     item_weight_unit_of_measure varchar primary key
);

create table amazon_swvg.valid_item_length_unit_of_measure (
     item_length_unit_of_measure varchar primary key
);

create table amazon_swvg.valid_website_shipping_weight_unit_of_measure (
     website_shipping_weight_unit_of_measure varchar primary key
);

create table amazon_swvg.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_swvg.valid_prop_65 (
     prop_65 varchar primary key
);

create table amazon_swvg.valid_cpsia_cautionary_statement (
     cpsia_cautionary_statement varchar primary key
);

create table amazon_swvg.valid_hardware_platform (
     hardware_platform varchar primary key
);

create table amazon_swvg.valid_esrb_age_rating (
     esrb_age_rating varchar primary key
);

create table amazon_swvg.valid_genre (
     genre varchar primary key
);

create table amazon_swvg.valid_color_map (
     color_map varchar primary key
);

create table amazon_swvg.valid_operating_system (
     operating_system varchar primary key
);

create table amazon_swvg.valid_online_play (
     online_play varchar primary key
);

create table amazon_swvg.valid_format (
     format varchar primary key
);

create table amazon_swvg.valid_system_requirements_platform (
     system_requirements_platform varchar primary key
);
