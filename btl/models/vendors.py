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
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
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


def select_vendor_contacts(vendor_id):
    dbconn.cur.execute(
        """
        select name, title, phone, alt_phone, email
        from vendor.contacts
        join vendor.vendor_contact
        using (contact_id)
        where vendor_id = %s;
        """, [vendor_id])
    a = dbconn.cur.fetchall()
    return a    
