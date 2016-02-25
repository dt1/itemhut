# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn
import psycopg2

def select_valid_mskus():
    dbconn.cur.execute(
        """
        select marketplace_sku
        from orders.msku_sku;
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_market_order(market_order_id, marketplace, marketplace_sku, qty_sold):
    dbconn.cur.execute(
        """
        select market_order_id
        from orders.market_orders
        where market_order_id = trim(%s);
        """, [market_order_id])
    a = dbconn.cur.fetchall()
    if a:
        return True
    
    dbconn.cur.execute(
        """
        begin;
        insert into orders.market_orders
            (market_order_id, marketplace, marketplace_sku, qty_sold)
        values (trim(%s), trim(%s), trim(%s), %s::int);
        
        insert into orders.orders(market_order_id)
        values (trim(%s));

        commit;
        """, [market_order_id, marketplace, marketplace_sku, qty_sold,
              market_order_id])

def select_all_orders():
    dbconn.cur.execute(
        """
        select order_id, market_order_id, marketplace, sku, 
             marketplace_sku, qty_sold, order_date
        from orders.market_orders
        join orders.orders
        using (market_order_id)
        join orders.msku_sku
        using (marketplace_sku);
        """)
    a = dbconn.cur.fetchall()
    return a
