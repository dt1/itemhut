create schema ebords;

create table ebords.json_insert (
  jid serial primary key,
  v json
);

create table ebords.jid_order_id_lut (
       jid int,
       order_id varchar unique,
       primary key (jid, order_id),
       foreign key (jid) references ebords.json_insert (jid)
);

create table ebords.order_id_transaction_array_id_lut (
       order_id varchar,
       transaction_array_id varchar,
       primary key (transaction_array_id),
       foreign key (order_id)
       	       references ebords.jid_order_id_lut (order_id)
);

create table ebords.ack (
  jid int primary key,
  ack varchar,
  foreign key (jid) references ebords.json_insert (jid)
);

create table ebords.buyer_info (
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
  foreign key (order_id) references ebords.jid_order_id_lut (order_id)
);

create table ebords.errors (
  jid int,
  severity_code varchar,
  error_parameters_id varchar,
  error_parameters_value varchar,
  error_code varchar,
  long_message varchar,
  error_classification varchar,
  short_message varchar,
  primary key (error_parameters_value),
  foreign key (jid) references ebords.json_insert (jid)
);

create table ebords.timestamps (
	jid int primary key,
	ebay_timestamp timestamp,
	system_timestamp timestamp default now(),
	foreign key (jid) references ebords.json_insert (jid)
); 



-- Item Condition ID
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, ConditionID}'
from ebords.json_insert;


-- Item Condition ID
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, ConditionDisplayName}'
from ebords.json_insert;


-- Site
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, Site}'
from ebords.json_insert;

-- Listing Title
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, Title}'
from ebords.json_insert;

-- Sale Platform
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Platform}'
from ebords.json_insert;


-- Listing Creation Date
-- timestamp (?)
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, CreatedDate}'
from ebords.json_insert;

-- Max Shipping Time (in days?)
-- int
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingTimeMax}'
from ebords.json_insert;

-- Shipping Currency
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingServiceCost, _currencyID}'
from ebords.json_insert;

-- Shipping Value
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingServiceCost, value}'
from ebords.json_insert;

-- Shipping Priority
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingServicePriority}'
from ebords.json_insert;

-- Shipping Service
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingService}'
from ebords.json_insert;

-- Expedited Service
-- boolean
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ExpeditedService}'
from ebords.json_insert;

-- "minimum" shipping time
-- int
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, ShippingServiceOptions, ShippingTimeMin}'
from ebords.json_insert;

-- Sales Tax Percent
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SalesTax, SalesTaxPercent}'
from ebords.json_insert;


-- Shipping Included in Tax
-- boolean
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SalesTax, ShippingIncludedInTax}'
from ebords.json_insert;

-- Shipping Sales Tax Currency
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SalesTax, SalesTaxAmount, _currencyID}'
from ebords.json_insert;

-- Sales Tax Amount
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SalesTax, SalesTaxAmount, value}'
from ebords.json_insert;


-- Sales Tax State
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SalesTax, SalesTaxState}'
from ebords.json_insert;


----------------------------

-- Item ID
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Item, ItemID}'
from ebords.json_insert;

-- create table ebords.product_details (
--        order_id varchar primary key,
--        item_id varchar,
       


create trigger process_json_orders
after insert on ebords.json_insert
for each row
execute procedure ebords.process_orders();
