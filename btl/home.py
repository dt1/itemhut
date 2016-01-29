from bottle import *
import psycopg2
import psycopg2.extras

import sys
sys.path.append("/omark/pydb")
import dbconn

@error(404)
def error404(error):
    return "404; please press the back button"

# for css, js, img, etc
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")


def select_amazon_regular():
    dbconn.cur.execute(
	"""
	select schema_name,
        replace(replace(schema_name, 'amazon_', ''), '_', '-') slink,
        initcap(replace(replace(schema_name, 'amazon_', ''), '_', ' ')) sname
	from information_schema.schemata
	where schema_name ~~* 'amazon%'
	and schema_name !~~* '%lite'
        order by slink;
	""")
    a = dbconn.cur.fetchall()
    return a

def get_amazon_reg_fields(schema_name):
    dbconn.cur.execute(
        """
        select column_name,
        initcap(replace(column_name, '_', ' ')) cname
        from information_schema.columns
        where table_schema = '{0}'
        and table_name = 'template'
        order by ordinal_position;
        """.format(schema_name))
    a = dbconn.cur.fetchall()
    return a

def get_arf(schema_name):
    c = dbconn.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    c.execute(
        """
        select item_sku
        from {0}.template;
        """.format(schema_name))
    a = c.fetchall()
    return a

def get_base_amazon_data(schema_name):
    dbconn.cur.execute(
        """
        select item_sku, item_name, quantity
        from {0}.template;
        """.format(schema_name))
    a = dbconn.cur.fetchall()
    return a

def valid_amazon_list():
    a = select_amazon_regular()
    valid_list = []
    for i in a:
        valid_list.append(i[1])
    return valid_list

# amazon pages
@route("/products/amazon/<section>/new-item")
def add_amazon_item(section):
    valid_list = valid_amazon_list()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_amazon_reg_fields(s)
        return template("views/amazon_section", amz_header = amz_header, fields = fields, section = section)
    
@route("/products/amazon/<section>")
def amazon_section(section):
    valid_list = valid_amazon_list()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_base_amazon_data(s)
        return template("views/amazon_section", amz_header = amz_header, fields = fields, section = section)

# product pages
@route("/products/<storefront>")
def product_store(storefront = None):
    if storefront in ["amazon"]:
        a = select_amazon_regular()
        return template("views/amazon", reg = a)
    if storefront in ["ebay", "amazon"]:
        return template("views/products")
    else:
        error404("err")

@route("/products")
def products():
    return template("views/products")

# warehouse pages
@route("/warehouse/<wh>")
def warehouse_n(wh = None):
    if wh in ["warehouse-a", "warehouse-b"]:
        return template("views/warehouse")
    else:
        error404("err")

@route("/warehouse")
def warehouse():
    return template("views/warehouse")

# order pages
@route("/orders")
def orders():
    return template("views/orders")

# emails
@route("/emails")
def emails():
    return template("views/emails")

# customers
@route("/customers")
def customers():
    return template("views/customers")

# analytics
@route("/analytics")
def analytics():
    return template("views/analytics")

# admin
@route("/admin")
def admin():
    return template("views/admin")

# home page    
@route("/")
def index():
    return template("views/home.tpl")

debug(True)
run(reloader=True, host="localhost", port=8080)
