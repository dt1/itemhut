# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
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
    if upc == '':
        upc = None
    dbconn.cur.execute(
        """
        begin;
        insert into product.sku_upc (sku, upc, sku_type)
        values (trim(%s), %s::bigint, %s)
        on conflict (sku)
        do update
        set upc = excluded.upc,
        sku_type = excluded.sku_type;
        commit;
        """, [sku, upc, sku_type])

def insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five):
    dbconn.cur.execute(
        """
        begin;
        insert into product.descriptions 
        (sku, product_name, product_description, bullet_one, 
        bullet_two, bullet_three, bullet_four, bullet_five)
        values (trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), 
        trim(%s), trim(%s), trim(%s))
        on conflict (sku)
        do update
        set product_name = excluded.product_name,
        product_description = excluded.product_description,
        bullet_one = excluded.bullet_one,
        bullet_two = excluded.bullet_two,
        bullet_three = excluded.bullet_three,
        bullet_four = excluded.bullet_four,
        bullet_five = excluded.bullet_five;
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

def insert_images(sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image):
    dbconn.cur.execute(
        """ begin; 
        insert into product.images (sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image)
        values (%s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s)
        on conflict (sku)
        do update
        set main_image = excluded.main_image,
        image_one = excluded.image_one,
        image_two = excluded.image_two,
        image_three = excluded.image_three,
        image_four = excluded.image_four,
        image_five = excluded.image_five,
        image_six = excluded.image_six,
        image_seven = excluded.image_seven,
        image_eight = excluded.image_eight,
        image_nine = excluded.image_nine,
        image_ten = excluded.image_ten,
        image_eleven = excluded.image_eleven,
        image_twelve = excluded.image_twelve,
        swatch_image = excluded.swatch_image;
        commit;
        """, [sku, main_image, image_one,
              image_two, image_three, image_four, image_five,
              image_six, image_seven, image_eight, image_nine,
              image_ten, image_eleven,
              image_twelve, swatch_image])
