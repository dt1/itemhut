# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from bottle import *
import psycopg2
import psycopg2.extras
import collections

from models.amazon import *
from models.product import *
from models.warehouse import *

import sys
sys.path.append("/itemhut/pydb")
import dbconn


def ins_one(str):
    dbconn.cur.execute(
        """
        begin;
        insert into table_test.valid_one
        values ($${0}$$);
        commit;
        """.format(str))
    

@route("/test-insert")
@route("/test-insert", method="POST")
def test_insert():
    if request.POST.get("save", ""):
        task = request.POST.get("task").strip()
        hello = request.POST.get("hello", "").strip()
        t = request.forms.getall("task")
#        ins_one(item)
        return "{0}".format(t)

@error(404)
def error404(err):
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
        return template("views/amazon/new_item", amz_header = amz_header, fields = fields, section = section, fdict = fdict)
    
@route("/channels/amazon/<section>")
def amazon_section(section):
    valid_list = valid_amazon_list()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_base_amazon_data(s)
        return template("views/amazon/section", amz_header = amz_header, fields = fields, section = section)
        
# product pages
@route("/channels/<storefront>")
def product_store(storefront = None):
    if storefront in ["amazon"]:
        a = select_amazon_regular()
        return template("views/amazon/main", reg = a)
    if storefront in ["ebay"]:
        return template("views/ebay/main")
    else:
        error404("err")

@route("/channels")
def products():
    return template("views/channels")

@route("/products/add-kit")
@route("/products/add-kit", method="POST")
def add_kit():
    sku_upc = sku_upcs()
    if request.POST.get("add-kit"):
        master_sku = request.POST.get("master-sku")
        for i in range(1, 11):
            kit_name = request.POST.get("kit-name-{0}".format(i))
            kit_amt = request.POST.get("kit-amt-{0}".format(i))
            if kit_name:
                if kit_amt:
                    insert_sku_upc(master_sku, None, "master")
                    insert_kit(master_sku, kit_name, kit_amt)
                else:
                    return template("views/products/add_kit", sku_upc = sku_upc, new_sku = None, err = "Please add an amount for your kits")
        return template("views/products/add_kit", sku_upc = sku_upc, new_sku = master_sku, err = None)
    else:
        return template("views/products/add_kit", sku_upc = sku_upc, new_sku = None, err = None)

@route("/products/kits")
def all_kits():
    k = kits()
    return template("views/products/kits", kits = k)

@route("/products/add-product")
@route("/products/add-product", method="POST")
def add_products():
    sku_upc = sku_upcs()
    stypes = sku_types()
    if request.POST.get("add-product"):
        sku = request.POST.get("sku")
        upc = request.POST.get("upc")
        sku_type = request.POST.get("sku_type")

        insert_sku_upc(sku, upc, sku_type)
        
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        bullet_one = request.POST.get("bullet-one")
        bullet_two = request.POST.get("bullet-two")
        bullet_three = request.POST.get("bullet-three")
        bullet_four = request.POST.get("bullet-four")
        bullet_five = request.POST.get("bullet-five")

        insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five)
        
        main_image = request.POST.get("main-image")

        
        image_one = request.POST.get("image-one")
        image_two = request.POST.get("image-two")
        image_three = request.POST.get("image-three")
        image_four = request.POST.get("image-four")
        image_five = request.POST.get("image-five")
        image_six = request.POST.get("image-six")
        image_seven = request.POST.get("image-seven")
        image_eight = request.POST.get("image-eight")
        image_nine = request.POST.get("image-nine")
        image_ten = request.POST.get("image-ten")
        image_eleven = request.POST.get("image-eleven")
        image_twelve = request.POST.get("image-twelve")
        swatch_image = request.POST.get("swatch-image")
        return template("views/products/add_product", sku_upc = sku_upc, sku_types = stypes, new_sku = sku)
    else:
        return template("views/products/add_product", sku_upc = sku_upc, sku_types = stypes, new_sku = None)

@route("/products/all")
def all_products():
    sku_upc = sku_upcs()
    return template("views/products/all_products", sku_upc = sku_upc)

@route("/products")
def products():
    return template("views/products/main", sku_upc = None)


# warehouse pages:
@route("/warehouses/cases/new-config")
@route("/warehouses/cases/new-config", method="POST")
def new_warehouse_case_config():
    upc_list = get_upcs()
    if request.POST.get("add-config"):
        upc = request.POST.get("upc")
        box_qty = request.POST.get("box-qty")
        case_qty = request.POST.get("case-qty")
        if int(upc) in upc_list:
            insert_new_case_box(upc, box_qty, case_qty)
            return template("views/warehouse/new_case_box", err = None)
        else:
            return template("views/warehouse/new_case_box", err = "UPC invalid: " + upc)
    else:
        return template("views/warehouse/new_case_box", err = None)

@route("/warehouses/cases")
def warehouse_cases():
    case_boxes = get_case_boxes()
    return template("views/warehouse/case_boxes", case_boxes = case_boxes)

@route("/warehouses/<wh>/information")
def warehouse_pallet_locations(wh = None):
    wh_info = warehouse_information(wh)
    if wh_info:
        return template("views/warehouse/information", wh_info = wh_info)
    else:
        error404("err")


@route("/warehouses/<wh>/running-inventory")
def warehouse_pallet_locations(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    sku_count = running_inventory(wh)
    if warehouse_name:
        return template("views/warehouse/running_inventory", warehouse_name = warehouse_name, sku_count = sku_count)
    else:
        error404("err")


@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    pallet_location_list = pallet_locations(wh)
    if warehouse_name:
        return template("views/warehouse/pallet_locations", warehouse_name = warehouse_name, pallet_location_list = pallet_location_list)
    else:
        error404("err")

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    if warehouse_name:
        return template("views/warehouse/page", warehouse_name = warehouse_name, wh_link = warehouse_lower)
    else:
        error404("err")
    
@route("/warehouses")
def warehouse():
    wh = valid_warehouses()
    valid_wh = [i[0] for i in wh]
    return template("views/warehouse/main", wh_list = valid_wh)

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
