# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

def gen_view(v):
    return "views/warehouse/{0}".format(v)

# warehouse pages:
@route("/warehouses/<wh>/qc/scan-<oid>")
@view(gen_view("scan_order"), err = None)
@check_user
@check_warehouse_user
def quality_control(wh, oid):
    order = whs.select_order_to_scan(oid)
    return dict(order = order, wh = wh, oid = oid)

@route("/warehouses/<wh>/qc")
@view(gen_view("qc"), err = None)
@check_user
@check_warehouse_user
def quality_control(wh):
    orders = whs.select_outbound_orders(wh)
    return dict(orders = orders, wh = wh)

@route("/warehouses/cases/new-config")
@post("/warehouses/cases/new-config")
@view(gen_view("add_case_box"), err = None)
@check_user
@check_warehouse_user
def new_warehouse_case_config():
    upc_list = prd.get_upcs()
    if request.POST.get("add-config"):
        upc = request.POST.get("upc")
        box_qty = request.POST.get("box-qty")
        case_qty = request.POST.get("case-qty")
        if int(upc) in upc_list:
            prd.insert_new_case_box(upc, box_qty, case_qty)
            return dict(upc_list = upc_list)
        else:
            err = "UPC invalid: {0}".format(upc)
            return dict(upc_list = upc_list, err = err)
    else:
        return dict(upc_list = upc_list)

@route("/warehouses/cases")
@view(gen_view("case_boxes"))
@check_user
@check_warehouse_user
def warehouse_cases():
    case_boxes = whs.get_case_boxes()
    return dict(case_boxes = case_boxes)

@route("/warehouses/<wh>/information")
@check_user
@check_warehouse_user
def warehouse_gen_information(wh):
    wh_info = whs.warehouse_information(wh)
    try:
       wh_info[0][6]
    except:
        return error404("err")
       
    if wh_info[0][6] == 'B&M':
        return template(gen_view("information"),
                        wh_info = wh_info)
    elif wh_info[0][6] == '3PL':
        return template(gen_view("information_3pl"),
                        wh_info = wh_info)

@route("/warehouses/<wh>/add-product")
@post("/warehouses/<wh>/add-product")
@view(gen_view("add_3pl_product"), upc = None)
@check_user
@check_warehouse_user
def warehouse_add_product(wh):
    wh_info = whs.warehouse_information(wh)
    sku_upc = whs.select_sku_upc_not_in_3pl(wh)
    try:
       wh_info[0][6]
    except:
        return error404("err")

    if wh_info[0][6] == '3PL':
        if request.POST.get("add-product"):
            upc = request.POST.get("upc")
            qty = request.POST.get("qty")
            whs.insert_3pl_product(wh, upc, qty)
            return dict(wh_info = wh_info, sku_upc = sku_upc, upc=upc)
        return dict(wh_info = wh_info, sku_upc = sku_upc)

@route("/warehouses/<wh>/update-running-inventory-<sku>")
@post("/warehouses/<wh>/update-running-inventory-<sku>")
@view(gen_view("update_running_3pl_inventory"))
@check_user
@check_warehouse_user
def update_warehouse_running_inventory(wh, sku):
    wh_info = whs.warehouse_information(wh)
    sku_count = whs.select_3pl_running_inventory_sku(wh, sku)
    try:
       wh_info[0][6]
    except:
        return error404("err")

    if wh_info[0][6] == '3PL' and sku_count:
        if request.POST.get("update-qty"):
            qty = request.POST.get("qty")
            picking_loc = sku_count[0][3]
            whs.update_3pl_running_inventory(picking_loc, qty)
            url = "/warehouses/{0}/update-running-inventory-{1}".format(wh, sku)
            redirect(url)
        return dict(sku_count = sku_count, wh_info = wh_info)

@route("/warehouses/<wh>/running-inventory")
@check_user
@check_warehouse_user
def warehouse_running_inventory(wh):
    wh_info = whs.warehouse_information(wh)
    try:
       wh_info[0][6]
    except:
        return error404("err")

    if wh_info[0][6] == 'B&M':
        sku_count = whs.running_inventory(wh)
        return template(gen_view("running_inventory"),
                        sku_count = sku_count,
                        wh_info = wh_info)
    elif wh_info[0][6] == '3PL':
        sku_count = whs.select_3pl_running_inventory(wh)
        return template(gen_view("running_3pl_inventory"),
                        sku_count = sku_count,
                        wh_info = wh_info)

@route("/warehouses/<wh>/update-picking-location-<pid>")
@post("/warehouses/<wh>/update-picking-location-<pid>")
@view(gen_view("update_picking_location"))
@check_user
@check_warehouse_user
def update_picking_location(wh, pid):
    wh_info = whs.warehouse_information(wh)
    pl_info = whs.select_picking_location_info(pid)
    sku_upc = prd.sku_upcs()
    if wh_info:
        if request.POST.get("update-picking-location"):
            picking_location = request.POST.get("picking-location")
            upc = request.POST.get("upc")
            qty = request.POST.get("qty")
            whs.update_picking_location_info(pid, picking_location, upc, qty)
            url = "/warehouses/{0}/update-picking-location-{1}".format(wh, pid)
            redirect(url)
        return dict(pid = pid, wh_info = wh_info, sku_upc = sku_upc,
                    pl_info = pl_info)
    else:
        return error404("err")


