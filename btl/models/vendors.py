# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/btl/pydb")
import dbconn

def select_vendors():
    dbconn.cur.execute(
        """
        select vendor_id, vendor_name, phone,
               fax, website, email,
               street, city, state,
               zip, country
        from vendor.vendors;
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_new_vendor(vendor_id, vendor_name, phone, fax, website,
                      email, street, city, state, zip, country):
    dbconn.cur.execute(
        """
        begin;
        insert into vendor.vendors (vendor_id, vendor_name, phone,
              fax, website, email, street, city, state, zip,
              country)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        on conflict (vendor_id)
        do update
        set vendor_name = excluded.vendor_name,
        phone = excluded.phone,
        fax = excluded.fax,
        website = excluded.website,
        email = excluded.email,
        street = excluded.street,
        city = excluded.city,
        state = excluded.state,
        zip = excluded.zip;
        commit;
        """, [vendor_id, vendor_name, phone, fax, website, email,
              street, city, state, zip, country])

def get_vendor_info(vendor_id):
    dbconn.cur.execute(
        """
        select vendor_id, vendor_name, phone,
              fax, website, email, street, city, state, zip,
              country
        from vendor.vendors
        where vendor_id = %s;
        """, [vendor_id])
    a = dbconn.cur.fetchall()
    return a

def insert_vendor_contact(vendor_id, contact_name, contact_title, phone, alt_phone, email):
    dbconn.cur.execute(
        """
        begin;
        with new_contact_id (contact_id) as
	     (insert into vendor.contacts (name, title, phone,
                      alt_phone, email)
              values (%s, %s, %s, %s, %s)
	      returning contact_id)
        insert into vendor.vendor_contact(vendor_id, contact_id)
        select %s, contact_id
        from new_contact_id;
        commit;
        """, [contact_name, contact_title, phone, alt_phone, email,
              vendor_id])

def update_vendor_contact(cid, contact_name, contact_title, phone,
                          alt_phone, email):
    dbconn.cur.execute(
        """
        begin;
        update vendor.contacts
        set name = %s,
        title = %s,
        phone = %s,
        alt_phone = %s,
        email = %s
        where contact_id = %s;
        commit;
        """, [contact_name, contact_title, phone,alt_phone,
              email, cid])

def select_vendor_contact_info(contact_id):
    dbconn.cur.execute(
        """
        select contact_id, name, title, phone, alt_phone, email
        from vendor.contacts
        where contact_id = %s;
        """, [contact_id])
    a = dbconn.cur.fetchall()
    return a
    

def select_vendor_contacts(vendor_id):
    dbconn.cur.execute(
        """
        select contact_id, name, title, phone, alt_phone, email
        from vendor.contacts
        join vendor.vendor_contact
        using (contact_id)
        where vendor_id = %s;
        """, [vendor_id])
    a = dbconn.cur.fetchall()
    return a    

def update_vendor_info(old_vendor_id, new_vendor_id, vendor_name,
                       phone, fax, website, email, street, city, state,
                       zip, country):
    if old_vendor_id.strip() != new_vendor_id.strip():
        dbconn.cur.execute(
            """
            begin;
            update vendor.vendors
            set vendor_id = trim(%s)
            where vendor_id = trim(%s);
            commit;
            """, [new_vendor_id, old_vendor_id])
    insert_new_vendor(new_vendor_id, vendor_name, phone, fax, website,
                      email, street, city, state, zip, country)

def insert_product_vendor(vendor_id, upc):
    dbconn.cur.execute(
        """
        begin;
        insert into vendor.vendor_products (vendor_id, upc)
        values (%s, %s)
        on conflict (upc)
        do nothing;
        commit;
        """, [vendor_id, upc])

def select_upc_list():
    dbconn.cur.execute(
        """
        select sku, upc
        from product.sku_upc
        where upc is not null;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_vendor_products(vid):
    dbconn.cur.execute(
        """
        begin;
        select upc, sku
        from vendor.vendor_products
        join product.sku_upc
        using (upc)
        where vendor_id = trim(%s);
        """, [vid])
    a = dbconn.cur.fetchall()
    return a
