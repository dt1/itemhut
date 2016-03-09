# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn
import psycopg2

def select_valid_mskus():
    dbconn.cur.execute(
        """
        select marketplace_sku
        from marketplace.msku_sku;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_valid_marketplaces():
    dbconn.cur.execute(
        """
        select marketplace
        from marketplace.valid_markeplace;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_all_orders():
    dbconn.cur.execute(
        """
        select 1;
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_market_step1_no_sameship(order_id, marketplace,
                                    salesperson_id, company_id,
                                    contact_id):
    if contact_id == "None":
        contact_id = None
        
    dbconn.cur.execute(
        """
        begin;
        with new_order (internal_order_id) as
            (insert into orders.market_orders (market_order_id,
                  marketplace, salesperson_id)
             values (%s, %s, %s)
             returning internal_order_id)
        insert into orders.moi_company (internal_order_id, company_id,
             company_contact_id)
        select internal_order_id, %s::int, %s::int
        from new_order
        returning internal_order_id;
        """, [order_id, marketplace, salesperson_id, company_id,
              contact_id])
    a = dbconn.cur.fetchall()
    dbconn.cur.execute(
        """
        commit;
        """)
    return a

def insert_market_step1_sameship(order_id, marketplace,
                                 salesperson_id, company_id,
                                 contact_id):
    if contact_id == "None":
        contact_id = None
        
    dbconn.cur.execute(
        """
        begin;
        with new_order (internal_order_id) as
            (insert into orders.market_orders (market_order_id,
                  marketplace, salesperson_id)
             values (%s, %s, %s)
             returning internal_order_id)
             ,
             new_moi (internal_order_id) as
             (insert into orders.moi_company (internal_order_id, 
                                              company_id,
                                              company_contact_id)
              select internal_order_id, %s::int, %s::int
              from new_order
              returning internal_order_id)
        insert into orders.shipto(internal_order_id, shipto_company,
                    shipto_attn, shipto_street, shipto_city, 
                    shipto_state, shipto_zip, shipto_country)
        select internal_order_id, company_name, contact_name, 
                company_street, company_state, 
                company_state, company_zip, 
                company_country
        from company.companies
        left join company.company_contact
        using (company_id)
        left join company.contacts
        using (contact_id)
        , new_moi
        where company_id = %s::int
        and (contact_id = %s::int
        or contact_id is null)
        returning internal_order_id;
        """, [order_id, marketplace, salesperson_id, company_id,
              contact_id, company_id, contact_id])
    a = dbconn.cur.fetchall()
    dbconn.cur.execute(
        """
        commit;
        """)
    return a

def insert_market_step1(order_id, marketplace, salesperson_id,
                        sameship, company_id, contact_id):
    if sameship:
        a = insert_market_step1_sameship(order_id, marketplace,
                                            salesperson_id, company_id,
                                            contact_id)
    else:
        a = insert_market_step1_no_sameship(order_id, marketplace,
                                            salesperson_id, company_id,
                                            contact_id)
    return a

def select_valid_markter_order(order_id):
    dbconn.cur.execute(
        """
        select internal_order_id, market_order_id, shipto_company_id, 
        shipto_company, 
        shipto_attn, shipto_street, shipto_city, shipto_state,
        shipto_zip, shipto_country, ship_by_date, deliver_by_date
        from orders.market_orders
        left join orders.shipto
        using (internal_order_id)
        left join orders.shipto_companies
        using (shipto_company_id)
        where internal_order_id = %s::int;
        """, [order_id])
    a = dbconn.cur.fetchall()
    return a

def insert_shipto(oid, shipto_company, shipto_attn, shipto_street,
                  shipto_city, shipto_state, shipto_zip,
                  shipto_country, ship_by_date, deliver_by_date):
    if ship_by_date == "":
        ship_by_date = None
    if deliver_by_date == "":
        deliver_by_date = None
    dbconn.cur.execute(
        """
        begin;
        select orders.insert_shipto_customer(%s::int, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s);
        commit; 
        """, [oid, shipto_company, 
        shipto_attn, shipto_street, shipto_city, shipto_state, 
        shipto_zip, shipto_country, ship_by_date, deliver_by_date])
