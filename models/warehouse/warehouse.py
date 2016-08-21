# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def add_full_pallet_to_pickingloc(wh, pid):
        a = dcur.execute(
            """
            begin;
            with upc_count(upc, total) as
                (select upc, case_qty * piece_qty * box_qty total
                 from warehouse.pallet_palletloc
                 left join warehouse.pallet_case
                 using (pallet_id)
	         left join warehouse.case_box
                 using (case_id)
                 left join warehouse.boxes
                 using (box_id)
                 left join product.sku_upc
                 using (upc)
                 where pallet_id = %s::int
                 group by upc, total, pallet_id)
            update warehouse.picking_locations wpl
            set qty = qty + total
            from
            (select upc, total
            from upc_count) t1
            where wpl.upc = t1.upc
            and wpl.picking_location_id in
            (select picking_location_id
            from warehouse.warehouse_picking_loc
            where warehouse_id = %s);

            delete from warehouse.pallets
            where pallet_id = %s::int;
            commit;
            """, [pid, wh, pid])

def running_inventory(wh):
    a = dcur.execute(
        """
        select sku, upc,
        sum(coalesce(box_qty * piece_qty * case_qty, 0)
            + coalesce(qty, 0))
        from warehouse.warehouses
        join warehouse.warehouse_pallet_loc
        using (warehouse_id)
        join warehouse.pallet_locations
        using (pallet_location_id)
        join warehouse.pallet_palletloc
        using (pallet_location_id)
        join warehouse.pallet_case
        using (pallet_id)
        join warehouse.case_box
        using (case_id)
        join warehouse.boxes
        using (box_id)
        join product.sku_upc
        using (upc)
        right join warehouse.picking_locations
        using (upc)
        where warehouse_id = %s
        group by sku, upc;
        """, [wh])
    a = dcur.fetchall()
    return a

def validate_warehouse(wh):
    a = dcur.execute(
        """
        select warehouse_id, warehouse_name
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dcur.fetchall()
    try:
        return a
    except:
        return None

def valid_warehouses():
    a = dcur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_type
        from warehouse.warehouses
        order by warehouse_name;
        """)
    a = dcur.fetchall()
    return a

def select_pallet_locations(wh):
    a = dcur.execute(
        """
        select pallet_location_id, pallet_location_name, pallet_id,
        string_agg(sku || '/' || upc || ' cases(' || case_qty || ')', ';;'),
	string_agg(sku || '(' || (case_qty * piece_qty * box_qty)::varchar || ')', ';;')
        from warehouse.warehouses
        join warehouse.warehouse_pallet_loc
        using (warehouse_id)
        join warehouse.pallet_locations
        using (pallet_location_id)
        left join warehouse.pallet_palletloc
        using (pallet_location_id)
        left join warehouse.pallet_case
        using (pallet_id)
	left join warehouse.case_box
        using (case_id)
        left join warehouse.boxes
        using (box_id)
        left join product.sku_upc
        using (upc)
        where warehouse_id = %s
        group by pallet_location_id, pallet_location_name, pallet_id
        order by pallet_location_id;
        """, [wh])
    a = dcur.fetchall()
    return a

def warehouse_information(wh):
    a = dcur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_street_address,
               warehouse_state, warehouse_zip,
               warehouse_country, warehouse_type
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dcur.fetchall()
    return a

def get_case_boxes():
    a = dcur.execute(
        """
        select case_id, box_id, box_qty, piece_qty, upc,
               sku, product_name, piece_qty * box_qty
        from warehouse.case_box
        join warehouse.cases
        using (case_id)
        join warehouse.boxes
        using (box_id)
        left join product.sku_upc
        using (upc)
        left join product.descriptions
        using (sku);        """)
    a = dcur.fetchall()
    return a

def valid_warehouse_list():
    wh_query = valid_warehouses()
    warehouse_name = [i[0] for i in wh_query]
    warehouse_lower = [i[1] for i in wh_query]
    return warehouse_name, warehouse_lower

