# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/incoming/update-order-<oid>")
@route("/incoming/update-order-<oid>", method="POST")
def update_incoming_order(oid):
    if request.POST.get("arrived"):
        set_order_complete(oid)
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        qty = request.POST.get("qty")
        insert_incoming_order_product(oid, upc, qty)
    products = select_incoming_product(oid)
    upc_list = get_order_upc_candidates(oid)
    order_info = select_incoming_order_data(oid)
    return template("views/incoming/update_incoming_order", inv = False,
                    invoice_added = False, order_info = order_info,
                    upc_list = upc_list, products = products)

@route("/incoming/all-records")
def all_records():
    orders = select_all_incoming_orders()
    return template("views/incoming/incoming_main", inv = False,
                    orders = orders)

@route("/incoming/add-record")
@route("/incoming/add-record", method="POST")
def add_record():
    if request.POST.get("add-record"):
        invoice = request.POST.get("invoice")
        vendor_id = request.POST.get("vendor-id")
        order_date = request.POST.get("order-date")
        eta = request.POST.get("eta")
        invoice_file = request.POST.get("invoice-file")
        insert_invoice_data(invoice, vendor_id, order_date, eta,
                        invoice_file)
        return template("views/incoming/add_record", inv = False,
                        invoice_added = invoice)
    return template("views/incoming/add_record", inv = False,
                    invoice_added = False)

@route("/incoming")
def incoming():
    orders = select_incoming_orders()
    return template("views/incoming/incoming_main", inv = False,
                    orders = orders)
