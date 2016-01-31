from bottle import *
import psycopg2
import psycopg2.extras
import collections

from models.amazon import *
from models.product import *
from models.warehouse import *

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

# amazon pages
@route("/channels/amazon/<section>/new-item")
def add_amazon_item(section):
    valid_list = valid_amazon_list()
    fdict = collections.OrderedDict()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_amazon_reg_fields(s)
        for f in fields:
            fdict[f[0]] = {}
            fdict[f[0]]["cname"] = f[1]
            fdict[f[0]]["data_type"] = f[3]
            if f[4]:
                fdict[f[0]]["valid_array"] = get_amazon_valid_arrays(s, f[4])
        return template("views/amazon_new_item", amz_header = amz_header, fields = fields, section = section, fdict = fdict)
    
@route("/channels/amazon/<section>")
def amazon_section(section):
    valid_list = valid_amazon_list()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_base_amazon_data(s)
        return template("views/amazon_section", amz_header = amz_header, fields = fields, section = section)
        
# product pages
@route("/channels/<storefront>")
def product_store(storefront = None):
    if storefront in ["amazon"]:
        a = select_amazon_regular()
        return template("views/amazon", reg = a)
    if storefront in ["ebay", "amazon"]:
        return template("views/channels")
    else:
        error404("err")

@route("/channels")
def products():
    return template("views/channels")

@route("/products/add-product")
def add_products():
    sku_upc = sku_upcs()
    stypes = sku_types()
    return template("views/add_product", sku_upc = sku_upc, sku_types = stypes)


@route("/products/all")
def all_products():
    sku_upc = sku_upcs()
    return template("views/all_products", sku_upc = sku_upc)

@route("/products")
def products():
    return template("views/products", sku_upc = None)

# warehouse pages
@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh = None):
    wh_query = valid_warehouses()
    pallet_location_list = pallet_locations(wh)
    valid_wh = [i[0].replace(" ", "-").lower() for i in wh_query]
    warehouse_name = wh.replace("-", " ").title()
    if wh.lower() in valid_wh:
        return template("views/warehouse_pallet_locations", warehouse_name = warehouse_name, pallet_location_list = pallet_location_list)

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    wh_query = valid_warehouses()
    wh_link = wh
    wh_list = [i[0] for i in wh_query]
    valid_wh = [i[0].replace(" ", "-").lower() for i in wh_query]
    warehouse_name = wh.replace("-", " ").title()
    if wh.lower() in valid_wh:
        return template("views/warehouse_page", wh_list = wh_list, warehouse_name = warehouse_name, wh_link = wh_link)

@route("/warehouses")
def warehouse():
    wh = valid_warehouses()
    valid_wh = [i[0] for i in wh]
    return template("views/warehouse", wh_list = valid_wh)

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
