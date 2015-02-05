create or replace function ebay_category.f_version_info (v json)
returns table (r_version int, r_category_count int,
	       r_update_time timestamp, r_download_time timestamp,
	       r_ack varchar)
as
$$

declare
t_version int = v#>>'{Version}';
t_category_count int = v#>>'{CategoryCount}';
t_update_time timestamp = v#>>'{UpdateTime}';
t_download_time timestamp =  v#>>'{Timestamp}';
t_ack varchar = v#>>'{Ack}';

begin

return query values (t_version, t_category_count, t_update_time,
       	            t_download_time, t_ack);

end;
$$ language plpgsql;

----------------------

create or replace function ebay_category.f_categories (v json)
returns table (r_category_id int, r_category_name varchar,
	       r_category_level int, r_auto_pay_enabled boolean,
	       r_best_offer_enabled boolean, r_category_parent_id int,	       r_leaf_category boolean)
as
$$

declare
category_array json := v#>'{CategoryArray, Category}';
item json;
t_category_id int;
t_category_name varchar;
t_category_level int;
t_auto_pay_enabled boolean;
t_best_offer_enabled boolean;
t_category_parent_id int;
t_leaf_category boolean;

begin
for item in select * from json_array_elements(category_array)
loop
	t_category_id = item#>>'{CategoryID}';
	t_category_name = item#>>'{CategoryName}';
	t_category_level =item#>>'{CategoryLevel}';
	t_auto_pay_enabled = item#>>'{AutoPayEnabled}';
	t_best_offer_enabled = item#>>'{BestOfferEnabled}';
	t_category_parent_id = item#>>'{CategoryParentID}';
	t_leaf_category = item#>>'{LeafCategory}';

	return query values (t_category_id, t_category_name,
	       	     	     t_category_level, t_auto_pay_enabled,
			    t_best_offer_enabled, t_category_parent_id,
			    t_leaf_category);

end loop;
end;
$$ language plpgsql;
