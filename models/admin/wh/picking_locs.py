# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def select_pickinglocs_list(wh):
    a = dcur.execute(
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
        and warehouse_id = %(wh)s);
        """, {"wh": wh})
    a = dcur.fetchall()
    return a


def select_pickingloc_info(plid):
    a = dcur.execute(
        """
        select picking_location_id, picking_location_name, sku, upc
        from warehouse.picking_locations wpl
        left join product.sku_upc
        using (upc)
        where (sku_type = 'regular'
               or sku_type is null)
        and picking_location_id = %s::int;
        """, {"plid": plid})
    a = dcur.fetchall()
    return a

def update_pickingloc_info(wh, plid, old_plname, new_plname, upc):
    if old_plname != new_plname:
        a = dcur.execute(
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
        a = dcur.fetchall()
        if a:
            return True

    a = dcur.execute(
        """
        begin;
        update warehouse.picking_locations
        set picking_location_name = %(plname)s,
        upc = %(upc)s::bigint
        where picking_location_id = %(plid)s::int;
        """, {"plname": new_plname,
              "upc": upc,
              "plid": plid})

def insert_picking_location(d):
        a = dcur.execute(
            """
            select *
            from warehouse.picking_locations wpp
            where exists
            (select *
            from warehouse.warehouse_picking_loc
            where picking_location_id = wpp.picking_location_id
            and warehouse_id = %(wh)s)
            and picking_location_name = %(plname)s;
            """, d)
        a = dcur.fetchall()
        if a:
            return True


        if d["upc"] == "":
            d["upc"] = None
            
        a = dcur.execute(
            """
            with new_plid (picking_location_id) as
                (insert into warehouse.picking_locations
                     (picking_location_name, upc)
                 values(%(plname)s, %(upc)s::bigint)
                 returning picking_location_id)
            insert into warehouse.warehouse_picking_loc
                (warehouse_id, picking_location_id)
            select %(wh)s, picking_location_id
            from new_plid;
            """, d)


def bulk_load_pickinglocs(f, wh):
    a = dcur.execute(
        """
        begin;
        create temp table pls (
        picking_location_name varchar,
        upc varchar);
        """)

    ff = open(f)
    cur.copy_from(ff, "pls", sep=",")

    a = dcur.execute(
        """
        update pls
        set upc = null
        where upc = '';

        with tpls (picking_location_id) as
             (insert into warehouse.picking_locations
                   (picking_location_name, upc)
              select picking_location_name, upc::bigint
              from pls pls
              where not exists
                    (select *
                     from warehouse.picking_locations
                     join warehouse.warehouse_picking_loc
                     using (picking_location_id)
                     where picking_location_name =
                           pls.picking_location_name
                     and warehouse_id = %(wh)s)
             returning picking_location_id)
        insert into warehouse.warehouse_picking_loc
              (warehouse_id, picking_location_id)
        select %(wh)s, picking_location_id
        from tpls;

        drop table pls;
        commit;
        """, {"wh": wh})
