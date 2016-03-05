# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def insert_company(uid, cname, phone1, phone2, fax, email, street,
                   state, zipcode, country):
    dbconn.cur.execute(
        """
        begin;
        insert into company.companies (company_uid, company_name, 
             company_phone, company_phone2, company_fax, company_email,
             company_street, copmany_state, company_zip, 
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
