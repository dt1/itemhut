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

def sku_kit_candidates():
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions
        using (sku)
        where sku_type <> 'master';
        """)
    a = dbconn.cur.fetchall()
    return a

def select_reg_products():
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions
        using (sku)
        where sku_type <> 'master';        
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

def insert_product_descriptions(sku, product_name,
                                product_description, bullet_one,
                                bullet_two, bullet_three, bullet_four,
                                bullet_five):
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
        set product_name = trim(excluded.product_name),
        product_description = trim(excluded.product_description),
        bullet_one = trim(excluded.bullet_one),
        bullet_two = trim(excluded.bullet_two),
        bullet_three = trim(excluded.bullet_three),
        bullet_four = trim(excluded.bullet_four),
        bullet_five = trim(excluded.bullet_five);
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
        """ 
        begin; 
        insert into product.images (sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image)
        values (%s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s)
        on conflict (sku)
        do update
        set main_image = trim(excluded.main_image),
        image_one = trim(excluded.image_one),
        image_two = trim(excluded.image_two),
        image_three = trim(excluded.image_three),
        image_four = trim(excluded.image_four),
        image_five = trim(excluded.image_five),
        image_six = trim(excluded.image_six),
        image_seven = trim(excluded.image_seven),
        image_eight = trim(excluded.image_eight),
        image_nine = trim(excluded.image_nine),
        image_ten = trim(excluded.image_ten),
        image_eleven = trim(excluded.image_eleven),
        image_twelve = trim(excluded.image_twelve),
        swatch_image = trim(excluded.swatch_image);
        commit;
        """, [sku, main_image, image_one,
              image_two, image_three, image_four, image_five,
              image_six, image_seven, image_eight, image_nine,
              image_ten, image_eleven,
              image_twelve, swatch_image])

def update_product_data(old_sku, new_sku, upc, sku_type, product_name,
                     product_description, image):
    if old_sku.strip() != new_sku.strip():
        dbconn.cur.execute(
            """
            begin;
            update product.sku_upc
            set sku = trim(%s)
            where sku = %s;
            commit;
            """, [new_sku, old_sku])
    insert_sku_upc(new_sku, upc, sku_type)
    insert_product_descriptions(new_sku, product_name,
                                product_description, None,
                                None, None, None, None)
    insert_images(new_sku, image, None, None, None, None, None, None,
                  None, None, None, None, None, None, None)

def get_sku_data(sku):
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name, product_description, 
               main_image
        from product.sku_upc
        left join product.descriptions
        using (sku)
        left join product.images
        using (sku)
        where trim(sku) = trim(%s);
        """, [sku])
    a = dbconn.cur.fetchall()
    return a