@route("/warehouses/<wh>/add-picking-location")
@post("/warehouses/<wh>/add-picking-location")
@view(gen_view("add_picking_location"))
@check_user
@check_warehouse_user
def add_warehouse_picking_location(wh):
    wh_info = whs.warehouse_information(wh)
    sku_upc = prd.sku_upcs()
    if request.POST.get("add-picking-location"):
        picking_location = request.POST.get("picking-location")
        sku = request.POST.get("sku")
        qty = request.POST.get("qty")
        message = insert_picking_location(wh, picking_location, sku, qty)
        return dict(wh_info = wh_info, sku_upc = sku_upc,
                    message = message)
    if wh_info:
        return dict(wh_info = wh_info, sku_upc = sku_upc,
                    message = None)
    else:
        return error404("err")

@route("/warehouses/<wh>/picking-locations")
@view(gen_view("picking_locations"))
@check_user
@check_warehouse_user
def warehouse_picking_locations(wh):
    wh_info = whs.warehouse_information(wh)
    picking_location_list = whs.select_picking_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    picking_location_list = picking_location_list)
    else:
        return error404("err")

@route("/warehouses/<wh>/move-to-picking-<pid>")
@check_user
@check_warehouse_user
def move_to_pickingloc(wh, pid):
    if pid != "None":
        whs.add_full_pallet_to_pickingloc(wh, pid)
    url = "/warehouses/{0}/pallet-locations".format(wh)
    redirect(url)
        
## pallet locations
@route("/warehouses/<wh>/add-pallet-location")
@post("/warehouses/<wh>/add-pallet-location")
@view(gen_view("add_pallet_location"))
@check_user
@check_warehouse_user
def add_pallet_location(wh):
    wh_info = whs.warehouse_information(wh)
    if wh_info:
        if request.POST.get("add-pallet-location"):
            location_name = request.POST.get("location-name")
            whs.insert_pallet_location(wh, location_name)
            return dict(wh_info = wh_info, location_name = location_name)
        return dict(wh_info = wh_info, location_name = None)
    else:
        return error404("err")

@route("/warehouses/<wh>/update-pallet-<pid>/delete-case-<cid>")
@check_user
@check_warehouse_user
def delete_case_from_pallet(wh, pid, cid):
    whs.delete_pallet_case(pid, cid)
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
    redirect(url)
        
# pallets
@route("/warehouses/<wh>/update-pallet-<pid>")
@post("/warehouses/<wh>/update-pallet-<pid>")
@view(gen_view("update_pallet"), err = None)
@check_user
@check_warehouse_user
def warehouse_pallets(wh, pid):
    wh_info = whs.warehouse_information(wh)
    case_boxes = whs.select_case_boxes(pid)
    pallet_info = whs.select_pallet_info(pid)
    if request.POST.get("update-loc"):
        ploc = request.POST.get("pallet-location")
        pl_id = pallet_info[0][7]
        whs.update_pallet_location(pl_id, ploc)
        url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
        redirect(url)
    if request.POST.get("add-case"):
        cid = request.POST.get("case-id")
        qty = request.POST.get("qty")
        if cid:
            whs.insert_pallet_case(pid, cid, qty)
            url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
            redirect(url)
        else:
            err = "Please enter a case"
            return dict(wh_info = wh_info,
                         wh = wh, case_boxes = case_boxes,
                        pallet_info = pallet_info, pid = pid,
                        err = err)
    if wh_info:
        return dict(wh_info = wh_info,
                         wh = wh, case_boxes = case_boxes,
                        pallet_info = pallet_info, pid = pid)

@route("/warehouses/<wh>/add-pallet-to-ploc-<pl_id>")
@check_user
@check_warehouse_user
def add_pallet_to_loc(wh, pl_id):
    new_pallet = whs.insert_new_pallet_palletloc(pl_id)
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, new_pallet[0][0])
    redirect(url)
    
@route("/warehouses/<wh>/create-pallet")
@check_user
@check_warehouse_user
def warehouse_pallets(wh):
    pid = whs.generate_pallet_id(wh)
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid[0][0])
    redirect(url)

@route("/warehouses/<wh>/pallets")
@view(gen_view("pallets"))
@check_user
@check_warehouse_user
def warehouse_pallets(wh):
    wh_info = whs.warehouse_information(wh)
    pallet_location_list = whs.select_pallet_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    pallet_location_list = pallet_location_list)
    else:
        return error404("err")

@route("/warehouses/<wh>/pallet-locations/update-loc-<pid>")
@view(gen_view("pallet_locations"))
@check_user
@check_warehouse_user
def warehouse_pallet_locations(wh, pid):
    wh_info = whs.warehouse_information(wh)
    pallet_location_list = whs.select_pallet_locations(wh)
    if wh_info:
        return template(wh_info = wh_info,
                        pallet_location_list = pallet_location_list)
    else:
        return error404("err")
        
@route("/warehouses/<wh>/pallet-locations")
@view(gen_view("pallet_locations"))
@check_user
@check_warehouse_user
def warehouse_pallet_locations(wh):
    wh_info = whs.warehouse_information(wh)
    pallet_location_list = whs.select_pallet_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    pallet_location_list = pallet_location_list)

@route("/warehouses/<wh>")
@check_user
@check_warehouse_user
def warehouse_n(wh):
    wh_info = whs.warehouse_information(wh)
    try :
        wh_info[0][6]
    except:
        return error404("err")

    if wh_info[0][6] == 'B&M':
        sku_count = whs.running_inventory(wh)
        return template(gen_view("running_inventory"),
                        sku_count = sku_count, wh_info = wh_info)
    elif wh_info[0][6] == '3PL':
        sku_count = whs.select_3pl_running_inventory(wh)
        return template(gen_view("running_3pl_inventory"),
                        sku_count = sku_count, wh_info = wh_info)
        
@route("/warehouses")
@view(gen_view("warehouse_main"))
@check_user
@check_warehouse_user
def warehouse():
    wh = whs.valid_warehouses()
    running_inventory = whs.select_all_running_inventory()
    return dict(wh = wh, running_inventory = running_inventory)
