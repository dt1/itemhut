-- http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddFixedPriceItem.html

drop schema ebay_product cascade;
create schema ebay_product;

create or replace function build_tf_table (table_name varchar)
returns void as
$$
begin


	execute format
	('create table ebay_product.valid_%1$I (
		%1$I varchar primary key);

	insert into ebay_product.valid_%1$I
	(%1$I)
	values (''true''), (''false'');', table_name);
end;
$$ language plpgsql;

create table ebay_product.valid_linked_pay_pal_account (
       linked_pay_pal_account varchar
);

select build_tf_table('auto_pay');
select build_tf_table('category_based_attributes_prefill');
select build_tf_table('category_mapping_allowed');
select build_tf_table('charity');
select build_tf_table('return_search_result_on_duplicates');
select build_tf_table('use_stock_photo_url_as_gallery');
select build_tf_table('use_first_product');
select build_tf_table('global_shipping');
select build_tf_table('disable_buyer_requirements');
select build_tf_table('gift_icon');
select build_tf_table('include_recommendations');
select build_tf_table('optimal_picture_size');
select build_tf_table('post_checkout_experience_enabled');
select build_tf_table('include_ebay_product_details');
select build_tf_table('private_listing');
select build_tf_table('shipping_included_in_tax');
select build_tf_table('free_shipping');
select build_tf_table('shipping_irregular');
select build_tf_table('shipping_terms_in_description');
select build_tf_table('skype_enabled');
select build_tf_table('use_tax_table');

create table ebay_product.charities (
       charity_id varchar primary key,
       charity_number int unique
);

create table ebay_product.valid_conditions (
       condition_id int primary key,
       condition_name varchar
);

insert into ebay_product.valid_conditions (condition_id, condition_name)
values
(1000, 'New'),
(1500, 'New other (see details)'),
(1750, 'New with defects'),
(2000, 'Manufacturer refurbished'),
(2500, 'Seller refurbished'),
(2750, 'Like New'),
(3000, 'Used'),
(4000, 'Very Good'),
(5000, 'Good'),
(6000, 'Acceptable'),
(7000, 'For parts or not working');

create table ebay_product.valid_discount_price_info (
       discount_price_info varchar primary key
);

create table ebay_product.valid_gift_services (
       gift_services varchar primary key
);

insert into ebay_product.valid_gift_services (gift_services)
values
('GiftExpressShipping'),
('GiftShipToRecipient'),
('GiftWrap');

create table ebay_product.valid_hit_counter (
       hit_counter varchar primary key
);

insert into ebay_product.valid_hit_counter (hit_counter)
values
('BasicStyle'),
('GreenLED'),
('Hidden'),
('HiddenStyle'),
('HonestyStyle'),
('NoHitCounter'),
('RetroStyle');



create table ebay_product.valid_inventory_tracking_method (
       inventory_tracking_method varchar primary key
);

insert into ebay_product.valid_inventory_tracking_method
values ('ItemID'), ('SKU');

create table ebay_product.valid_listing_designer (
       listing_designer varchar primary key
);

insert into ebay_product.valid_listing_designer (listing_designer)
values
('LayoutID'),
('OptimalPictureSize'),
('ThemeID');



create table ebay_product.themes (
       theme_id int primary key,
       theme_name varchar unique,
       theme_content varchar
);


create table ebay_product.listing_designer (
       layout_id int primary key,
       optimal_picture_size varchar,
       theme_id int,
       foreign key (optimal_picture_size)
               references ebay_product.valid_optimal_picture_size (optimal_picture_size),
       foreign key (theme_id)
               references ebay_product.themes (theme_id)
);

create table ebay_product.valid_listing_duration (
       listing_duration varchar primary key
);

create table ebay_product.valid_listing_enhancement (
       listing_enhancement varchar primary key
);

insert into ebay_product.valid_listing_enhancement (listing_enhancement)
values
('Featured'),
('Highlight'),
('HomePageFeatured'),
('ProPackBundle'),
('ProPackPlusBundle'),
('ValuePackBundle');

