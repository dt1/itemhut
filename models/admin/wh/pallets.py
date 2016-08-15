# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

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
