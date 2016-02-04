import sys
sys.path.append("/omark/pydb")
import dbconn

def sku_upcs():
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions
        using (sku);        
        """)
    a = dbconn.cur.fetchall()
    return a

def sku_types():
    dbconn.cur.execute(
        """
        select *
        from product.sku_types;
        """)
    a = dbconn.cur.fetchall()
    return a

def kits():
    dbconn.cur.execute(
        """
        select master_sku, 
        string_agg(child_sku || ' (' || child_sku_qty || ')', ' ') parts
        from product.kits
        group by master_sku;
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_sku_upc(sku, upc, sku_type):
    dbconn.cur.execute(
        """
        begin;
        insert into product.sku_upc (sku, upc, sku_type)
        values (trim(%s), %s::bigint, %s);
        commit;
        """, [sku, upc, sku_type])

def insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five):
    if not product_name:
        product_name = None

    if not product_description:
        product_description = None

    if not bullet_one:
        bullet_one = None

    if not bullet_two:
        bullet_two = None

    if not bullet_three:
        bullet_three = None

    if not bullet_four:
        bullet_four = None

    if not bullet_five:
        bullet_five = None

    dbconn.cur.execute(
        """
        begin;
        insert into product.descriptions 
        (sku, product_name, product_description, bullet_one, bullet_two,
      bullet_three, bullet_four, bullet_five)
        values (trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), 
        trim(%s), trim(%s), trim(%s));
        commit;
        """, [sku, product_name, product_description, bullet_one,
             bullet_two, bullet_three, bullet_four, bullet_five])

def insert_kit(master_sku, kit_sku, kit_amt):
    dbconn.cur.execute(
        """
        begin;
        insert into product.kits (master_sku, child_sku, child_sku_qty)
        values(%s, %s, %s);
        commit;
        """, [master_sku, kit_sku, kit_amt])

def get_upcs():
    dbconn.cur.execute(
        """
        select upc
        from product.sku_upc
        where upc is not null;
        """)
    a = dbconn.cur.fetchall()
    res = [i[0] for i in a]
    return res

def insert_new_case_box(upc, box_qty, case_qty):
    dbconn.cur.execute(
        """
        begin;
        with new_case_id (case_id) as
	     (insert into warehouse.cases (case_id)
              values (default)
	      returning case_id)
	      ,
        new_box_id (box_id) as
	      (insert into warehouse.boxes (upc, piece_qty)
	       values (%s::int, %s::int)
	       returning box_id)
         insert into warehouse.case_box (case_id, box_id, box_qty)
        select nci.case_id, nbi.box_id, %s::int
        from new_case_id nci,
        new_box_id nbi;
        commit;
        """, [upc, box_qty, case_qty])
