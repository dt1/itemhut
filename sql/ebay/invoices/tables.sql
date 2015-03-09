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







select jsonb_each(v)
from ebay_invoices.json_insert;

select v#>'{Ack}'
from ebay_invoices.json_insert;