def select_picking_locations(wh):
    a = dcur.execute(
        """
        select picking_location_id, picking_location_name, sku, upc,
               qty
        from warehouse.warehouses
        join warehouse.warehouse_picking_loc
        using(warehouse_id)
        join warehouse.picking_locations
        using(picking_location_id)
        join product.sku_upc
        using (upc)
        where warehouse_id = %s;
        """, [wh])
    a = dcur.fetchall()
    return a

def insert_picking_location(wh, picking_location, sku, qty):
    a = dcur.execute(
        """
        select warehouse_id, warehouse_name, picking_location_name
        from warehouse.warehouses
        join warehouse.warehouse_picking_loc
        using(warehouse_id)
        join warehouse.picking_locations
        using(picking_location_id)
        where warehouse_id = %s
        and picking_location_name = %s;
        """, [wh, picking_location])
    a = dcur.fetchall()
    if a:
        return "{0} already exists in {1} warehouse".format(picking_location, a[0][1])

    else:
        a = dcur.execute(
            """
            with new_picking_location (new_location_id) as
	    (insert into warehouse.picking_locations
	    (picking_location_name, sku, qty)
	    values (%s, %s, %s::int)
	    returning picking_location_id
	    )
            insert into warehouse.warehouse_picking_loc
	    (warehouse_id, picking_location_id)
            select %s, new_location_id
            from new_picking_location;
            """, [picking_location, sku, qty, wh])
    return None

def select_picking_location_info(pid):
    a = dcur.execute(
        """
        select picking_location_name, upc, qty
        from warehouse.picking_locations
        where picking_location_id = %s::int;
        """, [pid])
    a = dcur.fetchall()
    return a

def update_picking_location_info(pid, picking_location, sku, qty):
    a = dcur.execute(
        """
        begin;
        update warehouse.picking_locations
        set picking_location_name = %s,
        upc = %s::bigint,
        qty = %s::int
        where picking_location_id = %s::int;
        commit;
        """, [picking_location, sku, qty, pid])

def select_sku_upc_not_in_3pl(wh):
    a = dcur.execute(
        """
        select sku, upc
        from product.sku_upc psu
        where not exists
	(select *
	from warehouse.warehouse_picking_loc
	join warehouse.picking_locations
	using (picking_location_id)
	where warehouse_id = %s
	and psu.upc = upc);
        """, [wh])
    a = dcur.fetchall()
    return a

def insert_3pl_product(wh, upc, qty):
    a = dcur.execute(
        """
        begin;
        with new_loc (picking_location_id) as
	    (insert into warehouse.picking_locations
		(picking_location_name,
	         upc, qty)
	     values (now()::varchar, %s::bigint, %s::int)
	     returning picking_location_id)
        insert into warehouse.warehouse_picking_loc
	     (warehouse_id, picking_location_id)
        select %s, picking_location_id
        from new_loc;
        commit;
        """, [upc, qty, wh])

def select_3pl_running_inventory(wh):
    a = dcur.execute(
        """
        select sku, upc, qty
        from warehouse.warehouse_picking_loc
        join warehouse.picking_locations
        using (picking_location_id)
        join product.sku_upc
        using (upc)
        where warehouse_id = %s;
        """, [wh])
    a = dcur.fetchall()
    return a

def select_3pl_running_inventory_sku(wh, sku):
    a = dcur.execute(
        """
        select sku, upc, qty, picking_location_id
        from warehouse.warehouse_picking_loc
        join warehouse.picking_locations
        using (picking_location_id)
        join product.sku_upc
        using (upc)
        where warehouse_id = %s
        and sku = %s;
        """, [wh, sku])
    a = dcur.fetchall()
    return a

def update_3pl_running_inventory(picking_location_id, qty):
    a = dcur.execute(
        """
        begin;
        update warehouse.picking_locations
        set qty = %s::int
        where picking_location_id = %s;
        commit;
        """, [qty, picking_location_id])


def select_case_boxes(pid):
    a = dcur.execute(
        """
        select case_id, sku, upc, box_qty, piece_qty
        from warehouse.cases
        join warehouse.case_box
        using (case_id)
        join warehouse.boxes
        using (box_id)
        join product.sku_upc
        using (upc)
        where case_id not in
        (select case_id
        from warehouse.pallet_case
        where pallet_id = %s);
        """, [pid])
    a = dcur.fetchall()
    return a

