create or replace function ebay_orders.insert_order_errors (jid int,
                                                       v json)
returns table (r_jid int, r_scode varchar, r_epid varchar,
	      r_epval varchar, r_ecode varchar, r_longm varchar,
	      r_errclass varchar, r_shortm varchar)
as
$$

declare
error_array json := v#>'{Errors}';
item json;
t_jid int := jid;
t_scode varchar;
t_epid varchar;
t_epval varchar;
t_ecode varchar;
t_longm varchar;
t_errclass varchar;
t_shortm varchar;

begin
for item in select * from json_array_elements(error_array)
    loop
	t_scode = item#>>'{SeverityCode}';
	t_epid = item#>>'{ErrorParameters, ParamID}';
	t_epval = item#>>'{ErrorParameters, Value}';
	t_ecode = item#>>'{ErrorCode}';
	t_longm = item#>>'{LongMessage}';
	t_errclass = item#>>'{ErrorClassification}';
	t_shortm = item#>>'{ShortMessage}';
		
	if t_epval is not null
	then
	return query values (t_jid, t_scode, t_epid, t_epval, 
		       	     t_ecode, t_longm, t_errclass, t_shortm);
        end if;
       
end loop;
end;
$$ language plpgsql;

----------------------------------------

create or replace function ebay_orders.insert_timestamps (jid int, v json)
returns table (r_jid int, r_ebay_timestamp timestamp,
	      r_system_timestamp timestamp)
as
$$
declare
t_jid int := jid;
t_ebay_timestamp timestamp := v#>>'{Timestamp}';
t_system_timestamp timestamp := now();

begin
	return query values (t_jid, t_ebay_timestamp,
  	       	             t_system_timestamp);
end;
$$ language plpgsql;

----------------------------------------

create or replace function ebay_orders.create_jid_oid_lut (jid int,
                                                      v json)
returns table (r_jid int, r_oid varchar)
as
$$
declare
order_array json := v#>'{OrderArray, Order}';
item json;
t_jid int = jid;
t_oid varchar;
begin

for item in select * from json_array_elements(order_array)
    loop
    t_oid = item#>>'{OrderID}';

    if t_oid not in (select order_id
                   from ebay_orders.jid_order_id_lut
	           limit 1)
    then
    return query values (t_jid, t_oid);
    end if;

end loop;
end;
$$ language plpgsql;

-----------------------------------


create or replace function ebay_orders.create_oid_tid_lut (v json)
returns table (r_oid varchar, r_tid varchar)
as
$$
declare
order_array json := v#>'{OrderArray, Order}';
item json;
t_oid varchar;
t_tid varchar;

begin

for item in select * from json_array_elements(order_array)
loop
    t_oid = item#>>'{OrderID}';
    t_tid = item#>>'{TransactionArray, Transaction, TransactionID}';

    if t_tid is null then
	t_tid = item#>>'{TransactionArray, Transaction, 0, 
	      	         TransactionID}';

    end if;
    
    if t_tid not in (select transaction_array_id
                     from ebay_orders.order_id_transaction_array_id_lut
		     limit 1)
    then
       return query values (t_oid, t_tid);
    end if;
end loop;
end;
$$ language plpgsql;

------------------------------------

create or replace function ebay_orders.insert_jid_oid_lut
                                  (jid int, oid varchar)
returns varchar
as
$$

begin
if oid not in (select order_id
           from ebay_orders.jid_order_id_lut
	   limit 1)
then
insert into ebay_orders.jid_order_id_lut
values (jid, oid);
end if;

return null;
end;
$$ language plpgsql;

---------------------

create or replace function ebay_orders.insert_buyer_info (jid int, v json)
returns table (r_oid varchar, r_address_owner varchar, 
	      r_name varchar, r_address_id varchar, 
	      r_external_address_id varchar,
	      r_street1 varchar, r_street2 varchar, r_city varchar,
	      r_country_name varchar, r_phone varchar, r_country varchar,
	      r_postal_code varchar, r_state_province varchar)
as 
$$

