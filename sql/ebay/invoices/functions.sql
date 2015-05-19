create or replace function ebay_invoices.create_jid_tid_lut
       (jid int, v varchar)
returns table (r_jid int, r_tid bigint)
as
$$
begin

t_jid int = jid;

--------------------------------

create or replace function ebay_invoices.process_invoices(v jsonb)
returns table (
	r_account_details_entry_type varchar,
	r_date date,
	r_memo varchar,
	r_vat_percent numeric,
	r_net_detail_amount_currency varchar,
	r_net_detail_amount_value numeric,
	r_item_id bigint,
	r_gross_detail_amount_currency varchar,
	r_gross_detail_amount_value numeric,
	r_order_line_item_id varchar,
	r_description varchar,
	r_ref_number bigint,
	r_transaction_id bigint,
	r_title varchar,
	r_received_top_rated_discount varchar)
 
as
$$

declare
jjarray jsonb = v#>>'{AccountEntries, AccountEntry}';
rr varchar;
item jsonb;
t_account_details_entry_type varchar;
t_date date;
t_memo varchar;
t_vat_percent numeric;
t_net_detail_amount_currency varchar;
t_net_detail_amount_value numeric;
t_item_id bigint;
t_gross_detail_amount_currency varchar;
t_gross_detail_amount_value numeric;
t_order_line_item_id varchar;
t_description varchar;
t_ref_number bigint;
t_transaction_id bigint;
t_title varchar;
t_received_top_rated_discount varchar;

begin

for item in select * from jsonb_array_elements(jjarray)
	loop
	t_account_details_entry_type := item#>>'{AccountDetailsEntryType}';
	t_date := item#>>'{Date}';
	t_memo := item#>>'{Memo}';
	t_vat_percent := item#>>'{VATPercent}';
	t_net_detail_amount_currency :=
	                     item#>>'{NetDetailAmount, currency_id}';
	t_net_detail_amount_value :=
	                     item#>>'{NetDetailAmount, value}';
        t_item_id := item#>>'{ItemID}';
	t_gross_detail_amount_currency :=
	                     item#>>'{GrossDetailAmount, currency_id}';
	t_gross_detail_amount_value :=
	                     item#>>'{GrossDetailAmount, value}';
	t_order_line_item_id := item#>>'{OrderLineItemID}';
	t_description := item#>>'{Description}';
	t_ref_number := item#>>'{RefNumber}';
	t_transaction_id := item#>>'{TransactionID}';
	t_title := item#>>'{Title}';
	t_received_top_rated_discount := item#>>'{ReceivedTopRatedDiscount}';

		return query values (
		t_account_details_entry_type,
		t_date,
		t_memo,
		t_vat_percent ,
		t_net_detail_amount_currency,
		t_net_detail_amount_value,
		t_item_id,
		t_gross_detail_amount_currency,
		t_gross_detail_amount_value,
		t_order_line_item_id,
		t_description,
		t_ref_number,
		t_transaction_id,
		t_title,
		t_received_top_rated_discount);

end loop;
end;
$$ LANGUAGE plpgsql;

------------

create or replace function ebay_invoices.insert_ack (jid int, v jsonb)
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

--------------------

create or replace function ebay_invoices.process_json ()
returns trigger
as
$$
declare
n_jid int := new.jid;
n_v jsonb := new.v;

begin
	insert into ebay_invoices.ack (jid, ack)
	select r_jid, r_ack
	from ebay_invoices.insert_ack (n_jid, n_v);

	insert into  ebay_invoices.invoices (
	account_details_entry_type,
	date,
	memo,
	vat_percent,
	net_detail_amount_currency,
	net_detail_amount_value,
	item_id,
	gross_detail_amount_currency,
	gross_detail_amount_value,
	order_line_item_id,
	description,
	ref_number,
	transaction_id,
	title,
	received_top_rated_discount)

	select 
	r_account_details_entry_type,
	r_date,
	r_memo,
	r_vat_percent ,
	r_net_detail_amount_currency,
	r_net_detail_amount_value,
	r_item_id,
	r_gross_detail_amount_currency,
	r_gross_detail_amount_value,
	r_order_line_item_id,
	r_description,
	r_ref_number,
	r_transaction_id,
	r_title,
	r_received_top_rated_discount

	from ebay_invoices.process_invoices (n_v);

return new;
end;
$$ language plpgsql;
