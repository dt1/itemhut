create or replace function ebay_category.process_categories ()
returns trigger
as
$$
declare
n_v json := new.v;
version_number int := new.v#>>'{Version}';

begin

-- if version_number not in
--    (select version
--    from ebcats.version_info)
-- then
	insert into ebay_category.version_info (version, category_count,
	       	    			 update_time,download_time, ack)
	select r_version, r_category_count, r_update_time,
	       r_download_time, r_ack
	from ebay_category.f_version_info (n_v);

	insert into ebay_category.categories (category_id, category_name,
	       	     	    	       category_level, auto_pay_enabled,
			    	       best_offer_enabled,
				       category_parent_id,
				       leaf_category)
        select r_category_id, r_category_name, r_category_level,
	       r_auto_pay_enabled, r_best_offer_enabled,
	       r_category_parent_id, r_leaf_category				from ebay_category.f_categories (n_v);
-- end if;
return new;
end;
$$language plpgsql;

create trigger process_json_categories
after insert
on ebay_category.json_insert
for each row
execute procedure ebay_category.process_categories();