declare
order_array json := v#>'{OrderArray, Order}';
item json;
t_jid int := jid;
t_oid varchar;
t_address_owner varchar;
t_name varchar;
t_address_id varchar;
t_external_address_id varchar;
t_street1 varchar;
t_street2 varchar;
t_city varchar;
t_country_name varchar;
t_phone varchar;
t_country varchar;
t_postal_code varchar;
t_state_province varchar;

begin

for item in select * from json_array_elements(order_array)
    loop
	t_oid = item#>>'{OrderID}';
	t_address_owner = item#>>'{ShippingAddress, AddressOwner}';
	t_name = item#>>'{ShippingAddress, Name}';
	t_address_id = item#>>'{ShippingAddress, AddressID}';
	t_external_address_id = item#>>'{ShippingAddress, 
                                         ExternalAddressID}';

	t_street1 = item#>>'{ShippingAddress, Street1}';
	t_street2 = item#>>'{ShippingAddress, Street2}';
	t_city = item#>>'{ShippingAddress, CityName}';
	t_country_name = item#>>'{ShippingAddress, CountryName}';
	t_phone = item#>>'{ShippingAddress, Phone}';
	t_country = item#>>'{ShippingAddress, Country}';
	t_postal_code = item#>>'{ShippingAddress, PostalCode}';
	t_state_province = item#>>'{ShippingAddress, 
                                    StateOrProvince}';

	return query values (t_oid, t_address_owner, t_name, 
		t_address_id, t_external_address_id, t_street1,
		t_street2, t_city, t_country_name, t_phone, t_country,                t_postal_code, t_state_province);

end loop;

end;
$$ language plpgsql;

-----------------

create or replace function ebay_orders.insert_ack (jid int, v json)
returns table (r_jid int, r_ack varchar)
as
$$

declare
t_jid int := jid;
t_ack varchar := v#>>'{Ack}';

begin
	return query values (t_jid, t_ack);
end;
$$ language plpgsql;

-- create or replace function ebay_orders.insert_order_array (jid int, v json)
-- return table 
-- as
-- $$

-- declare 
-- json_length int;

-- t_seller_email varchar;
-- t_integrated_credit_card_enabled bool;
-- t_payment_hold_status varchar;

-- t_actual_shipping_currency varchar;
-- t_actual_shipping_cost numeric;
-- t_transaction_site_id varchar;
-- t_actual_handling_currency varchar;
-- t_actual_handling_cost numeric;
-- t_transaction_currency_id varchar;
-- t_transaction_price numeric;

-- t_quantity_purchased int;

-- t_total_tax_currency varchar;
-- t_total_tax_amount numeric;
-- t_tax_amount_currency_id varchar;
-- t_tax_amount numeric;
-- t_tax_imposition varchar;
-- t_tax_description varchar;

-- t_item_id varchar;
-- t_condition_id varchar;
-- t_condition_display_name varchar;
-- t_site varchar;
-- t_listing_title varchar;
-- t_listing_platform varchar;
-- t_listing_creation_date timestamp;
-- t_buyer_email varchar;
-- t_transaction_id bigint;
-- t_order_line_id varchar;
-- t_shipping_carrier varchar;
-- t_shipping_tracking varchar;
-- t_selling_manager_sales_record int;
-- t_created_time timestamp;
-- t_currency_id varchar;
-- t_checkout_status varchar;
-- t_payment_method varchar;
-- t_last_modified_time timestamp;
-- t_ebay_payment_status varchar;
-- t_integrated_merchant_credit_card_enabled bool;
-- t_get_it_fast bool;
-- t_selling_manager_sales_record_number int;
-- t_shipping_time_max int;
-- t_shipping_service_currency varchar;
-- t_shipping_service_cost numeric;
-- t_shipping_service_priority varchar;
-- t_shipping_service varchar;
-- t_expedited_shipping bool;
-- t_shipping_time_min int;
-- t_sales_tax_percent numeric;
-- t_shipping_included_in_tax bool;
-- t_shipping_sales_tax_currency varchar;

-- t_sales_tax_amount numeric;
-- t_sales_tax_state varchar;
-- t_sales_tax_percent numeric;

