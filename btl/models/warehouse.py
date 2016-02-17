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
        where lower(warehouse_name) = $${0}$$;
        """.format(wh2))
    a = dbconn.cur.fetchall()
    return a

def validate_warehouse(wh):
    wh2 = wh.replace("-", " ").lower()
    dbconn.cur.execute(
        """
        select warehouse_name,
        replace(lower(warehouse_name), ' ', '-')
        from warehouse.warehouses
        where lower(warehouse_name) = $${0}$$;
        """.format(wh2))
    a = dbconn.cur.fetchall()
    warehouse_name = [i[0] for i in a]
    warehouse_lower = [i[1] for i in a]
    try:
        return warehouse_name[0], warehouse_lower[0]
    except:
        return None, None

def valid_warehouses():
    dbconn.cur.execute(
        """
        select warehouse_name,
        lower(warehouse_name)
        from warehouse.warehouses
        order by warehouse_name;
        """)
    a = dbconn.cur.fetchall()
    return a

def pallet_locations(wh):
    wh2 = wh.replace("-", " ").lower()
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
        where lower(warehouse_name) = $${0}$$
        order by pallet_location_id;
        """.format(wh2))
    a = dbconn.cur.fetchall()
    return a

def warehouse_information(wh):
    wh2 = wh.replace("-", " ").lower()
    dbconn.cur.execute(
        """
        select warehouse_name, warehouse_street_address, 
               warehouse_state, warehouse_zip, 
               warehouse_country, warehouse_type
        from warehouse.warehouses
        where lower(warehouse_name) = $${0}$$;
        """.format(wh2))
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
