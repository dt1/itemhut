# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_user_count():
    dbconn.cur.execute(
        """
        select count(*)
        from users.users;
        """)
    a = dbconn.cur.fetchall()
    if a[0][0] > 0:
        return True
    else:
        return False

def select_warehouse_types():
    dbconn.cur.execute(
        """
        select warehouse_type
        from warehouse.valid_warehouse_type;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_warehouse_id(warehouse_id):
    dbconn.cur.execute(
        """
        select warehouse_id
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [warehouse_id])
    a = dbconn.cur.fetchall()
    return a

def insert_warehouse(warehouse_id, warehouse_name, street, state, zip,
                     country, warehouse_type):
    dbconn.cur.execute(
        """
        begin;
        insert into warehouse.warehouses (warehouse_id, warehouse_name,
            warehouse_street_address, warehouse_state, warehouse_zip,
            warehouse_country, warehouse_type)
        values (%s, %s, %s, %s, %s, %s, %s);
        commit;
        """, [warehouse_id, warehouse_name, street, state, zip,
                     country, warehouse_type])

def insert_new_user(username, password, real_name,  utype, urole):
    dbconn.cur.execute(
        """
        select user_name
        from users.users
        where user_name = %s;
        """, [username])
    a = dbconn.cur.fetchall()
    if a:
        return True

    dbconn.cur.execute(
        """
        begin;
        insert into users.users (user_name, password, person_name,
                user_type, user_role)
        values (trim(%s), %s, trim(%s), trim(%s), trim(%s));
        commit
        """, [username, password, real_name, utype, urole])

def select_user_password_role(username):
    dbconn.cur.execute(
        """
        select password, user_role
        from users.users
        where user_name = %s;
        """, [username])
    a = dbconn.cur.fetchall()
    return a

def select_valid_roles():
    dbconn.cur.execute(
        """
        select user_role
        from users.valid_user_roles
        where user_role <> 'original admin';
        """)
    a = dbconn.cur.fetchall()
    return a

def select_valid_usertypes():
    dbconn.cur.execute(
        """
        select user_type
        from users.valid_user_types;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_users():
    dbconn.cur.execute(
        """
        select user_name, person_name, user_type, user_role
        from users.users;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_user_info(uid):
    dbconn.cur.execute(
        """
        select user_name, person_name, user_type, user_role
        from users.users
        where user_name = %s;
        """, [uid])
    a = dbconn.cur.fetchall()
    return a

def update_user(original_username, username, real_name, utype,
                urole):
    if original_username != username:
        dbconn.cur.execute(
            """
            select user_name
            from users.users
            where user_name = %s;
            """, [username])
        a = dbconn.cur.fetchall()
        if a:
            return True

    if utype == "":
        utype = None

    dbconn.cur.execute(
        """
        begin;
        select users.update_user(%s, %s, %s, %s, %s);
        commit;
        """, [original_username, username, real_name,
              utype, urole])

def update_user_password(uid, pwd):
    dbconn.cur.execute(
        """
        begin;
        update users.users
        set password = %s
        where user_name = %s;
        commit;
        """, [pwd, uid])

def select_warehouse_list():
    dbconn.cur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_type
        from warehouse.warehouses;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_warehouse_info(wh):
    dbconn.cur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_street_address,
        warehouse_state, warehouse_zip, warehouse_country,
        warehouse_type
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def update_warehouse_info(original_wh_id, wh_id, wh_name, wh_street,
                          wh_state, wh_zip, wh_country):
    if original_wh_id != wh_id:
        dbconn.cur.execute(
            """
            select warehouse_id
            from warehouse.warehouses
            where warehouse_id = %s;
            """, [wh_id])
        a = dbconn.cur.fetchall()
        if a:
            return True

    dbconn.cur.execute(
        """
        begin;
        update warehouse.warehouses
        set warehouse_id = trim(%s),
        warehouse_name = trim(%s),
        warehouse_street_address = trim(%s),
        warehouse_state = trim(%s),
        warehouse_zip = trim(%s),
        warehouse_country = trim(%s)
        where warehouse_id = %s;
        commit;
        """, [wh_id, wh_name, wh_street, wh_state,
              wh_zip, wh_country, original_wh_id])

def select_palletlocs_list(wh):
    dbconn.cur.execute(
        """
        select pallet_location_id, pallet_location_name
        from warehouse.warehouse_pallet_loc
        join warehouse.pallet_locations
        using (pallet_location_id)
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.cur.fetchall()
    return a

def delete_palletloc(pid):
    dbconn.cur.execute(
        """
        begin;
        delete
        from warehouse.pallet_locations
        where pallet_location_id = %s::int;
        commit;
        """, [pid])

def bulk_load_palletlocs(f, wh):
    dbconn.cur.execute(
        """
        begin;
        create temp table pls (pallet_location_name varchar);

        copy pls
        from %s csv header;

        with tpls (pallet_location_id) as
            (insert into warehouse.pallet_locations
                 (pallet_location_name)
             select pallet_location_name
             from pls
             where not exists
	         (select *
                  from warehouse.pallet_locations
	          join warehouse.warehouse_pallet_loc
	          using (pallet_location_id)
	          where warehouse_id = %s
	          and pallet_location_name <> pls.pallet_location_name)
              returning pallet_location_id)
        insert into warehouse.warehouse_pallet_loc
            (warehouse_id, pallet_location_id)
        select %s, pallet_location_id
        from tpls;

        drop table pls;
        commit;
        """, [f, wh, wh])

def select_palletloc_name(plid):
    dbconn.cur.execute(
        """
        select pallet_location_name
        from warehouse.pallet_locations
        where pallet_location_id = %s::int;
        """, [plid])
    a = dbconn.cur.fetchall()
    return a

def update_palletloc_name(plid, pl_name, wh):
    dbconn.cur.execute(
        """
        select *
        from warehouse.pallet_locations
        join warehouse.warehouse_pallet_loc
        using (pallet_location_id)
        where pallet_location_name = trim(%s)
        and warehouse_id = %s;
        """, [pl_name, wh])
    a = dbconn.cur.fetchall()
    if a:
        return True

    dbconn.cur.execute(
        """
        begin;
        update warehouse.pallet_locations
        set pallet_location_name = %s
        where pallet_location_id = %s::int;
        commit;
        """, [pl_name, plid])

def insert_pallet_location(wh, pl_name):
    dbconn.cur.execute(
        """
        select *
        from warehouse.pallet_locations
        join warehouse.warehouse_pallet_loc
        using (pallet_location_id)
        where pallet_location_name = trim(%s)
        and warehouse_id = %s;
        """, [pl_name, wh])
    a = dbconn.cur.fetchall()
    if a:
        return True

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
        """, [pl_name, wh])

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
