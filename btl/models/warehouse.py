import sys
sys.path.append("/omark/pydb")
import dbconn

def valid_warehouses():
    dbconn.cur.execute(
        """
        select warehouse_name
        from warehouse.warehouses
        order by warehouse_name;
        """)
    a = dbconn.cur.fetchall()
    return a

def pallet_locations(wh):
    wh2 = wh.replace("-", " ").lower()
    dbconn.cur.execute(
        """
        select pallet_location_id, pallet_location_name, pallet_id
        from warehouse.warehouses
        join warehouse.warehouse_pallet_loc
        using (warehouse_id)
        join warehouse.pallet_locations
        using (pallet_location_id)
        left join warehouse.pallet_palletloc
        using (pallet_location_id)
        where lower(warehouse_name) = $${0}$$
        order by pallet_location_id;
        """.format(wh2))
    a = dbconn.cur.fetchall()
    return a
