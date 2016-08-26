# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def sku_kit_candidates(sku):
    a = dcur.execute(
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
    a = dcur.fetchall()
    return a

def select_sku_kits(sku):
    a = dcur.execute(
        """
        select child_sku, child_sku_qty
        from product.kits
        where master_sku = %s;
        """, [sku])
    a = dcur.fetchall()
    return a

def sku_kit_candidates(sku):
    a = dcur.execute(
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
    a = dcur.fetchall()
    return a

def select_sku_kits(sku):
    a = dcur.execute(
        """
        select child_sku, child_sku_qty
        from product.kits
        where master_sku = %s;
        """, [sku])
    a = dcur.fetchall()
    return a

def select_kits():
    a = dcur.execute(
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
    a = dcur.fetchall()
    return a

def insert_kit_child(d):
    a = dcur.execute(
        """
        begin;
        insert into product.kits (master_sku, child_sku, child_sku_qty)
        values(%(sku)s, %(kit-sku)s, %(qty)s::int);
        commit;
        """, d)

def delete_kit_child(master, child):
    a = dcur.execute(
        """
        begin;
        delete from product.kits
        where master_sku = %(master)s
        and child_sku = %(child)s;
        """, [master, child])
