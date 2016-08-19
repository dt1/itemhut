# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_vendors():
    dbconn.dcur.execute(
        """
        select vendor_id, vendor_name, phone,
               fax, website, email,
               street, city, state,
               zip, country
        from vendor.vendors;
        """)
    a = dbconn.dcur.fetchall()
    return a

def insert_new_vendor(d):
    dbconn.dcur.execute(
        """
        begin;
        insert into vendor.vendors (vendor_id, vendor_name, phone,
              fax, website, email, street, city, state, zip,
              country)
        values (%(vendor-id)s, %(vendor-name)s, %(phone)s, %(fax)s, 
        %(website)s, %(email)s, %(street)s, %(city)s, %(state)s, 
        %(zip)s, %(country)s)
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
        zip = excluded.zip,
        country = excluded.country;
        commit;
        """, d)

def get_vendor_info(vendor_id):
    dbconn.dcur.execute(
        """
        select vendor_id, vendor_name, phone,
              fax, website, email, street, city, state, zip,
              country
        from vendor.vendors
        where vendor_id = %s;
        """, [vendor_id])
    a = dbconn.dcur.fetchall()
    return a

def insert_vendor_contact(d):
    dbconn.dcur.execute(
        """
        begin;
        with new_contact_id (contact_id) as
	     (insert into vendor.contacts (name, title, phone,
                      alt_phone, email)
              values (%(name)s, %(title)s, %(phone)s, 
                      %(alt-phone)s, %(email)s)
	      returning contact_id)
        insert into vendor.vendor_contact(vendor_id, contact_id)
        select %(vid)s, contact_id
        from new_contact_id;
        commit;
        """, d)

def update_vendor_contact(d):
    dbconn.dcur.execute(
        """
        begin;
        update vendor.contacts
        set name = %(name)s,
        title = %(title)s,
        phone = %(phone)s,
        alt_phone = %(alt-phone)s,
        email = %(email)s
        where contact_id = %(cid)s;
        commit;
        """, d)

def select_vendor_contact_info(contact_id):
    dbconn.dcur.execute(
        """
        select contact_id, name, title, phone, alt_phone, email
        from vendor.contacts
        where contact_id = %s;
        """, [contact_id])
    a = dbconn.dcur.fetchall()
    return a
    

def select_vendor_contacts(vendor_id):
    dbconn.dcur.execute(
        """
        select contact_id, name, title, phone, alt_phone, email
        from vendor.contacts
        join vendor.vendor_contact
        using (contact_id)
        where vendor_id = %s;
        """, [vendor_id])
    a = dbconn.dcur.fetchall()
    return a    

def update_vendor_info(d):
    if d["old-vid"].strip() != d["vendor-id"].strip():
        dbconn.dcur.execute(
            """
            begin;
            update vendor.vendors
            set vendor_id = trim(%(vendor-id)s)
            where vendor_id = trim(%(old-vid)s);
            commit;
            """, d)
    insert_new_vendor(d)

def insert_product_vendor(vendor_id, upc):
    dbconn.dcur.execute(
        """
        begin;
        insert into vendor.vendor_products (vendor_id, upc)
        values (%s, %s::bigint)
        on conflict (upc)
        do nothing;
        commit;
        """, [vendor_id, upc])

def select_upc_list():
    dbconn.dcur.execute(
        """
        select sku, upc
        from product.sku_upc psu
        where upc is not null
        and not exists
        (select *
        from vendor.vendor_products
        where upc = psu.upc);
        """)
    a = dbconn.dcur.fetchall()
    return a

def select_vendor_products(vid):
    dbconn.dcur.execute(
        """
        begin;
        select upc, sku
        from vendor.vendor_products
        join product.sku_upc
        using (upc)
        where vendor_id = trim(%s);
        """, [vid])
    a = dbconn.dcur.fetchall()
    return a

def delete_vendor_product(vid, upc):
    dbconn.dcur.execute(
        """
        begin;
        delete from vendor.vendor_products
        where vendor_id = %s
        and upc = %s::bigint;
        commit;
        """, [vid, upc])
