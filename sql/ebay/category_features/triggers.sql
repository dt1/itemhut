create or replace function ebay_category_features.process_category_defaults ()
returns trigger
as
$$
declare
n_v json := new.v;

begin
        insert into ebay_category_features.default_payment_methods
	       	                                   (payment_method)
	select r_payment_method
	from ebay_category_features.f_default_payment_methods (n_v);

	insert into ebay_category_features.default_gallery_feature_durations
	            (gallery_feature_duration)
	select r_duration
	from ebay_category_features.f_default_gallery_feature_durations
	           (n_v);


	insert into ebay_category_features.default_listing_durations
	            (duration_type, duration_value)
        select r_duration_type, r_duration_value
	from ebay_category_features.f_default_listing_durations (n_v);


	insert into ebay_category_features.default_category_groups (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_category_groups (n_v);

	insert into ebay_category_features.default_category_dis_en_abled (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_category_dis_en_abled (n_v);

	insert into ebay_category_features.default_category_tf (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_category_tf (n_v);

	insert into ebay_category_features.default_category_subscriptions (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_category_subscriptions (n_v);

	insert into ebay_category_features.default_counts (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_counts (n_v);

	insert into ebay_category_features.default_prices (key, value)
	select r_key, r_value
	from ebay_category_features.f_default_prices (n_v);


return new;
end;
$$ language plpgsql;

create trigger process_json_category_defaults
after insert
on ebay_category_features.json_insert
for each row
execute procedure ebay_category_features.process_category_defaults();
