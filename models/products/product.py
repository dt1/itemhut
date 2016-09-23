# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

from models.products.kits import *

def select_image_gallery():
    a = dcur.execute(
        """
        select image
        from product.image_gallery
        order by image;
        """)
    a = dcur.fetchall()
    return a

def update_product_set_img_null(d):
    a = dcur.execute(
        """
        select product.set_product_image_null
            (%(sku)s, %(remove-image)s);
        """, d)

def update_product_image(d):
    a = dcur.execute(
        """
        select product.update_image_by_col
        (%(image-column)s, %(new-image)s, %(sku)s);
        """, d)

def sku_upcs():
    a = dcur.execute(
        """
        select image
        from product.image_gallery
        """)
    a = dcur.fetchall()
    return a

def insert_sku_upc(d):
    a = dcur.execute(
        """
        begin;
        insert into product.sku_upc (sku, upc, sku_type)
        values (trim(%(sku)s), %(upc)s::bigint, %(sku-type)s)
        on conflict (sku)
        do update
        set upc = excluded.upc,
        sku_type = excluded.sku_type;
        commit;
        """, d)

def select_reg_products():
    a = dcur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions

        using (sku)
        where sku_type <> 'master';
        """)
    a = dcur.fetchall()
    return a

def sku_types():
    a = dcur.execute(
        """
        select sku_type
        from product.sku_types;
        """)
    a = dcur.fetchall()
    return a

def insert_product_descriptions(d):
    a = dcur.execute(
        """
        begin;
        insert into product.descriptions
        (sku, product_name, product_description, bullet_one,
        bullet_two, bullet_three, bullet_four, bullet_five)
        values (trim(%(sku)s), trim(%(product-name)s),
        trim(%(product-description)s), trim(%(bullet-one)s),
        trim(%(bullet-two)s), trim(%(bullet-three)s),
        trim(%(bullet-four)s), trim(%(bullet-five)s))
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
        """, d)

def get_upcs():
    a = dcur.execute(
        """
        select upc
        from product.sku_upc
        where upc is not null;
        """)
    a = dcur.fetchall()
    res = [i[0] for i in a]
    return res

def insert_new_case_box(d):
    a = dcur.execute(
        """
        begin;
        with new_case_id (case_id) as
	     (insert into warehouse.cases (case_id)
              values (default)
	      returning case_id)
	      ,
        new_box_id (box_id) as
	      (insert into warehouse.boxes (upc, piece_qty)
	       values (%(upc)s::int, %(box-qty)s::int)
	       returning box_id)
        insert into warehouse.case_box (case_id, box_id, box_qty)
        select nci.case_id, nbi.box_id, %(case-qty)s::int
        from new_case_id nci,
        new_box_id nbi;
        commit;
        """, d)

def insert_images(d):
    a = dcur.execute(
        """
        begin;
        create temp table ig (image varchar);
        
        insert into ig (image)
        values(%(main-image-path)s),
        (%(image-one-path)s),
        (%(image-two-path)s),
        (%(image-three-path)s),
        (%(image-four-path)s),
        (%(image-five-path)s),
        (%(image-six-path)s),
        (%(image-seven-path)s),
        (%(image-eight-path)s),
        (%(image-nine-path)s),
        (%(image-ten-path)s),
        (%(image-eleven-path)s),
        (%(image-twelve-path)s),
        (%(swatch-image-path)s);

        insert into product.image_gallery(image)
        select image from ig
        where ig.image is not null;

        drop table ig;

        insert into product.images (sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image)
        values (%(sku)s, %(main-image-path)s,
        %(image-one-path)s, %(image-two-path)s, %(image-three-path)s,
        %(image-four-path)s, %(image-five-path)s, %(image-six-path)s,
        %(image-seven-path)s, %(image-eight-path)s,
        %(image-nine-path)s, %(image-ten-path)s, %(image-eleven-path)s,
        %(image-twelve-path)s, %(swatch-image-path)s)
        on conflict (sku)
        do update
        set main_image = coalesce(trim(excluded.main_image),
                                  product.images.main_image),
        image_one = coalesce(trim(excluded.image_one),
                             product.images.image_one),
        image_two = coalesce(trim(excluded.image_two),
                             product.images.image_two),
        image_three = coalesce(trim(excluded.image_three),
                               product.images.image_three),
        image_four = coalesce(trim(excluded.image_four),
                              product.images.image_four),
        image_five = coalesce(trim(excluded.image_five),
                              product.images.image_five),
        image_six = coalesce(trim(excluded.image_six),
                             product.images.image_six),
        image_seven = coalesce(trim(excluded.image_seven),
                               product.images.image_seven),
        image_eight = coalesce(trim(excluded.image_eight),
                               product.images.image_eight),
        image_nine = coalesce(trim(excluded.image_nine),
                              product.images.image_nine),
        image_ten = coalesce(trim(excluded.image_ten),
                             product.images.image_ten),
        image_eleven = coalesce(trim(excluded.image_eleven),
                                product.images.image_eleven),
        image_twelve = coalesce(trim(excluded.image_twelve),
                                product.images.image_twelve),
        swatch_image = coalesce(trim(excluded.swatch_image),
                                product.images.swatch_image);
        commit;
        """, d)

def update_product_data(d):
    if d["pid"].strip() != d["sku"].strip():
        a = dcur.execute(
            """
            begin;
            update product.sku_upc
            set sku = trim(%(sku)s)
            where sku = trim(%(pid)s);
            commit;
            """, d)

    insert_sku_upc(d)
    insert_product_descriptions(d)

def get_sku_data(sku):
    a = dcur.execute(
        """
        select sku, upc, sku_type, product_name, product_description,
               bullet_one, bullet_two, bullet_three, bullet_four,
               bullet_five, main_image, image_one, image_two,
               image_three, image_four, image_five, image_six,
               image_six, image_seven, image_eight, image_nine,
               image_ten, image_eleven, image_twelve, swatch_image
        from product.sku_upc
        left join product.descriptions
        using (sku)
        left join product.images
        using (sku)
        where trim(sku) = trim(%s);
        """, [sku])
    a = dcur.fetchall()
    return a
