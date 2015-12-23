
create table amazon_office.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_office.valid_gtin_exemption_reason (
     gtin_exemption_reason varchar primary key
);

create table amazon_office.valid_related_product_id_type (
     related_product_id_type varchar primary key
);

create table amazon_office.valid_feed_product_type (
     feed_product_type varchar primary key
);

create table amazon_office.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_office.valid_product_tax_code (
     product_tax_code varchar primary key
);

create table amazon_office.valid_offering_can_be_giftwrapped (
     offering_can_be_giftwrapped varchar primary key
);

create table amazon_office.valid_offering_can_be_gift_messaged (
     offering_can_be_gift_messaged varchar primary key
);

create table amazon_office.valid_currency (
     currency varchar primary key
);

create table amazon_office.valid_is_discontinued_by_manufacturer (
     is_discontinued_by_manufacturer varchar primary key
);

create table amazon_office.valid_missing_keyset_reason (
     missing_keyset_reason varchar primary key
);

create table amazon_office.valid_item_length_unit_of_measure (
     item_length_unit_of_measure varchar primary key
);

create table amazon_office.valid_item_weight_unit_of_measure (
     item_weight_unit_of_measure varchar primary key
);

create table amazon_office.valid_website_shipping_weight_unit_of_measure (
     website_shipping_weight_unit_of_measure varchar primary key
);

create table amazon_office.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_office.valid_parent_child (
     parent_child varchar primary key
);

create table amazon_office.valid_relationship_type (
     relationship_type varchar primary key
);

create table amazon_office.valid_variation_theme (
     variation_theme varchar primary key
);

create table amazon_office.valid_cpsia_cautionary_statement (
     cpsia_cautionary_statement varchar primary key
);

create table amazon_office.valid_prop_65 (
     prop_65 varchar primary key
);

create table amazon_office.valid_power_source_type (
     power_source_type varchar primary key
);

create table amazon_office.valid_resolution_base (
     resolution_base varchar primary key
);

create table amazon_office.valid_display_type (
     display_type varchar primary key
);

create table amazon_office.valid_includes_rechargable_battery (
     includes_rechargable_battery varchar primary key
);

create table amazon_office.valid_special_features (
     special_features varchar primary key
);

create table amazon_office.valid_battery_type (
     battery_type varchar primary key
);

create table amazon_office.valid_are_batteries_included (
     are_batteries_included varchar primary key
);

create table amazon_office.valid_mfg_warranty_description_type (
     mfg_warranty_description_type varchar primary key
);

create table amazon_office.valid_caller_identification (
     caller_identification varchar primary key
);

create table amazon_office.valid_color_map (
     color_map varchar primary key
);

create table amazon_office.valid_maximum_size_unit_of_measure (
     maximum_size_unit_of_measure varchar primary key
);

create table amazon_office.valid_line_size_unit_of_measure (
     line_size_unit_of_measure varchar primary key
);

create table amazon_office.valid_paper_size (
     paper_size varchar primary key
);

create table amazon_office.valid_included_features (
     included_features varchar primary key
);

create table amazon_office.valid_connectivity_technology (
     connectivity_technology varchar primary key
);

create table amazon_office.valid_hardware_platform (
     hardware_platform varchar primary key
);

create table amazon_office.valid_input_device_interface (
     input_device_interface varchar primary key
);

create table amazon_office.valid_operating_system (
     operating_system varchar primary key
);

create table amazon_office.valid_paper_finish (
     paper_finish varchar primary key
);
