# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.incoming.incoming as icm

def gen_route(r):
    return "/incoming/{0}".format(r)

def gen_view(v):
    return "views/incoming/{0}".format(v)

@route(gen_route("update-order-<oid>"))
@post(gen_route("update-order-<oid>"))
@view(gen_view("update_incoming_order"))
@check_user
def update_incoming_order(oid):
    d = {"oid": oid}
    L = ["upc", "qty"]
    if request.POST.get("arrived"):
        icm.set_order_complete(oid)
    if request.POST.get("add-product"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        icm.insert_incoming_order_product(d)
    products = icm.select_incoming_product(oid)
    upc_list = icm.get_order_upc_candidates(oid)
    order_info = icm.select_incoming_order_data(oid)
    return dict(invoice_added = False, order_info = order_info,
                upc_list = upc_list, products = products)



@route(gen_route("all-records"))
@view(gen_view("incoming_main"))
@check_user
def all_records():
    orders = icm.select_all_incoming_orders()
    return dict(orders = orders)

@route(gen_route("add-record"))
@post(gen_route("add-record"))
@view(gen_view("add_record"))
@check_user
def add_record():
    L = ["invoice", "vendor-id", "order-date", "eta", "invoice-file"]
    if request.POST.get("add-record"):
        d = {i : request.POST.get(i) for i in L}
        save_path = "uploaded_files/invoices/{0}".format(d["invoice-file"])
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        invoice_file.save(save_path, overwrite=True)

        f_path = "{0}/{1}".format(invoice_file, invoice_file.filename)
        d["f-path"] = f_path
        icm.insert_invoice_data(d)
    
        return dict(invoice_added = invoice)
        
    return dict(invoice_added = False)

@route("/incoming")
@view(gen_view("incoming_main"))
@check_user
def incoming():
    orders = icm.select_incoming_orders()
    return dict(orders = orders)
