# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_all_companies():
    dbconn.cur.execute(
        """
        select company_id, company_uid, company_name, company_phone,
               company_phone2, company_fax, company_email,
               company_street, company_state, company_zip,
               company_country
        from company.companies;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_company_info(cid):
    dbconn.cur.execute(
        """
        select company_id, company_uid, company_name, company_phone,
               company_phone2, company_fax, company_email,
               company_street, company_state, company_zip,
               company_country
        from company.companies
        where company_id = %s::int;
        """, [cid])
    a = dbconn.cur.fetchall()
    return a

def insert_company(uid, cname, phone1, phone2, fax, email, street,
                   state, zipcode, country):
    dbconn.cur.execute(
        """
        begin;
        insert into company.companies (company_uid, company_name,
             company_phone, company_phone2, company_fax, company_email,
             company_street, company_state, company_zip,
             company_country)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        returning company_id;
        """, [uid, cname, phone1, phone2, fax, email, street,
                   state, zipcode, country])
    a = dbconn.cur.fetchall()
    dbconn.cur.execute(
        """
        commit;
        """)
    return a

def update_company(cid, uid, cname, phone1, phone2, fax, email,
                   street, state, zipcode, country):
    dbconn.cur.execute(
        """
        begin;
        update company.companies
        set company_uid = %s,
        company_name = %s,
        company_phone = %s,
        company_phone2 = %s,
        company_fax = %s,
        company_email = %s,
        company_street = %s,
        company_state = %s,
        company_zip = %s,
        company_country  = %s
        where company_id = %s::int;
        commit;
        """, [uid, cname, phone1, phone2, fax, email, street,
                   state, zipcode, country, cid])

def add_contact(cid, contact_name, contact_position, phone1, phone2,
                email):
    dbconn.cur.execute(
        """
        begin;
        with new_contact (contact_id) as
            (insert into company.contacts (contact_name,
                  contact_position, contact_phone, contact_phone2, 
                  contact_email)
             values (%s, %s, %s, %s, %s)
             returning (contact_id))
        insert into company.company_contact (company_id, contact_id)
        select %s, contact_id
        from new_contact
        returning contact_id;
        """, [contact_name, contact_position, phone1, phone2,
              email, cid])
    
    a = dbconn.cur.fetchall()

    dbconn.cur.execute(
        """
        commit;
        """)

    return a

def select_company_contacts(cid):
    dbconn.cur.execute(
        """
        select contact_id, contact_name, contact_position, 
               contact_phone, contact_phone2, contact_email
        from company.contacts ccs
        where exists
        (select *
         from company.company_contact
         where contact_id = ccs.contact_id
         and company_id = %s::int);
        """, [cid])
    a = dbconn.cur.fetchall()
    return a

def select_contact(cnid):
    dbconn.cur.execute(
        """
        select contact_id, contact_name, contact_position, 
        contact_phone, contact_phone2, contact_email
        from company.contacts
        where contact_id = %s::int;
        """, [cnid])
    a = dbconn.cur.fetchall()
    return a

def update_contact(cnid, contact_name, position, phone1, phone2,
                   email):
    dbconn.cur.execute(
        """
        begin;
        update company.contacts
        set contact_name = %s,
        contact_position = %s,
        contact_phone = %s,
        contact_phone2 = %s,
        contact_email = %s
        where contact_id = %s::int;
        commit;
        """, [contact_name, position, phone1, phone2, email, cnid])

def select_companies_with_contacts():
    dbconn.cur.execute(
        """
        select company_id, contact_id, company_uid, company_name, 
               contact_name
        from company.companies
        left join company.company_contact
        using (company_id)
        left join company.contacts
        using (contact_id);
        """)
    a = dbconn.cur.fetchall()
    return a
