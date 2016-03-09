# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/orders/add-order/order<oid:int>/add-deliver-to")
@post("/orders/add-order/order<oid:int>/add-deliver-to")
@view("views/orders/add_deliver_to")
def add_deliver_to(oid):
    mlist = ords.select_valid_markter_order(oid)
    if mlist:
        if request.POST.get("another-company"):
            shipto_company = request.POST.get("company")
            shipto_attn = request.POST.get("attn")
            shipto_street = request.POST.get("street")
            shipto_city = request.POST.get("city")
            shipto_state = request.POST.get("state")
            shipto_zip = request.POST.get("zip")
            shipto_country = request.POST.get("country")
            ship_by_date = request.POST.get("ship-by")
            deliver_by_date = request.POST.get("deliver-by")
        return dict(mlist = mlist)
    else:
        redirect("/orders/add-order")

@route("/orders/add-order/order<oid:int>/deliver-to")
@post("/orders/add-order/order<oid:int>/deliver-to")
@view("views/orders/deliver_to")
def add_deliver_to(oid):
    mlist = ords.select_valid_markter_order(oid)
    if mlist:
        if request.POST.get("another-company") or request.POST.get("done"):
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
            if request.POST.get("another-company"):
                url = "/orders/add-order/order{0}/add-deliver-to".format(oid)
                redirect(url)
            else:
                return "done"
        return dict(mlist = mlist)
    else:
        redirect("/orders/add-order")

@route("/orders/add-order/order<oid:int>")
def reroute_add_order(oid):
    url = "/orders/add-order".format(oid)
    redirect(url)

@route("/orders/add-order")
@post("/orders/add-order")
@view("views/orders/add_order")
def add_order():
    check_user()
    userid = request.session["username"]
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
        url = "/orders/add-order/order{0}".format(oid[0][0])
        redirect(url)
    return dict(msku_list = msku_list, err = None, new_order = None,
                market_list = market_list, userid = userid,
                companies = companies)

@route("/orders")
@view("views/orders/orders_main")
def orders():
    check_user()
    orders = select_all_orders()
    return dict(orders = orders)
