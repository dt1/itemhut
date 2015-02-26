create table amazon_video.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_video.valid_feed_product_type (
     feed_product_type varchar primary key
);

create table amazon_video.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_video.valid_binding (
     binding varchar primary key
);

create table amazon_video.valid_condition_type (
     condition_type varchar primary key
);

create table amazon_video.valid_product_tax_code (
     product_tax_code varchar primary key
);

create table amazon_video.valid_expedited_shipping (
     expedited_shipping varchar primary key
);

create table amazon_video.valid_will_ship_internationally (
     will_ship_internationally varchar primary key
);

create table amazon_video.valid_standard_plus (
     standard_plus varchar primary key
);

create table amazon_video.valid_package_weight_unit_of_measure (
     package_weight_unit_of_measure varchar primary key
);

create table amazon_video.valid_package_dimensions_unit_of_measure (
     package_dimensions_unit_of_measure varchar primary key
);

create table amazon_video.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_video.valid_country_of_origin (
     country_of_origin varchar primary key
);

create table amazon_video.valid_cpsia_cautionary_description (
     cpsia_cautionary_description varchar primary key
);

create table amazon_video.valid_cpsia_cautionary_statement (
     cpsia_cautionary_statement varchar primary key
);

create table amazon_video.valid_format (
     format varchar primary key
);

create table amazon_video.valid_mpaa_rating (
     mpaa_rating varchar primary key
);

create table amazon_video.valid_audio_encoding_language (
     audio_encoding_language varchar primary key
);

create table amazon_video.valid_language_subtitled (
     language_subtitled varchar primary key
);

create table amazon_video.valid_is_adult_product (
     is_adult_product varchar primary key
);

create table amazon_video.valid_genre (
     genre varchar primary key
);

create table amazon_video.valid_blu_ray_region (
     blu_ray_region varchar primary key
);

create table amazon_video.valid_dvd_region (
     dvd_region varchar primary key
);
