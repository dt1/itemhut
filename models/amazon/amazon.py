# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def select_amazon_regular():
    a = dcur.execute(
	"""
	select schema_name,
        replace(replace(schema_name, 'amazon_', ''), '_', '-') slink,
        initcap(replace(replace(schema_name, 'amazon_', ''), '_', ' ')) sname
	from information_schema.schemata
	where schema_name ~~* 'amazon%'
	and schema_name !~~* '%lite'
        order by slink;
	""")
    a = dcur.fetchall()
    return a

def get_amazon_reg_fields(schema_name):
    a = dcur.execute(
        """
        select column_name, 
        initcap(replace(column_name, '_', ' ')) cname,
        t1.table_name t1tname, 
        data_type, 
        t2.table_name t2tname
        from
        (select table_name, column_name, ordinal_position, data_type
        from information_schema.columns
        where table_schema = '{0}'
        and table_name = 'template') t1
        left join
        (select table_name, column_name
        from information_schema.columns
        where table_schema = '{0}'
        and table_name != 'template') t2
        using (column_name)
        order by ordinal_position;
        """.format(schema_name))
    a = dcur.fetchall()
    return a

def get_amazon_valid_arrays(schema_name, table_name):
    a = dcur.execute(
        """
        select *
        from {0}.{1};
        """.format(schema_name, table_name))
    a = dcur.fetchall()
    return a

def get_arf(schema_name):
    c = dbconn.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    ca = dcur.execute(
        """
        select item_sku
        from {0}.template;
        """.format(schema_name))
    a = c.fetchall()
    return a

def get_base_amazon_data(schema_name):
    if schema_name == "amazon_coins":
        a = dcur.execute(
            """
            select item_sku, 'coin', quantity
            from {0}.template;
            """.format(schema_name))

    elif schema_name == "amazon_entertainment_collectibles":
        a = dcur.execute(
            """
            select item_sku, 'coin', limited_edition_quantity
            from {0}.template;
            """.format(schema_name))
    elif schema_name == "amazon_food_service_and_jan_san":

        a = dcur.execute(
            """
            select sku, "product-name", "number-of-items"
            from {0}.template;
            """.format(schema_name))

    else:
        a = dcur.execute(
            """
            select item_sku, item_name, quantity
            from {0}.template;
            """.format(schema_name))
    a = dcur.fetchall()
    return a

def valid_amazon_list():
    a = select_amazon_regular()
    valid_list = []
    for i in a:
        valid_list.append(i[1])
    return valid_list