def generate_pallet_id(wh):
    a = dcur.execute(
        """
        begin;
        with new_pl (pallet_location_id) as
	      (insert into warehouse.pallet_locations
		    (pallet_location_name)
	       values ('staged')
	       returning pallet_location_id)
	       ,
             new_pallet (pallet_id) as
	       (insert into warehouse.pallets (pallet_id)
		values (default)
	        returning pallet_id)
	        ,
              new_wh_palletloc as
                (insert into warehouse.warehouse_pallet_loc
		     (warehouse_id, pallet_location_id)
	         select %s, pallet_location_id
	         from new_pl)
        insert into warehouse.pallet_palletloc
             (pallet_location_id, pallet_id)
        select pallet_location_id, pallet_id
        from new_pl, new_pallet
        returning pallet_id;
        """, [wh])
    a = dcur.fetchall()
    a = dcur.execute(
        """
        commit;
        """)
    return a

def select_pallet_info(pid):
    a = dcur.execute(
        """
        select case_id, sku, upc, box_qty, piece_qty, case_qty,
        coalesce(pallet_location_name, 'Empty'), pallet_location_id
        from warehouse.pallet_palletloc
        join warehouse.pallet_locations
        using (pallet_location_id)
	join warehouse.pallets
        using (pallet_id)
	left join warehouse.pallet_case
        using (pallet_id)
	left join warehouse.case_box
	using (case_id)
	left join warehouse.boxes
	using (box_id)
        left join product.sku_upc
        using (upc)
        where pallet_id = %s::int;
        """, [pid])
    a = dcur.fetchall()
    return a

def insert_pallet_case(pid, cid, qty):
    a = dcur.execute(
        """
        begin;
        insert into warehouse.pallet_case
             (pallet_id, case_id, case_qty)
        values (%s::int, %s::int, %s::int);
        commit;
        """, [pid, cid, qty])

def delete_pallet_case(pid, cid):
    a = dcur.execute(
        """
        begin;
        delete from warehouse.pallet_case
        where pallet_id = %s::int
        and case_id = %s::int;
        commit;
        """, [pid, cid])

def select_all_running_inventory():
    a = dcur.execute(
        """
        select sku, upc, coalesce(total1, 0) + coalesce(total2, 0)
from
        (select sku, upc, qty total1
        from warehouse.warehouse_picking_loc
        join warehouse.picking_locations
        using (picking_location_id)
        join product.sku_upc
        using (upc)) t1

	full join

        (select sku, upc, sum(box_qty * piece_qty * case_qty) total2
        from warehouse.warehouses
        join warehouse.warehouse_pallet_loc
        using (warehouse_id)
        join warehouse.pallet_locations
        using (pallet_location_id)
        join warehouse.pallet_palletloc
        using (pallet_location_id)
        join warehouse.pallet_case
        using (pallet_id)
        join warehouse.case_box
        using (case_id)
        join warehouse.boxes
        using (box_id)
        join product.sku_upc
        using (upc)
        group by sku, upc) t2
        using (sku, upc);
        """)
    a = dcur.fetchall()
    return a

def select_outbound_orders(wh):
        a = dcur.execute(
                """
                select internal_order_id, market_order_id, 
                array_agg(sku  || ' (' || sku_qty || ')'),
                ship_by_date
                from orders.market_orders
                join orders.shipto
                using (internal_order_id)
                join orders.shipto_marketplace_skus
                using (shipto_id)
                join marketplace.msku_sku
                using (marketplace_sku)
                group by internal_order_id, market_order_id, 
                         ship_by_date
                order by internal_order_id;
                """)
        a = dcur.fetchall()
        return a
        
def select_order_to_scan(oid):
        a = dcur.execute(
                """
                select internal_order_id, market_order_id, 
                array_agg(sku  || ' (' || sku_qty || ')'),
                ship_by_date
                from orders.market_orders
                join orders.shipto
                using (internal_order_id)
                join orders.shipto_marketplace_skus
                using (shipto_id)
                join marketplace.msku_sku
                using (marketplace_sku)
                where internal_order_id = %s::int
                group by internal_order_id, market_order_id, 
                         ship_by_date
                """, [oid])
        a = dcur.fetchall()
        return a
