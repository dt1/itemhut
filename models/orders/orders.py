# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur
import psycopg2

def select_all_orders():
    a = dcur.execute(
        """
        select internal_order_id, market_order_id, marketplace,
               company_name, order_date, salesperson_id
        from orders.market_orders
        join orders.moi_company
        using (internal_order_id)
        join company.companies
        using (company_id);
        """)
    a = dcur.fetchall()
    return a

def select_valid_mskus():
    a = dcur.execute(
        """
        select marketplace_sku
        from marketplace.msku_sku;
        """)
    a = dcur.fetchall()
    return a

def select_valid_marketplaces():
    a = dcur.execute(
        """
        select marketplace
        from marketplace.valid_markeplace;
        """)
    a = dcur.fetchall()
    return a

def insert_market_step1_no_sameship(d):
    if d["contact-id"] == "None":
        d["contact-id"] = None

    a = dcur.execute(
        """
        begin;
        with new_order (internal_order_id) as
            (insert into orders.market_orders (market_order_id,
                  marketplace, salesperson_id)
             values (%(order-id)s, %(marketplace)s, %(salesperson-id)s)
             returning internal_order_id)
        insert into orders.moi_company (internal_order_id, company_id,
             company_contact_id)
        select internal_order_id, %(company-id)s::int, 
               %(contact-id)s::int
        from new_order
        returning internal_order_id;
        """, d)
    a = dcur.fetchall()
    a = dcur.execute(
        """
        commit;
        """)
    return a

def insert_market_step1_sameship(d):
    if d["contact-id"] == "None":
        d["contact-id"] = None

    a = dcur.execute(
        """
        begin;
        select r_internal_order_id 
        from orders.insert_company_sameship(%(order-id)s, 
        %(salesperson-id)s, %(marketplace)s, %(company-id)s::int, 
        %(contact-id)s::int);
        """, d)
    a = dcur.fetchall()
    a = dcur.execute(
        """
        commit;
        """)
    return a

def insert_market_step1(d):
    if d["sameship"]:
        a = insert_market_step1_sameship(d)
    else:
        a = insert_market_step1_no_sameship(d)
    return a

