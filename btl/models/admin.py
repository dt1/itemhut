# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/btl/pydb")
import dbconn

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
