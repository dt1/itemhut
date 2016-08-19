# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_warehouse_types():
    dbconn.dcur.execute(
        """
        select warehouse_type
        from warehouse.valid_warehouse_types;
        """)
    a = dbconn.dcur.fetchall()
    return a

def select_warehouse_id(warehouse_id):
    dbconn.dcur.execute(
        """
        select warehouse_id
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [warehouse_id])
    a = dbconn.dcur.fetchall()
    return a

def insert_warehouse(warehouse_id, warehouse_name, street, state, zip,
                     country, warehouse_type):
    dbconn.dcur.execute(
        """
        begin;
        insert into warehouse.warehouses (warehouse_id, warehouse_name,
            warehouse_street_address, warehouse_state, warehouse_zip,
            warehouse_country, warehouse_type)
        values (%s, %s, %s, %s, %s, %s, %s);
        commit;
        """, [warehouse_id, warehouse_name, street, state, zip,
                     country, warehouse_type])


def select_warehouse_list():
    dbconn.dcur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_type
        from warehouse.warehouses;
        """)
    a = dbconn.dcur.fetchall()
    return a

def select_warehouse_info(wh):
    dbconn.dcur.execute(
        """
        select warehouse_id, warehouse_name, warehouse_street_address,
        warehouse_state, warehouse_zip, warehouse_country,
        warehouse_type
        from warehouse.warehouses
        where warehouse_id = %s;
        """, [wh])
    a = dbconn.dcur.fetchall()
    return a

def update_warehouse_info(original_wh_id, wh_id, wh_name, wh_street,
                          wh_state, wh_zip, wh_country):
    if original_wh_id != wh_id:
        dbconn.dcur.execute(
            """
            select warehouse_id
            from warehouse.warehouses
            where warehouse_id = %s;
            """, [wh_id])
        a = dbconn.dcur.fetchall()
        if a:
            return True

    dbconn.dcur.execute(
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
