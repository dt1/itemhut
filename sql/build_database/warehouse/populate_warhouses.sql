\set wname 'B'
\set wname_s '\'' :wname '\'' 

with new_warehouse (warehouse_id) as
	(insert into warehouse.warehouses (warehouse_name)
	values	     
	(:wname_s)
	returning warehouse_id)
	,
	new_pallet (pallet_id) as
	(insert into warehouse.pallets (pallet_id)
	values
	(default)
	returning pallet_id)
	,
	new_pallet_location (pl_id) as
	(insert into warehouse.pallet_locations (pallet_id)
	 select pallet_id 
	 from new_pallet
	 returning pallet_location_id)

insert into warehouse.warehouse_pallet_loc (warehouse_id, pallet_location_id)
select new_warehouse.warehouse_id
,
new_pallet_location.pl_id
from new_warehouse, new_pallet_location;
