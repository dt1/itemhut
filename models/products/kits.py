# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def sku_kit_candidates(sku):
    dbconn.cur.execute(
        """
        select sku, upc, product_name
        from product.sku_upc psu
        left join product.descriptions
        using (sku)
        where sku_type <> 'master'
        and not exists
        (select *
         from product.kits
         where child_sku = psu.sku
         and master_sku = %s);
        """, [sku])
    a = dbconn.cur.fetchall()
    return a

def select_sku_kits(sku):
    dbconn.cur.execute(
        """
        select child_sku, child_sku_qty
        from product.kits
        where master_sku = %s;
        """, [sku])
    a = dbconn.cur.fetchall()
    return a

def sku_kit_candidates(sku):
    dbconn.cur.execute(
        """
        select sku, upc, product_name
        from product.sku_upc psu
        left join product.descriptions
        using (sku)
        where sku_type <> 'master'
        and not exists
        (select *
         from product.kits
         where child_sku = psu.sku
         and master_sku = %s);
        """, [sku])
    a = dbconn.cur.fetchall()
    return a

def select_sku_kits(sku):
    dbconn.cur.execute(
        """
        select child_sku, child_sku_qty
        from product.kits
        where master_sku = %s;
        """, [sku])
    a = dbconn.cur.fetchall()
    return a

def select_kits():
    dbconn.cur.execute(
        """
        select master_sku, 
        string_agg(child_sku || ' (' || child_sku_qty || ')', ' ')
        from product.kits
        group by master_sku

        union

        select sku, null
        from product.sku_upc psu
        where sku_type = 'master'
        and not exists
	   (select *
	    from product.kits
	    where master_sku = psu.sku);
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_kit(master_sku, kit_sku, kit_amt):
    dbconn.cur.execute(
        """
        begin;
        insert into product.kits (master_sku, child_sku, child_sku_qty)
        values(%s, %s, %s);
        commit;
        """, [master_sku, kit_sku, kit_amt])

def delete_kit_child(master, child):
    dbconn.cur.execute(
        """
        begin;
        delete from product.kits
        where master_sku = %s
        and child_sku = %s;
        """, [master, child])
