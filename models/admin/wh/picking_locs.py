# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_pickinglocs_list(wh):
    dbconn.cur.execute(
        """
        select picking_location_id, picking_location_name, sku, upc
        from warehouse.picking_locations wpl
        full join product.sku_upc
        using (upc)
        where (sku_type = 'regular' 
               or sku_type is null)
        and exists
        (select *
        from warehouse.warehouse_picking_loc
        where picking_location_id = wpl.picking_location_id
        and warehouse_id = %s);
        """, [wh])
    a = dbconn.cur.fetchall()
    return a


def select_pickingloc_info(plid):
    dbconn.cur.execute(
        """
        select picking_location_id, picking_location_name, sku, upc
        from warehouse.picking_locations wpl
        left join product.sku_upc
        using (upc)
        where (sku_type = 'regular' 
               or sku_type is null)
        and picking_location_id = %s::int;
        """, [plid])
    a = dbconn.cur.fetchall()
    return a

def update_pickingloc_info(wh, plid, old_plname, new_plname, upc):
    if old_plname != new_plname:
        dbconn.cur.execute(
            """
            select *
            from warehouse.picking_locations wpp
            where exists
            (select *
            from warehouse.warehouse_picking_loc
            where picking_location_id = wpp.picking_location_id
            and warehouse_id = %s)
            and picking_location_name = %s;
            """, [wh, new_plname])
        a = dbconn.cur.fetchall()
        if a:
            return True

    dbconn.cur.execute(
        """
        begin;
        update warehouse.picking_locations
        set picking_location_name = %s,
        upc = %s::bigint
        where picking_location_id = %s::int;
        """, [new_plname, upc, plid])

def insert_picking_location(wh, locname, upc):
        dbconn.cur.execute(
            """
            select *
            from warehouse.picking_locations wpp
            where exists
            (select *
            from warehouse.warehouse_picking_loc
            where picking_location_id = wpp.picking_location_id
            and warehouse_id = %s)
            and picking_location_name = %s;
            """, [wh, locname])
        a = dbconn.cur.fetchall()
        if a:
            return True

        dbconn.cur.execute(
            """
            with new_plid (picking_location_id) as 
                (insert into warehouse.picking_locations
                     (picking_location_name, upc)
                 values(%s, %s::bigint)
                 returning picking_location_id)
            insert into warehouse.warehouse_picking_loc
                (warehouse_id, picking_location_id)
            select %s, picking_location_id
            from new_plid;
            """, [locname, upc, wh])
          
            
def bulk_load_pickinglocs(locfile, wh):
    dbconn.cur.execute(
        """
        create temp table pls (
        picking_location_name varchar, 
        upc bigint);

        copy pls (picking_location_name, upc)
        from %s csv header;

        with tpls (picking_location_id) as
             (insert into warehouse.picking_locations 
                   (picking_location_name, upc)
              select picking_location_name, upc
              from pls pls
              where not exists
                    (select *
                     from warehouse.picking_locations
                     join warehouse.warehouse_picking_loc
                     using (picking_location_id)
                     where picking_location_name = 
                           pls.picking_location_name
                     and warehouse_id = %s)
             returning picking_location_id)
        insert into warehouse.warehouse_picking_loc 
              (warehouse_id, picking_location_id)
        select %s, picking_location_id
        from tpls;
        
        drop table pls;
        """, [locfile, wh, wh])
