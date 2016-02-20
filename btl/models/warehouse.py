# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def running_inventory(wh):
    wh2 = wh.replace("-", " ").lower()
    dbconn.cur.execute(
        """
        select sku, box_qty * piece_qty
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
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def validate_warehouse(wh):
    dbconn.cur.execute(
        """
        select warehouse_id, warehouse_name
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    try:
        return a
    except:
        return None

def valid_warehouses():
    dbconn.cur.execute(
        """
        select warehouse_id, warehouse_name
        from warehouse.warehouses
        order by warehouse_name;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_pallet_locations(wh):
    dbconn.cur.execute(
        """
        select pallet_location_id, pallet_location_name, pallet_id, sku || ' boxes(' || box_qty || ')' info, piece_qty * box_qty total
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
        order by pallet_location_id;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def warehouse_information(wh):
    dbconn.cur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_street_address,
               warehouse_state, warehouse_zip, 
               warehouse_country, warehouse_type
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def get_case_boxes():
    dbconn.cur.execute(
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
    a = dbconn.cur.fetchall()
    return a

def valid_warehouse_list():
    wh_query = valid_warehouses()
    warehouse_name = [i[0] for i in wh_query]
    warehouse_lower = [i[1] for i in wh_query]
    return warehouse_name, warehouse_lower

def insert_pallet_location(warehouse_id, location_name):
    dbconn.cur.execute(
        """
        begin;
        with new_loc (pallet_location_id) as
	    (insert into warehouse.pallet_locations
             (pallet_location_name)
	     values (%s)
	     returning pallet_location_id
	     )
        insert into warehouse.warehouse_pallet_loc 
                    (warehouse_id, pallet_location_id)
        select %s, pallet_location_id
        from new_loc;
        commit;
        """, [location_name, warehouse_id])

def select_picking_locations(wh):
    dbconn.cur.execute(
        """
        select picking_location_id, picking_location_name, sku, qty
        from warehouse.warehouses
        join warehouse.warehouse_picking_loc 
        using(warehouse_id)
        join warehouse.picking_locations 
        using(picking_location_id)
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def insert_picking_location(wh, picking_location, sku, qty):
    dbconn.cur.execute(
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
    a = dbconn.cur.fetchall()
    if a:
        return "{0} already exists in {1} warehouse".format(picking_location, a[0][1])

    else:
        dbconn.cur.execute(
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
    dbconn.cur.execute(
        """
        select picking_location_name, sku, qty
        from warehouse.picking_locations
        where picking_location_id = %s::int;
        """, [pid])
    a = dbconn.cur.fetchall()
    return a

def update_picking_location_info(pid, picking_location, sku, qty):
    dbconn.cur.execute(
        """
        begin;
        update warehouse.picking_locations
        set picking_location_name = %s,
        sku = %s,
        qty = %s
        where picking_location_id = %s;
        commit;
        """, [picking_location, sku, qty, pid])
