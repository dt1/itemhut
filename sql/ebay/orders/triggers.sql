create or replace function ebay_orders.process_orders ()
returns trigger as
$$
declare
n_jid int := new.jid;
n_v json := new.v;

begin
	insert into ebay_orders.jid_order_id_lut (jid, order_id)
	select r_jid, r_oid
	from ebay_orders.create_jid_oid_lut (n_jid, n_v);

	insert into ebay_orders.order_id_transaction_array_id_lut
	            (order_id, transaction_array_id)
        select r_oid, r_tid
	from ebay_orders.create_oid_tid_lut (n_v);


	insert into ebay_orders.errors
	       (jid, severity_code, error_parameters_id, 
	       error_parameters_value, error_code, long_message, 
	       error_classification, short_message)
	select r_jid, r_scode, r_epid, r_epval, r_ecode, r_longm,
	       r_errclass, r_shortm
	from ebay_orders.insert_order_errors(n_jid, n_v);
	
	insert into ebay_orders.timestamps (jid, ebay_timestamp,
	                               system_timestamp)
	select r_jid, r_ebay_timestamp, r_system_timestamp
	from ebay_orders.insert_timestamps (n_jid, n_v);

	insert into ebay_orders.buyer_info
	       (order_id, address_owner, name, address_id, 
	       external_address_id, street1, street2, city, country_name, 
	       phone, country, postal_code, state_province)
	select r_oid, r_address_owner, r_name, r_address_id, 
	       r_external_address_id, r_street1, r_street2, r_city,
	       r_country_name, r_phone, r_country, r_postal_code, 
	       r_state_province
	from ebay_orders.insert_buyer_info(n_jid, n_v);

	insert into ebay_orders.ack (jid, ack)
	select r_jid, r_ack
	from ebay_orders.insert_ack(n_jid, n_v);

        

return new;
end;
$$ language plpgsql;

create trigger process_json_orders
after insert on ebay_orders.json_insert
for each row
execute procedure ebay_orders.process_orders();
