#!/usr/bin/python3

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def commit():
    dbconn.cur.execute(
        """
        commit;
        """)
    

def set_warehouse_nulls():
    dbconn.cur.execute(
        """
        update warehouse.warehouses
        set warehouse_street_address = null
        where warehouse_street_address = 'None';

        update warehouse.warehouses
        set warehouse_state = null
        where warehouse_state = 'None';

        update warehouse.warehouses
        set warehouse_zip = null
        where warehouse_zip = 'None';

        update warehouse.warehouses
        set warehouse_country = null
        where warehouse_country = 'None';
        """)

def add_warehouse(warehouse_name, street_address = None, state = None,
                  w_zip = None, country = None):
    dbconn.cur.execute(
        """
        begin;
        with new_warehouse_id (wh_id) as
            (insert into warehouse.warehouses (warehouse_name, 
			 warehouse_street_address, warehouse_state,
			 warehouse_zip, warehouse_country)
             values ($${0}$$, $${1}$$, $${2}$$, $${3}$$, $${4}$$)
             returning warehouse_id)
        select wh_id
        from new_warehouse_id;
        """.format(warehouse_name, street_address, state, w_zip, country))

    new_warehouse_id = dbconn.cur.fetchone()[0]

    set_warehouse_nulls()
    commit()
    return new_warehouse_id

def update_warehouse(warehouse_id, warehouse_name, street_address = None,
                     state = None, w_zip = None, country = None):
    dbconn.cur.execute(
        """
        begin;
        update warehouse.warehouses
        set warehouse_name = $${1}$$,
            warehouse_street_address = $${2}$$,
            warehouse_state = $${3}$$,
            warehouse_zip = $${4}$$,
            warehouse_country = $${5}$$
        where warehouse_id = {0};
        commit;
        """.format(warehouse_id, warehouse_name, street_address, state, w_zip, country))
    set_warehouse_nulls()
    
def add_pallet():
    dbconn.cur.execute (
        """
        begin;
        with new_pallet_id (pid) as
		(insert into warehouse.pallets (pallet_id)
		values (default)
		returning pallet_id)
	select pid
	from new_pallet_id;
        """)
    new_pallet_id = dbconn.cur.fetchone()[0]
    commit()
    print(new_pallet_id)

def delete_pallet(pallet_id):
    dbconn.cur.execute(
        """
        begin;
        delete from warehouse.pallets
        where pallet_id = {0};
        commit;
        """.format(pallet_id))