def select_valid_market_order(order_id):
    a = dcur.execute(
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
    a = dcur.fetchall()
    return a

def insert_shipto(d):
    if ship_by_date == "":
        ship_by_date = None
    if deliver_by_date == "":
        deliver_by_date = None
    a = dcur.execute(
        """
        begin;
        select orders.insert_shipto_customer(%(oid)s::int, %(company)s,
        %(attn)s, %(street)s, %(city)s, %(state)s, %(zip)s, 
        %(country)s, %(ship-by)s, %(deliver-by)s);
        commit;
        """, d)

def select_order_companies(order_id):
    a = dcur.execute(
        """
        select shipto_id, internal_order_id, market_order_id,
        shipto_company_id,  shipto_company, ship_by_date,
        deliver_by_date
        from orders.shipto_companies
        join orders.shipto
        using (shipto_company_id)
        join orders.market_orders
        using (internal_order_id)
        where internal_order_id = %s::int
        order by shipto_id;
        """, [order_id])
    a = dcur.fetchall()
    return a

def select_company_product_candidates(order_id):
    a = dcur.execute(
        """
        select sku, marketplace_sku, product_name
        from marketplace.msku_marketplace mmm
        join marketplace.msku_sku
        using (marketplace_sku)
        left join product.descriptions
        using (sku)
        where exists
        (select *
        from orders.market_orders
        where marketplace = mmm.marketplace
        and internal_order_id = %s::int)
        and not exists
        (select *
        from orders.market_order_skus
        where marketplace_sku = mmm.marketplace_sku
        and internal_order_id = %s::int)
        and not exists
        (select *
        from orders.shipto_marketplace_skus
        where marketplace_sku = mmm.marketplace_sku);
        """, [order_id, order_id])
    a = dcur.fetchall()
    return a

def select_company_shipto_products(sid):
    a = dcur.execute(
        """
        select marketplace_sku, sku_qty
        from orders.shipto_marketplace_skus
        where shipto_id = %s;
        """, [sid])
    a = dcur.fetchall()
    return a

def insert_shipto_product(sid, msku, qty):
    a = dcur.execute(
        """
        begin;
        insert into orders.shipto_marketplace_skus
            (shipto_id, marketplace_sku, sku_qty)
        values (%s::int, %s, %s::int)
        on conflict (shipto_id, marketplace_sku)
        do update
        set sku_qty = %s::int;
        commit;
        """, [sid, msku, qty, qty])

def delete_company_product(sid, msku):
    a = dcur.execute(
        """
        begin;
        delete from orders.shipto_marketplace_skus
        where shipto_id = %s
        and marketplace_sku = %s;
        commit;
        """, [sid, msku])

def select_valid_filetypes():
    a = dcur.execute(
        """
        select file_type
        from orders.valid_file_type;
        """)
    a = dcur.fetchall()
    return a

def select_uploaded_files(sid):
    a = dcur.execute(
        """
        select file_path, file_type
        from orders.shipto_files
        where shipto_id = %s::int;
        """, [sid])
    a = dcur.fetchall()
    return a

def save_uploaded_files(sid, fpath, ftype):
    a = dcur.execute(
        """
        begin;
        insert into orders.shipto_files (shipto_id, file_path,
              file_type)
        values (%s::int, %s, %s);
        commit;
        """, [sid, fpath, ftype])

def delete_uploaded_file(sid, fpath):
    a = dcur.execute(
        """
        begin;
        delete from orders.shipto_files
        where shipto_id = %s::int
        and file_path = %s;
        commit;
        """, [sid, fpath])

def select_order_company_info(order_id):
    a = dcur.execute(
        """
        select internal_order_id, market_order_id, marketplace,
        salesperson_id, order_date, company_id, company_uid,
        company_name, company_phone, company_phone2, company_fax,
        company_email, company_street, company_state, company_zip,
        company_country, contact_name, contact_phone, contact_phone2,
        contact_email
        from orders.market_orders
        join orders.moi_company 
        using (internal_order_id)
        join company.companies 
        using (company_id)
        left join company.contacts
        using (company_contact_id)
        where internal_order_id = %s::int;
        """, [order_id])
    a = dcur.fetchall()
    return a

def select_order_shipto(order_id):
    a = dcur.execute(
        """
        select internal_order_id, shipto_id, shipto_company_id,
        shipto_company, shipto_attn, shipto_street, shipto_city,
        shipto_state, shipto_zip, shipto_country, ship_by_date,
        deliver_by_date,
        array_agg(marketplace_sku || ' (' || sku_qty || ')'),
        array_agg(file_path || ' (' || file_type || ')')
        from orders.shipto
        join orders.shipto_companies
        using (shipto_company_id)
        left join orders.shipto_marketplace_skus
        using (shipto_id)
        left join orders.shipto_files
        using (shipto_id)
        where internal_order_id = %s::int
        group by internal_order_id, shipto_id, shipto_company_id,
        shipto_company, shipto_attn, shipto_street, shipto_city,
        shipto_state, shipto_zip, shipto_country, ship_by_date,
        deliver_by_date;
        """, [order_id])
    a = dcur.fetchall()
    return a

def delete_shipto_record(sid):
    a = dcur.execute(
        """
        begin;
        delete from orders.shipto
        where shipto_id = %s::int;
        commit;
        """, [sid])

def edit_shipto_company(d):
    a = dcur.execute(
        """
        begin;
        update orders.shipto_companies
        set shipto_company = %(company)s, 
        shipto_attn = %(attn)s,
        shipto_street = %(street)s, 
        shipto_city = %(city)s,
        shipto_state = %(state)s,
        shipto_zip = %(zip)s, 
        shipto_country = %(country)s
        where shipto_id = %(sid)s::int;
        commit;
        """, d)
              
def select_salesteam_list():
    a = dcur.execute(
        """
        select user_name, person_name
        from users.users
        where user_type = 'sales';
        """)
    a = dcur.fetchall()
    return a
