# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def select_all_images():
    a = dcur.execute(
        """
        select array_agg(sku) sku_list, image
        from product.image_gallery ig
        left join product.images im
        on (ig.image = im.main_image
        or ig.image = im.image_one
        or ig.image = im.image_two
        or ig.image = im.image_three
        or ig.image = im.image_four
        or ig.image = im.image_five
        or ig.image = im.image_six
        or ig.image = im.image_seven
        or ig.image = im.image_eight
        or ig.image = im.image_nine
        or ig.image = im.image_ten
        or ig.image = im.image_eleven
        or ig.image = im.image_twelve
        or ig.image = im.swatch_image)
        group by image
        order by image;       
        """
    )
    a = dcur.fetchall()
    return a

def delete_image(d):
    a = dcur.execute(
        """
        begin;
        delete from product.image_gallery
        where image = %(img-del)s;
        commit;
        """, d)

def replace_image(d):
    a = dcur.execute(
        """
        begin;
        update table product.image_gallery
        set image = %(new-img)s
        where image = %(img-del)s;
        commit;
        """, d)