create table ebay_product.valid_listing_type (
       listing_type varchar primary key
);

insert into ebay_product.valid_listing_type (listing_type)
values
('AdType'),
('Chinese'),
('FixedPriceItem'),
('LeadGeneration');

create table ebay_product.valid_payment_methods (
      payment_methods varchar primary key
);

insert into ebay_product.valid_payment_methods (payment_methods)
values
('AmEx'),('CashInPerson'),('CashOnPickup'),('CCAccepted'),('COD'),('CODPrePayDelivery'),('CreditCard'),('CustomCode'),('Diners'),('DirectDebit'),('Discover'),('ELV'),('Escrow'),('IntegratedMerchantCreditCard'),('LoanCheck'),('MOCC'),('Moneybookers'),('MoneyXferAccepted'),('MoneyXferAcceptedInCheckout'),('None'),('Other'),('OtherOnlinePayments'),('PaisaPayAccepted'),('PaisaPayEscrow'),('PaisaPayEscrowEMI'),('PayOnPickup'),('PayPal'),('PayPalCredit'),('PayUponInvoice'),('PersonalCheck'),('PostalTransfer'),('PrePayDelivery'),('ProPay'),('VisaMC');

create table ebay_product.valid_gallery_duration (
       gallery_duration varchar primary key
);

insert into ebay_product.valid_gallery_duration (gallery_duration)
values
('Days_7'),
('Lifetime');

create table ebay_product.valid_picture_source (
       picture_source varchar primary key
);

insert into ebay_product.valid_picture_source (picture_source)
values
('EPS'),
('Vendor');

create table ebay_product.picture_details (
       item_sku varchar primary key,
       gallery_duration varchar,
       -- PhotoDisplay varchar -- add in later
       picture_source varchar,
       picture_url_1 varchar,
       picture_url_2 varchar,
       picture_url_3 varchar,
       picture_url_4 varchar,
       picture_url_5 varchar,
       picture_url_6 varchar,
       picture_url_7 varchar,
       picture_url_8 varchar,
       picture_url_9 varchar,
       picture_url_10 varchar,
       picture_url_11 varchar,
       picture_url_12 varchar,
       picture_url_13 varchar,
       picture_url_14 varchar,
       picture_url_15 varchar,
       picture_url_16 varchar,
       picture_url_17 varchar,
       picture_url_18 varchar,
       picture_url_19 varchar,
       picture_url_20 varchar,
       picture_url_21 varchar,
       picture_url_22 varchar,
       picture_url_23 varchar,
       picture_url_24 varchar,
       foreign key (gallery_duration)
               references ebay_product.valid_gallery_duration
	       		  (gallery_duration),
       foreign key (picture_source)
               references ebay_product.valid_picture_source
	       		  (picture_source)
);







create table ebay_product.valid_insurance_option (
       insurance_option varchar primary key
);

insert into ebay_product.valid_insurance_option
(insurance_option)
values
('IncludedInShippingHandling'),
('NotOffered'),
('Optional'),
('Required');



-- do later:
-- create table ebay_product.ticket_listing_details(

-- );

create table ebay_product.product_listing_details (
       item_sku varchar primary key,
       brand varchar,
       mpn varchar (65),
       ean varchar (13),
       include_ebay_product_details varchar,
       include_stock_photo_url varchar,
       isbm varchar,
       product_id varchar,
       product_reference_id varchar,
       return_search_result_on_duplicates varchar,
       upc bigint,
       use_first_product varchar,
       use_stock_photo_url_as_gallery varchar,
       foreign key (include_ebay_product_details)
               references ebay_product.valid_include_ebay_product_details (include_ebay_product_details),
       foreign key (include_ebay_product_details)
               references ebay_product.valid_include_ebay_product_details (include_ebay_product_details),
       foreign key (return_search_result_on_duplicates)
               references ebay_product.valid_return_search_result_on_duplicates
	       		  (return_search_result_on_duplicates),
       foreign key (upc)
               references product.sku_upc (upc),
       foreign key (return_search_result_on_duplicates)
               references ebay_product.valid_return_search_result_on_duplicates
	       		  (return_search_result_on_duplicates),
       foreign key (use_stock_photo_url_as_gallery)
               references ebay_product.valid_use_stock_photo_url_as_gallery
	       		  (use_stock_photo_url_as_gallery),
       foreign key (use_first_product)
               references ebay_product.valid_use_first_product
	       		  (use_first_product)
);

