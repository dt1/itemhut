# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def select_all_companies():
    a = dcur.execute(
        """
        select company_id, company_uid, company_name, company_phone,
               company_phone2, company_fax, company_email,
               company_street, company_state, company_zip,
               company_country
        from company.companies;
        """)
    a = dcur.fetchall()
    return a

def select_company_info(cid):
    a = dcur.execute(
        """
        select company_id, company_uid, company_name, company_phone,
               company_phone2, company_fax, company_email,
               company_street, company_state, company_zip,
               company_country
        from company.companies
        where company_id = %s::int;
        """, [cid])
    a = dcur.fetchall()
    return a

def insert_company(d):
    a = dcur.execute(
        """
        begin;
        insert into company.companies (company_uid, company_name,
             company_phone, company_phone2, company_fax, company_email,
             company_street, company_city, company_state, company_zip,
             company_country)
        values (%(company-uid)s, %(company-name)s, %(phone-one)s, 
        %(phone-two)s, %(fax)s, %(email)s, %(street)s, %(city)s, 
        %(state)s, %(zip)s, %(country)s)
        returning company_id;
        """, d)
    a = dcur.fetchall()
    a = dcur.execute(
        """
        commit;
        """)
    return a

def update_company(d):
    a = dcur.execute(
        """
        begin;
        update company.companies
        set company_uid = %(company-uid)s,
        company_name = %(company-name)s,
        company_phone = %(phone-one)s,
        company_phone2 = %(phone-two)s,
        company_fax = %(fax)s,
        company_email = %(email)s,
        company_street = %(street)s,
        company_state = %(state)s,
        company_zip = %(zip)s,
        company_country  = %(country)s
        where company_id = %(cid)s::int;
        commit;
        """, d)

def add_contact(d):
    a = dcur.execute(
        """
        begin;
        with new_contact (contact_id) as
            (insert into company.contacts (contact_name,
                  contact_position, contact_phone, contact_phone2, 
                  contact_email)
             values (%(contact-name)s, %(position)s, %(phone-one)s, 
        %(phone-two)s, %(email)s)
             returning (company_contact_id))
        insert into company.company_contact (company_id, 
        company_contact_id)
        select %(cid)s, contact_id
        from new_contact
        returning company_contact_id;
        """, d)
    a = dcur.fetchall()

    a = dcur.execute(
        """
        commit;
        """)

    return a

def select_company_contacts(cid):
    a = dcur.execute(
        """
        select company_contact_id, contact_name, contact_position, 
               contact_phone, contact_phone2, contact_email
        from company.contacts ccs
        where exists
        (select *
         from company.company_contact
         where company_contact_id = ccs.company_contact_id
         and company_id = %(cid)s::int);
        """, {"cid": cid})
    a = dcur.fetchall()
    return a

def select_contact(cnid):
    a = dcur.execute(
        """
        select company_contact_id, contact_name, contact_position, 
        contact_phone, contact_phone2, contact_email
        from company.contacts
        where company_contact_id = %(cnid)s::int;
        """, {"cnid": cnid})
    a = dcur.fetchall()
    return a

def update_contact(d):
    a = dcur.execute(
        """
        begin;
        update company.contacts
        set contact_name = %(contact-name)s,
        contact_position = %(position)s,
        contact_phone = %(phone-one)s,
        contact_phone2 = %(phone-two)s,
        contact_email = %(email)s
        where company_contact_id = %(cnid)s::int;
        commit;
        """, d)

def select_companies_with_contacts():
    a = dcur.execute(
        """
        select company_id, company_contact_id, company_uid, company_name, 
               contact_name
        from company.companies
        left join company.company_contact
        using (company_id)
        left join company.contacts
        using (company_contact_id);
        """)
    a = dcur.fetchall()
    return a
