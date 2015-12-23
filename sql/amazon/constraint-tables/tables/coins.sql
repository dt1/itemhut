
create table amazon_coins.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_coins.valid_item_type (
     item_type varchar primary key
);

create table amazon_coins.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_coins.valid_offering_can_be_gift_messaged (
     offering_can_be_gift_messaged varchar primary key
);

create table amazon_coins.valid_offering_can_be_giftwrapped (
     offering_can_be_giftwrapped varchar primary key
);

create table amazon_coins.valid_website_shipping_weight_unit_of_measure (
     website_shipping_weight_unit_of_measure varchar primary key
);

create table amazon_coins.valid_item_weight_unit_of_measure (
     item_weight_unit_of_measure varchar primary key
);

create table amazon_coins.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_coins.valid_package_dimensions_unit_of_measure (
     package_dimensions_unit_of_measure varchar primary key
);

create table amazon_coins.valid_package_weight_unit_of_measure (
     package_weight_unit_of_measure varchar primary key
);

create table amazon_coins.valid_country_of_origin (
     country_of_origin varchar primary key
);

create table amazon_coins.valid_mint_mark (
     mint_mark varchar primary key
);

create table amazon_coins.valid_denomination_unit (
     denomination_unit varchar primary key
);

create table amazon_coins.valid_series_title (
     series_title varchar primary key
);

create table amazon_coins.valid_variety (
     variety varchar primary key
);

create table amazon_coins.valid_item_styling (
     item_styling varchar primary key
);

create table amazon_coins.valid_graded_by (
     graded_by varchar primary key
);

create table amazon_coins.valid_grade_rating (
     grade_rating varchar primary key
);

create table amazon_coins.valid_unit_grouping (
     unit_grouping varchar primary key
);

create table amazon_coins.valid_style_name (
     style_name varchar primary key
);

create table amazon_coins.valid_designation (
     designation varchar primary key
);

create table amazon_coins.valid_edge_style (
     edge_style varchar primary key
);

create table amazon_coins.valid_designer (
     designer varchar primary key
);

create table amazon_coins.valid_estate_period (
     estate_period varchar primary key
);

create table amazon_coins.valid_material_type (
     material_type varchar primary key
);

create table amazon_coins.valid_item_diameter_unit_of_measure (
     item_diameter_unit_of_measure varchar primary key
);

create table amazon_coins.valid_total_metal_weight_unit_of_measure (
     total_metal_weight_unit_of_measure varchar primary key
);

create table amazon_coins.valid_metal_stamp (
     metal_stamp varchar primary key
);