create table ebay_product.quantity_restriction_per_buyer (
       maximum_quantity int check (maximum_quantity > 0)
);

create table ebay_product.valid_measurement_unit (
       measurement_unit varchar primary key
);

insert into ebay_product.valid_measurement_unit
(measurement_unit)
values
('English'), ('Metric');

create table ebay_product.valid_shipping_type (
       shipping_type varchar primary key
);

insert into ebay_product.valid_shipping_type
(shipping_type)
values
('Calculated'),
('CalculatedDomesticFlatInternational'),
('Flat'),
('FlatDomesticCalculatedInternational'),
('FreightFlat'),
('NotSpecified');

create table ebay_product.valid_shipping_package (
       shipping_package varchar primary key
);

insert into ebay_product.valid_shipping_package
(shipping_package)
values
('BulkyGoods'),('Caravan'),('Cars'),('CustomCode'),('Europallet'),('ExpandableToughBags'),('ExtraLargePack'),('Furniture'),('IndustryVehicles'),('LargeCanadaPostBox'),('LargeCanadaPostBubbleMailer'),('LargeEnvelope'),('Letter'),('MailingBoxes'),('MediumCanadaPostBox'),('MediumCanadaPostBubbleMailer'),('Motorbikes'),('None'),('OneWayPallet'),('PackageThickEnvelope'),('PaddedBags'),('ParcelOrPaddedEnvelope'),('Roll'),('SmallCanadaPostBox'),('SmallCanadaPostBubbleMailer'),('ToughBags'),('UPSLetter'),('USPSFlatRateEnvelope'),('USPSLargePack'),('VeryLargePack'),('Winepak');

create table ebay_product.shipping_package_details (
       shipping_package_detail_id serial primary key,
       shipping_package varchar,
       shipping_package_details_measurement_unit varchar default 'English',
       -- under ShippingPackageDetails.PackageDepth
       package_depth_unit varchar,
       package_depth_measurement_system varchar,
       -- under ShippingPackageDetails.PackageLength
       package_length_unit varchar,
       package_length_measurement_system varchar,
       -- under ShippingPackageDetails.PackageWidth
       package_width_unit varchar,
       package_width_measurement_system varchar,
       shipping_irregular varchar,
       -- under ShippingPackageDetails.WeightMajor
       weight_major int,
       weight_major_unit varchar,
       weight_major_measurement_system  varchar,
       -- under ShippingPackageDetails.WeightMinor
       weight_minor int,
       weight_minor_unit varchar,
       weight_minor_measurement_system varchar,

       foreign key (shipping_irregular)
               references ebay_product.valid_shipping_irregular
	       		  (shipping_irregular),
       foreign key (shipping_package)
               references ebay_product.valid_shipping_package
	       		  (shipping_package)
);

create table ebay_product.valid_skype_contact_option (
       skype_contact_option varchar primary key
);

insert into ebay_product.valid_skype_contact_option
(skype_contact_option)
values
('Chat'), ('Voice');

-- do later
create table ebay_product.storefront ();

