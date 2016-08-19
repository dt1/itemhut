# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_palletlocs_list(wh):
    dbconn.dcur.execute(
        """
        select pallet_location_id, pallet_location_name
        from warehouse.warehouse_pallet_loc
        join warehouse.pallet_locations
        using (pallet_location_id)
        where warehouse_id = %(wh_id)s;
        """, {"wh_id": wh})
    a = dbconn.dcur.fetchall()
    return a

def delete_palletloc(pid):
    dbconn.dcur.execute(
        """
        begin;
        delete
        from warehouse.pallet_locations
        where pallet_location_id = %(pid)s::int;
        commit;
        """, {"pid": pid})

def bulk_load_palletlocs(f, wh):
    dbconn.dcur.execute(
        """
        begin;
        create temp table pls (pallet_location_name varchar);

        copy pls
        from %(file)s csv header;

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
	          where warehouse_id = %(wh)s
	          and pallet_location_name <> pls.pallet_location_name)
              returning pallet_location_id)
        insert into warehouse.warehouse_pallet_loc
            (warehouse_id, pallet_location_id)
        select %(wh)s, pallet_location_id
        from tpls;

        drop table pls;
        commit;
        """, {"file": f,
              "wh": wh})

def select_palletloc_name(plid):
    dbconn.dcur.execute(
        """
        select pallet_location_name
        from warehouse.pallet_locations
        where pallet_location_id = %(plid)s::int;
        """, {"plid": plid})
    a = dbconn.dcur.fetchall()
    return a

def update_palletloc_name(plid, pl_name, wh):
    dbconn.dcur.execute(
        """
        select *
        from warehouse.pallet_locations
        join warehouse.warehouse_pallet_loc
        using (pallet_location_id)
        where pallet_location_name = trim(%(plname)s)
        and warehouse_id = %(wh)s;
        """, {"plname": pl_name,
              "wh": wh})
    a = dbconn.dcur.fetchall()
    if a:
        return True

    dbconn.dcur.execute(
        """
        begin;
        update warehouse.pallet_locations
        set pallet_location_name = %(plname)s
        where pallet_location_id = %s(plid)::int;
        commit;
        """, {"plname": pl_name,
              "plid": plid})

def insert_pallet_location(wh, pl_name):
    dbconn.dcur.execute(
        """
        select *
        from warehouse.pallet_locations
        join warehouse.warehouse_pallet_loc
        using (pallet_location_id)
        where pallet_location_name = trim(%(plname)s)
        and warehouse_id = %(wh)s;
        """, {"plname": pl_name,
              "wh": wh})
    a = dbconn.dcur.fetchall()
    if a:
        return True

    dbconn.dcur.execute(
        """
        begin;
        with new_loc (pallet_location_id) as
	    (insert into warehouse.pallet_locations
             (pallet_location_name)
	     values (%(plname)s)
	     returning pallet_location_id
	     )
        insert into warehouse.warehouse_pallet_loc
                    (warehouse_id, pallet_location_id)
        select %(wh)s, pallet_location_id
        from new_loc;
        commit;
        """, {"plname": pl_name,
              "wh": wh})
