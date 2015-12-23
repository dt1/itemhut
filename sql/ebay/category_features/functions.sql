create or replace function ebay_category_features.f_default_payment_methods
       	  	  	   (v json)
returns table (r_payment_method varchar)
as
$$

declare
payment_method_array json := v#>'{SiteDefaults,PaymentMethod}';
item varchar;
t_payment_method varchar;

begin
for item in select * from json_array_elements(payment_method_array)
loop
	t_payment_method = trim(both '"' from item);
	return query values (t_payment_method);
end loop;
end;
$$ language plpgsql;

--------------------

create or replace function
ebay_category_features.f_default_gallery_feature_durations
       	  	  	   (v json)
returns table (r_duration varchar)
as
$$

declare
duration_array json
        := v#>>'{SiteDefaults,GalleryFeaturedDurations,Duration}';
item varchar;
t_duration varchar;

begin
for item in select * from json_array_elements(duration_array)
loop
	t_duration = trim(both '"' from item);
	return query values (t_duration);
end loop;
end;
$$ language plpgsql;

--------------------------

create or replace function ebay_category_features.f_default_listing_durations
       	  	  	                          (v json)
returns table (r_duration_type varchar, r_duration_value int)
as
$$

declare
duration_array json := v#>'{SiteDefaults,ListingDuration}';
item json;
t_type varchar;
t_value int;

begin
for item in select * from json_array_elements(duration_array)
loop
	t_type = item#>>'{_type}';
	t_value = item#>>'{value}';
	return query values (t_type, t_value);
end loop;
end;
$$ language plpgsql;

------------------------------

create or replace function ebay_category_features.f_default_category_groups
							(v json)
returns table (r_key varchar, r_value varchar)
as
$$

declare
category_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value varchar;

begin
for k, v in select key, value
    	    from json_each_text((category_array))
	    where value in
	    	  (select groups
		  from ebay_constraints.category_groups)

loop
	t_key = k;
	t_value = v;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;

------------------------------

create or replace function ebay_category_features.f_default_category_dis_en_abled
							(v json)
returns table (r_key varchar, r_value varchar)
as
$$

declare
category_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value varchar;

begin
for k, v in select key, value
    	    from json_each_text((category_array))
	    where value in
	    	  (select dis_en_abled
		  from ebay_constraints.dis_en_abled)

loop
	t_key = k;
	t_value = v;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;

------------------------------

create or replace function ebay_category_features.f_default_category_tf
							(v json)
returns table (r_key varchar, r_value varchar)
as
$$

declare
category_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value varchar;

begin
for k, v in select key, value
    	    from json_each_text((category_array))
	    where value in
	    	  (select tf
		  from constraints.tf)

loop
	t_key = k;
	t_value = v;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;

---------------------------

create or replace function ebay_category_features.f_default_category_subscriptions
							(v json)
returns table (r_key varchar, r_value varchar)
as
$$

declare
category_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value varchar;

begin
for k, v in select key, value
    	    from json_each_text((category_array))
	    where value in
	    	  (select subscription
		  from ebay_constraints.subscriptions)

loop
	t_key = k;
	t_value = v;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;

-----------------------------

create or replace function ebay_category_features.f_default_counts (v json)
returns table (r_key varchar, r_value int)
as
$$
declare
count_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value int;

begin
for k, v in select key, value
from json_each_text((count_array))
where value not in
	(select groups
	from ebay_constraints.category_groups
	union
	select dis_en_abled
	from ebay_constraints.dis_en_abled
	union
	select tf
	from constraints.tf
	union
	select subscription
	from ebay_constraints.subscriptions)
and value = '0'

loop
	t_key = k;
	t_value = 0;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;

-------------------------------

create or replace function ebay_category_features.f_default_prices (v json)
returns table (r_key varchar, r_value numeric)
as
$$
declare
price_array json := v#>'{SiteDefaults}';
k varchar;
v varchar;
t_key varchar;
t_value numeric;

begin
for k, v in select key, value
from json_each_text((price_array))
where value not in
	(select groups
	from ebay_constraints.category_groups
	union
	select dis_en_abled
	from ebay_constraints.dis_en_abled
	union
	select tf
	from constraints.tf
	union
	select subscription
	from ebay_constraints.subscriptions)
and value = '0.0'

loop
	t_key = k;
	t_value = 0.0;
	return query values (t_key, t_value);
end loop;
end;
$$ language plpgsql;