-- ApplicationData
-- AutoPay
-- BuyerRequirementDetails
create table ebay_product.products (
       item_sku varchar primary key,
       application_data varchar(32),
       auto_pay varchar,
       buyer_requirement_details varchar,
       category_based_attributes_prefill varchar default 'true',
       category_mapping_allowed varchar default 'false',
       charity varchar default 'false',
       donation_percent float,
       condition_description varchar(1000),
       condition_id int,
       country varchar not null default 'US',
       -- add fk to country http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/extra/AddFxdPrcItm.Rqst.Itm.Cntry.html
       -- cross_border_trade varchar -- add in later
       currency varchar not null default 'USD',
       -- add fk to currency http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/types/CurrencyCodeType.html
       description varchar(500000),
       -- DigitalGoodInfo varchar -- add in later
       disable_buyer_requirements varchar default 'false',
       -- discount_price_info varchar -- add in later
       dispatch_time_max int,
       gift_icon varchar,
       gift_services varchar,
       hit_counter varchar,
       include_recommendations varchar,
       inventory_tracking_method varchar,
       -- ItemCompatibilityList varchar -- add in later
       -- item_specifics varchar -- add in later
       -- ListingCheckoutRedirectPreference -- add in later
       listing_designer varchar,
       -- listing_duration varchar, -- come back to soon, critical
       listing_enhancement varchar,
       listing_type varchar default 'Chinese',
       location varchar,
       payment_methods varchar,
       pay_pal_email_address varchar,
       -- PickupInStoreDetails -- add in later
       postal_code varchar not null,
       post_checkout_experience_enabled varchar,
       -- primary_category varchar -- come back to soon, critical
       private_listing varchar,
       private_notes varchar,
       quantity int,
       -- secondary_category varchar, -- come back to soon, critical
       -- seller varchar, eBay Motors; add later
       -- seller_inventory_id varchar, -- for half.com; return to ltr
       -- seller_provided_title varchar, -- for motors; return to ltr
       -- under ShippingDetails.CalculatedShippingRate:
       -- not supporting international yet
       -- international_packaging_handling_costs numeric,
       -- under ShippingDetails
       cod_cost numeric,
       cod_cost_currency_id varchar,
       exclude_ship_to_location varchar,
       global_shipping varchar,
       -- under ShippingDetails.InsuranceDetails
       insurance_fee numeric,
       insurance_fee_currency_id varchar,
       insurance_option varchar,
       -- under ShippingDetails.SalesTax
       shipping_details_sales_tax_percent float,
       shipping_details_sales_tax_state varchar,
       shipping_included_in_tax varchar,
       shipping_discount_profile_id varchar,
       shipping_type varchar,
       -- under ShippingPackageDetails
       shipping_package_detail_id int,
       shipping_package varchar,
       measurement_unit varchar default 'English',
       originating_postal_code varchar,
       shipping_terms_in_description varchar,
       -- ship_to_locations -- add later
       -- site -- look into later
       skype_enabled varchar,
       skype_contact_option varchar,
       skype_id varchar,
       start_price numeric not null,
       start_price_currency_id varchar,
       sub_title varchar(80),
       -- tax_category -- probably not ever needed?
       -- third_party_checkout -- probably not ever needed?
       -- third_party_checkout_integration -- probably not ever needed?
       title varchar(80),
       -- use_recommended_product -- return to later
       use_tax_table varchar,
       -- uuid -- later
       -- vat_details later
       -- vin -- no motors at the moment
       -- vrm -- no motors at the moment
       foreign key (auto_pay)
               references ebay_product.valid_auto_pay (auto_pay),
       foreign key (category_based_attributes_prefill)
               references ebay_product.valid_category_based_attributes_prefill
	       		  (category_based_attributes_prefill),
       foreign key (category_mapping_allowed)
               references ebay_product.valid_category_mapping_allowed
	       		  (category_mapping_allowed),
       foreign key (charity)
               references ebay_product.valid_charity
	       		  (charity),
       foreign key (disable_buyer_requirements)
               references ebay_product.valid_disable_buyer_requirements
	       		  (disable_buyer_requirements),
       -- foreign key (discount_price_info)
       --         references ebay_product.valid_discount_price_info
       -- 	       		  (discount_price_info)
       foreign key (gift_icon)
               references ebay_product.valid_gift_icon
	       		  (gift_icon),
       foreign key (gift_services)
               references ebay_product.valid_gift_services
	       		  (gift_services),
       foreign key (hit_counter)
               references ebay_product.valid_hit_counter
	       		  (hit_counter),
       foreign key (include_recommendations)
               references ebay_product.valid_include_recommendations
	       		  (include_recommendations),
       foreign key (inventory_tracking_method)
               references ebay_product.valid_inventory_tracking_method
	       		  (inventory_tracking_method),
       foreign key (listing_designer)
               references ebay_product.valid_listing_designer
	       		  (listing_designer),
       foreign key (listing_enhancement)
               references ebay_product.valid_listing_enhancement
	       		  (listing_enhancement),
       foreign key (listing_type)
               references ebay_product.valid_listing_type
	       		  (listing_type),
       foreign key (payment_methods)
               references ebay_product.valid_payment_methods
	       		  (payment_methods),
       foreign key (post_checkout_experience_enabled)
               references ebay_product.valid_post_checkout_experience_enabled
	       		  (post_checkout_experience_enabled),
       foreign key (private_listing)
               references ebay_product.valid_private_listing
	       		  (private_listing),
       foreign key (measurement_unit)
               references ebay_product.valid_measurement_unit
	       		  (measurement_unit),
       foreign key (global_shipping)
               references ebay_product.valid_global_shipping
	       		  (global_shipping),
       foreign key (insurance_option)
               references ebay_product.valid_insurance_option
	       		  (insurance_option),
       foreign key (shipping_included_in_tax)
               references ebay_product.valid_shipping_included_in_tax
	       		  (shipping_included_in_tax),
       foreign key (shipping_type)
               references ebay_product.valid_shipping_type
	       		  (shipping_type),
       foreign key (shipping_package_detail_id)
               references ebay_product.shipping_package_details
	       		  (shipping_package_detail_id),
       foreign key (shipping_terms_in_description)
               references ebay_product.valid_shipping_terms_in_description
	       		  (shipping_terms_in_description),
       foreign key (skype_enabled)
               references ebay_product.valid_skype_enabled (skype_enabled),		
       foreign key (skype_contact_option)
               references ebay_product.valid_skype_contact_option (skype_contact_option),
       foreign key (use_tax_table)
               references ebay_product.valid_use_tax_table (use_tax_table)
);

