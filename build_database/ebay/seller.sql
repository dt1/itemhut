create schema seller;

-- for classified listings, return to later
-- http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddItem.html#AddItem

create table ebay_seller.seller_contact_details (
       company_name varchar,
       county varchar,
       phone2_area_or_city_code int,
       phone2_country_code varchar
       
);

-- what is this?
create table ebay_seller.seller_profiles (

);
