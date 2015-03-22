create trigger process_ebay_invoices
after insert on ebay_invoices.json_insert
for each row
execute procedure ebay_invoices.process_json ();
