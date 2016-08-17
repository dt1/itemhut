create schema ebay_invoices;

create table ebay_invoices.json_insert (
       jid serial primary key,
       v jsonb
);

create table ebay_invoices.ack (
       jid int,
       ack varchar,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.build (
       jid int,
       build varchar,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.version (
       jid int,
       version int,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.account_id (
       jid int,
       account_id varchar,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.time_stamp (
       jid int,
       time_stamp timestamp,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.valid_currency (
       currency varchar primary key
);

create table ebay_invoices.jid_transaction_id_lut (
       transaction_id bigint primary key,
       jid int,
       foreign key (jid) references ebay_invoices.json_insert (jid)
);

create table ebay_invoices.account_entry (
       transaction_id bigint primary key,
       date date,
       ref_number bigint,
       memo varchar,
       order_line_item_id varchar,
       title varchar,
       description varchar,
       account_details_entry_type varchar,
       vat_percent numeric,
       gross_detail_amount_currency varchar,
       gross_detail_amount_value numeric,
       net_detail_amount_currency varchar,
       net_detail_amount_value numeric,
       foreign key (net_detail_amount_currency)
       	       references ebay_invoices.valid_currency (currency),
       foreign key (gross_detail_amount_currency)
       	       references ebay_invoices.valid_currency (currency),
       foreign key (transaction_id)
       	       references ebay_invoices.jid_transaction_id_lut
	       		  (transaction_id)
);




select v#>'{AccountEntries, AccountEntry, 0}'
from ebay_invoices.json_insert where jid = 4;

select jsonb_array_length(v#>'{AccountEntries, AccountEntry}')
from ebay_invoices.json_insert where jid = 4;

select v#>'{AccountEntries, AccountEntry}'
from ebay_invoices.json_insert;

select v#>'{Ack}'
from ebay_invoices.json_insert;

delete from ebay_invoices.json_insert
where jid <> 1;

insert into ebay_invoices.json_insert (v)
select v
from ebay_invoices.json_insert;

------------------------

drop table ebay_invoices.invoices;


create table ebay_invoices.invoices (
account_details_entry_type varchar,
date date,
memo varchar,
vat_percent numeric,
net_detail_amount_currency varchar,
net_detail_amount_value numeric,
item_id bigint,
gross_detail_amount_currency varchar,
gross_detail_amount_value numeric,
order_line_item_id varchar,
description varchar,
ref_number bigint,
transaction_id bigint,
title varchar,
received_top_rated_discount varchar);

-----------------------