create table ebay_product.quantity_info (
       item_sku varchar,
       minimum_remnant_set int,
       foreign key (item_sku)
               references ebay_product.products (item_sku)
);

create table ebay_product.ReturnPolicy (
       item_sku varchar,
       description varchar,
       refund_option varchar, -- call api to get valid values
       restocking_fee_value_option varchar, -- call api to get valid values
       returns_accepted_option varchar, -- call api to get valid values
       returns_within_option varchar, -- call api to get valid values
       shipping_cost_paid_by_option varchar, -- call api to get valid values
       warranty_duration_option varchar, -- call api to get valid values
       warranty_offered_option varchar, -- call api to get valid values
       warranty_type_option varchar, -- call api to get valid values
       foreign key (item_sku)
               references ebay_product.products (item_sku)

);

-- under ShippingDetails.ShippingServiceOptions
create table ebay_product.shipping_service_options (
       item_sku varchar,
       free_shipping varchar,
       shipping_service varchar,
       additional_cost numeric,
       additional_cost_currency_id varchar,
       shipping_service_cost numeric,
       shipping_service_cost_currency_id varchar,
       shipping_service_priority varchar,
       shipping_surcharge numeric,
       shipping_surcharge_currency_id varchar,
       foreign key (item_sku)
               references ebay_product.products (item_sku),
       foreign key (free_shipping)
               references ebay_product.valid_free_shipping (free_shipping)
);

drop function build_tf_table(varchar);
