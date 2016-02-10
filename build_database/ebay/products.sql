-- http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddFixedPriceItem.html
create schema ebay_product;


create table ebay_product.valid_linked_pay_pal_account (
       linked_pay_pal_account varchar
);

create table ebay_product.valid_auto_pay (
       auto_pay varchar primary key
);

insert into ebay_product.valid_auto_pay (auto_pay)
values ('true'), ('false');

create table ebay_product.category_based_attributes_prefill (
       category_based_attributes_prefill varchar primary key
);

insert into ebay_product.valid_category_based_attributes_prefill
(category_based_attributes_prefill)
values ('true'), ('false');

create table ebay_product.valid_category_mapping_allowed (
       auto_pay varchar primary key
);

insert into ebay_product.valid_category_mapping_allowed
(category_mapping_allowed)
values ('true'), ('false');

create table ebay_product.valid_charity (
       charity varchar primary key
);

insert into ebay_product.charity (charity)
values ('true'), ('false');

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

create table ebay_product.valid_disable_buyer_requirements (
       disable_buyer_requirements varchar primary key
);

insert into ebay_product.valid_disable_buyer_requirements
(disable_buyer_requirements)
values ('true'), ('false');

create table ebay_product.valid_discount_price_info (
       discount_price_info varchar primary key
);

create table ebay_product.valid_gift_icon (
       gift_icon varchar primary key
);

insert into ebay_product.valid_gift_icon (gift_icon)
values ('true'), ('false');

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

create table ebay_product.valid_include_recommendations (
       include_recommendations varchar primary key
);

insert into ebay_product.valid_include_recommendations
(include_recommendations)
values ('true'), ('false');

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

create table ebay_product.valid_optimal_picture_size (
       optimal_picture_size varchar primary key
);

insert into ebay_product.valid_optimal_picture_size (optimal_picture_size)
values ('true'), ('false');

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
               references ebay_product (optimal_picture_size),
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
       picture_details varchar primary key
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

create table ebay_product.valid_post_checkout_experience_enabled (
       post_checkout_experience_enabled varchar primary key
);

insert into ebay_product.valid_post_checkout_experience_enabled
(post_checkout_experience_enabled)
values
('true'), ('false');


create table ebay_product.valid_private_listing (
       private_listing varchar primary key
);

insert into ebay_product.valid_private_listing
(private_listing)
values
('true'), ('false');

create table ebay_product.valid_include_ebay_product_details (
       include_ebay_product_details varchar primary key
);


insert into ebay_product.valid_include_ebay_product_details
(include_ebay_product_details)
values
('true'), ('false');

create table ebay_product.valid_include_ebay_product_details (
       include_ebay_product_details varchar primary key
);


insert into ebay_product.valid_include_ebay_product_details
(include_ebay_product_details)
values
('true'), ('false');

create table ebay_product.valid_return_search_result_on_duplicates (
       return_search_result_on_duplicates varchar primary key
);

insert into ebay_product.valid_return_search_result_on_duplicates
(return_search_result_on_duplicates)
values
('true'), ('false');

create table ebay_product.valid_use_stock_photo_url_as_gallery (
       use_stock_photo_url_as_gallery varchar primary key
);

insert into ebay_product.valid_use_stock_photo_url_as_gallery
(use_stock_photo_url_as_gallery)
values
('true'), ('false');

create table ebay_product.valid_use_first_product (
       use_first_product varchar primary key
);

insert into ebay_product.valid_use_first_product
(use_first_product)
values
('true'), ('false');




insert into ebay_product.valid_return_search_result_on_duplicates
(return_search_result_on_duplicates)
values
('true'), ('false');


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
	       		  (return_search_result_on_duplicates)
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

create table ebay_product.quantity_info (
       item_sku varchar,
       minimum_remnant_set int,
       foreign key (item_sku)
               references ebay_product.products (item_sku)
);

create table ebay_product.quantity_restriction_per_buyer (
       maximum_quantity int check (maximum_quantity > 0)
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


-- ApplicationData
-- AutoPay
-- BuyerRequirementDetails
create table ebay_product.products (
       application_data varchar(32) primary key,
       item_sku varchar primary key,
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
);
