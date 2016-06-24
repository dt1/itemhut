# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from datetime import datetime

@route("/orders/order<oid:int>/delete-shipto-record-<sid:int>")
def delete_shipto_record(oid, sid):
    check_user()
    ords.delete_shipto_record(sid)
    url = "/orders/view-order-{0}".format(oid)
    redirect(url)
    
@route("/orders/add-order/order<oid:int>/delete-file<sid:int>/<p>/<f>")
def delete_order_file(oid, sid, p, f):
    check_user()
    fpath = "{0}/{1}".format(p, f)
    ords.delete_uploaded_file(sid, fpath)
    delfile = "uploaded_files/orders/{0}/{1}".format(p, f)
    os.remove(delfile)
    delpath = "uploaded_files/orders/{0}".format(p)
    os.rmdir(delpath)
    url = "/orders/add-order/order{0}/company{1}-add-files".format(oid, sid)
    redirect(url)


@route("/orders/add-order/order<oid:int>/company<sid:int>-add-files")
@post("/orders/add-order/order<oid:int>/company<sid:int>-add-files")
@view("views/orders/add_files")
def add_order_file(oid, sid):
    check_user()
    mlist = ords.select_valid_market_order(oid)
    valid_ftypes = ords.select_valid_filetypes()
    uploaded_files = ords.select_uploaded_files(sid)
    if request.POST.get("add-file"):
        upload = request.POST.get("upload")
        ftype = request.POST.get("ftype")

        phash = abs(hash(datetime.now()))
        save_path = "uploaded_files/orders/{0}".format(phash)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        upload.save(save_path)

        fpath = "{0}/{1}".format(phash, upload.filename)
        ords.save_uploaded_files(sid, fpath, ftype)

        url = "/orders/add-order/order{0}/company{1}-add-files".format(oid, sid)
        redirect(url)

    return dict(mlist = mlist, oid = oid, sid = sid,
                valid_ftypes = valid_ftypes,
                uploaded_files = uploaded_files)


@route("/orders/add-order/order<oid:int>/company<sid:int>-delete-product-<msku>")
def delete_company_product(oid, sid, msku):
    check_user()
    ords.delete_company_product(sid, msku)
    url = "/orders/add-order/order{0}/company{1}-add-products".format(oid, sid)
    redirect(url)

@route("/orders/add-order/order<oid:int>/company<sid:int>-add-products")
@post("/orders/add-order/order<oid:int>/company<sid:int>-add-products")
@view("views/orders/add_company_products")
def add_company_products(oid, sid):
    check_user()
    mlist = ords.select_valid_market_order(oid)
    pclist = ords.select_company_product_candidates(oid)
    added_plist = ords.select_company_shipto_products(sid)
    if request.POST.get("add-product"):
        msku = request.POST.get("msku")
        qty = request.POST.get("qty")
        ords.insert_shipto_product(sid, msku, qty)
        url = "/orders/add-order/order{0}/company{1}-add-products".format(oid, sid)
        redirect(url)
    return dict(mlist = mlist, oid = oid, sid = sid, pclist = pclist,
                added_plist = added_plist)


@route("/orders/add-order/order<oid:int>/company<cid:int>")
def redirect_to_company_page(oid, cid):
    check_user()
    url = "/orders/add-order/order{0}/list-companies".format(oid)
    redirect(url)

@route("/orders/add-order/order<oid:int>/list-companies")
@view("views/orders/list_companies")
def add_order_list_companies(oid):
    check_user()
    clist = ords.select_order_companies(oid)
    return dict(clist = clist)


@route("/orders/order<oid:int>/edit-deliver-to-<sid:int>")
@post("/orders/order<oid:int>/edit-deliver-to-<sid:int>")
@view("views/orders/edit_deliver_to")
def edit_deliver_to(oid, sid):
    check_user()
    mlist = ords.select_valid_market_order(oid)
    shipto_info = ords.select_order_shipto(oid)
    if request.POST.get("edit-company"):
        shipto_company = request.POST.get("company")
        shipto_attn = request.POST.get("attn")
        shipto_street = request.POST.get("street")
        shipto_city = request.POST.get("city")
        shipto_state = request.POST.get("state")
        shipto_zip = request.POST.get("zip")
        shipto_country = request.POST.get("country")
        ship_by_date = request.POST.get("ship-by")
        deliver_by_date = request.POST.get("deliver-by")
        ords.edit_shipto_company(sid, shipto_company, shipto_attn,
                        shipto_street, shipto_city, shipto_state,
                        shipto_zip, shipto_country, ship_by_date,
                        deliver_by_date)
        url = "/orders/view-order-{0}".format(oid)
        redirect(url)
    return dict(mlist = mlist, shipto_info = shipto_info)

@route("/orders/add-order/order<oid:int>/deliver-to")
@post("/orders/add-order/order<oid:int>/deliver-to")
@view("views/orders/deliver_to")
def add_deliver_to(oid):
    check_user()
    mlist = ords.select_valid_market_order(oid)
    if mlist:
        if request.POST.get("add-company"):
            shipto_company = request.POST.get("company")
            shipto_attn = request.POST.get("attn")
            shipto_street = request.POST.get("street")
            shipto_city = request.POST.get("city")
            shipto_state = request.POST.get("state")
            shipto_zip = request.POST.get("zip")
            shipto_country = request.POST.get("country")
            ship_by_date = request.POST.get("ship-by")
            deliver_by_date = request.POST.get("deliver-by")
            ords.insert_shipto(oid, shipto_company, shipto_attn,
                               shipto_street, shipto_city,
                               shipto_state, shipto_zip,
                               shipto_country, ship_by_date,
                               deliver_by_date)
            url = "/orders/view-order-{0}".format(oid)
            redirect(url)
        return dict(mlist = mlist)
    else:
        redirect("/orders/add-order")

@route("/orders/add-order/order<oid:int>")
def reroute_add_order(oid):
    check_user()
    url = "/orders/add-order".format(oid)
    redirect(url)

@route("/orders/add-order")
@post("/orders/add-order")
@view("views/orders/add_order")
def add_order():
    check_user()
    userid = request.session["username"]
    salesteam_list = ords.select_salesteam_list()
    msku_list = ords.select_valid_mskus()
    market_list = ords.select_valid_marketplaces()
    companies = com.select_companies_with_contacts()
    if request.POST.get("add-order"):
        order_id = request.POST.get("order-id")
        marketplace = request.POST.get("marketplace")
        salesperson_id = request.POST.get("salesperson-id")
        sameship = request.POST.get("sameship")
        com_info = request.POST.get("com-info")
        company_id, contact_id = com_info.split(',')
        oid = ords.insert_market_step1(order_id, marketplace,
                                  salesperson_id, sameship, company_id,
                                  contact_id)
        url = "/orders/view-order-{0}".format(oid[0][0])
        redirect(url)
    return dict(msku_list = msku_list, err = None, new_order = None,
                market_list = market_list, userid = userid,
                companies = companies,
                salesteam_list = salesteam_list)

@route("/orders/view-order-<oid:int>")
@view("views/orders/view_order")
def view_order(oid):
    check_user()
    order_info = ords.select_order_company_info(oid)
    shipto_info = ords.select_order_shipto(oid)
    return dict(order_info = order_info, shipto_info = shipto_info)


@route("/orders")
@view("views/orders/orders_main")
def orders():
    check_user()
    all_orders = ords.select_all_orders()
    return dict(all_orders = all_orders)
