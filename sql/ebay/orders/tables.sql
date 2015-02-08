drop schema ebay_orders cascade;

create schema ebay_orders;

create table ebay_orders.json_insert (
  jid serial primary key,
  v json
);

create table ebay_orders.jid_order_id_lut (
       jid int,
       order_id varchar unique,
       primary key (jid, order_id),
       foreign key (jid) references ebay_orders.json_insert (jid)
);

create table ebay_orders.order_id_transaction_array_id_lut (
       order_id varchar,
       transaction_array_id varchar,
       primary key (transaction_array_id),
       foreign key (order_id)
       	       references ebay_orders.jid_order_id_lut (order_id)
);

create table ebay_orders.ack (
  jid int primary key,
  ack varchar,
  foreign key (jid) references ebay_orders.json_insert (jid)
);

create table ebay_orders.buyer_info (
  order_id varchar primary key,
  address_owner varchar,
  name varchar,
  address_id varchar,
  external_address_id varchar,
  street1 varchar,
  street2 varchar,
  city varchar,
  country_name varchar,
  phone varchar,
  country varchar,
  postal_code varchar,
  state_province varchar,
  foreign key (order_id) references ebay_orders.jid_order_id_lut (order_id)
);

create table ebay_orders.errors (
  jid int,
  severity_code varchar,
  error_parameters_id varchar,
  error_parameters_value varchar,
  error_code varchar,
  long_message varchar,
  error_classification varchar,
  short_message varchar,
  primary key (error_parameters_value),
  foreign key (jid) references ebay_orders.json_insert (jid)
);

create table ebay_orders.timestamps (
	jid int primary key,
	ebay_timestamp timestamp,
	system_timestamp timestamp default now(),
	foreign key (jid) references ebay_orders.json_insert (jid)
); 


create table ebay_orders.transaction_shipping_details (
       transaction_array_id varchar,
       actual_shipping_cost numeric,
       actual_shipping_cost_currency_id varchar,
       actual_handling_cost numeric,
       actual_handling_cost_currency_id varchar,
       shipping_carrier_used varchar,
       shipment_tracking_number varchar,
       foreign key (transaction_array_id)
       ebay_orders.order_id_transaction_array_id_lut (transaction_array_id)
);

-- -- shipping currency 
-- -- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualShippingCost, _currencyID}'
-- from ebay_orders.json_insert;

-- -- shipping cost to buyer 
-- -- numeric
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualShippingCost, value}'
-- from ebay_orders.json_insert;


-- -- handling currency
-- -- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualHandlingCost, _currencyID}'
-- from ebay_orders.json_insert;

-- -- handling value
-- -- numeric
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualHandlingCost, value}'
-- from ebay_orders.json_insert;

-- -- Shipping Carrier
-- -- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ShippingDetails, ShipmentTrackingDetails, ShippingCarrierUsed}'
-- from ebay_orders.json_insert;

-- -- Shipping Tracking
-- -- varchar
-- select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ShippingDetails, ShipmentTrackingDetails, ShipmentTrackingNumber}'
-- from ebay_orders.json_insert;

create table ebay_orders.transaction_taxe_details (
       transaction_array_id varchar,
       tax_amount numeric,
       tax_amount_currency_id varchar,
       total_tax_amount numeric,
       total_tax_amount_currency_id varchar,
       tax_on_shipping_amount numeric,
       tax_on_shipping_amount_currency_id varchar,
       tax_on_handling_amount numeric,
       tax_on_handling_amount_currency_id varchar,
       imposition varchar,
       tax_description v
       foreign key (transaction_array_id)
       ebay_orders.order_id_transaction_array_id_lut (transaction_array_id)
);
