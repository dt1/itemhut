# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

# warehouse pages:
@route("/warehouses/cases/new-config")
@post("/warehouses/cases/new-config")
def new_warehouse_case_config():
    check_user()
    upc_list = get_upcs()
    if request.POST.get("add-config"):
        upc = request.POST.get("upc")
        box_qty = request.POST.get("box-qty")
        case_qty = request.POST.get("case-qty")
        if int(upc) in upc_list:
            insert_new_case_box(upc, box_qty, case_qty)
            return template("views/warehouse/add_case_box", err = None,
                            inv = True, upc_list = upc_list)
        else:
            return template("views/warehouse/add_case_box",
                            err = "UPC invalid: " + upc, inv = True,
                            upc_list = upc_list)
    else:
        return template("views/warehouse/add_case_box",
                        err = None, inv = True,
                        upc_list = upc_list)

@route("/warehouses/cases")
def warehouse_cases():
    check_user()
    case_boxes = get_case_boxes()
    return template("views/warehouse/case_boxes",
                    case_boxes = case_boxes, inv = True)

@route("/warehouses/<wh>/information")
def warehouse_gen_information(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    if wh_info[0][6] == 'B&M':
        return template("views/warehouse/information",
                        wh_info = wh_info, inv = True)
    elif wh_info[0][6] == '3PL':
        return template("views/warehouse/information_3pl",
                        wh_info = wh_info, inv = True)
    else:
        error404("err")


@route("/warehouses/<wh>/add-product")
@post("/warehouses/<wh>/add-product")
def warehouse_add_product(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    sku_upc = select_sku_upc_not_in_3pl(wh)
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        qty = request.POST.get("qty")
        insert_3pl_product(wh, upc, qty)
        return template("views/warehouse/add_3pl_product",
                        wh_info = wh_info, inv = True,
                        sku_upc = sku_upc, upc=upc)
    if wh_info[0][6] == '3PL':
        return template("views/warehouse/add_3pl_product",
                        wh_info = wh_info, inv = True,
                        sku_upc = sku_upc, upc=None)
    else:
        error404("err")


@route("/warehouses/<wh>/update-running-inventory-<sku>")
@post("/warehouses/<wh>/update-running-inventory-<sku>")
def update_warehouse_running_inventory(wh, sku):
    check_user()
    wh_info = warehouse_information(wh)
    sku_count = select_3pl_running_inventory_sku(wh, sku)
    if wh_info[0][6] == '3PL' and sku_count:
        if request.POST.get("update-qty"):
            qty = request.POST.get("qty")
            picking_loc = sku_count[0][3]
            update_3pl_running_inventory(picking_loc, qty)
            redirect("/warehouses/{0}/update-running-inventory-{1}".format(wh, sku))
        return template("views/warehouse/update_running_3pl_inventory",
                        sku_count = sku_count,
                        wh_info = wh_info, inv = True)
    else:
        error404("err")

@route("/warehouses/<wh>/running-inventory")
def warehouse_running_inventory(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    sku_count = running_inventory(wh)
    if wh_info[0][6] == 'B&M':
        return template("views/warehouse/running_inventory",
                        sku_count = sku_count,
                        wh_info = wh_info, inv = True)
    elif wh_info[0][6] == '3PL':
        return template("views/warehouse/running_3pl_inventory",
                        sku_count = sku_count,
                        wh_info = wh_info, inv = True)
    else:
        error404("err")


@route("/warehouses/<wh>/update-picking-location-<pid>")
@post("/warehouses/<wh>/update-picking-location-<pid>")
def update_picking_location(wh, pid):
    check_user()
    wh_info = warehouse_information(wh)
    pl_info = select_picking_location_info(pid)
    sku_upc = sku_upcs()
    if request.POST.get("update-picking-location"):
        picking_location = request.POST.get("picking-location")
        upc = request.POST.get("upc")
        qty = request.POST.get("qty")
        update_picking_location_info(pid, picking_location, upc, qty)
        redirect("/warehouses/{0}/update-picking-location-{1}".format(wh, pid))
        return template("views/warehouse/update_picking_location",
                        pid = pid, wh_info = wh_info,
                        sku_upc = sku_upc, inv = True, pl_info = pl_info)
    if wh_info:
        return template("views/warehouse/update_picking_location",
                        pid = pid, wh_info = wh_info,
                        sku_upc = sku_upc, inv = True, pl_info = pl_info)
    else:
        error404("err")


@route("/warehouses/<wh>/add-picking-location")
@post("/warehouses/<wh>/add-picking-location")
def add_warehouse_picking_location(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    sku_upc = sku_upcs()
    if request.POST.get("add-picking-location"):
        picking_location = request.POST.get("picking-location")
        sku = request.POST.get("sku")
        qty = request.POST.get("qty")
        message = insert_picking_location(wh, picking_location, sku, qty)
        return template("views/warehouse/add_picking_location",
                        wh_info = wh_info, sku_upc = sku_upc,
                        inv = True, message = message)
    if wh_info:
        return template("views/warehouse/add_picking_location",
                        wh_info = wh_info, sku_upc = sku_upc,
                        inv = True, message = None)
    else:
        error404("err")

@route("/warehouses/<wh>/picking-locations")
def warehouse_picking_locations(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    picking_location_list = select_picking_locations(wh)
    if wh_info:
        return template("views/warehouse/picking_locations",
                        wh_info = wh_info,
                        picking_location_list = picking_location_list,
                        inv = True)
    else:
        error404("err")

## pallet locations
@route("/warehouses/<wh>/add-pallet-location")
@post("/warehouses/<wh>/add-pallet-location")
def add_pallet_location(wh):
    check_user()
    wh_info = warehouse_information(wh)
    if request.POST.get("add-pallet-location"):
        location_name = request.POST.get("location-name")
        insert_pallet_location(wh, location_name)
        return template("views/warehouse/add_pallet_location",
                        wh_info = wh_info,
                        inv = True, location_name = location_name)
    if wh_info:
        return template("views/warehouse/add_pallet_location",
                        wh_info = wh_info,
                        inv = True, location_name = None)
    else:
        error404("err")

# pallets
@route("/warehouses/<wh>/update-pallet-<pid>")
@post("/warehouses/<wh>/update-pallet-<pid>")
def warehouse_pallets(wh, pid):
    check_user()
    wh_info = warehouse_information(wh)
    case_boxes = select_case_boxes(pid)
    pallet_info = select_pallet_info(pid)
    if request.POST.get("add-case"):
        ploc = request.POST.get("pallet-location")
        cid = request.POST.get("case-id")
        qty = request.POST.get("qty")
        pl_id = pallet_info[0][6]
        if cid:
            insert_pallet_case(pid, cid, qty)
            update_pallet_location(pl_id, ploc)
            url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
            redirect(url)
        else:
            err = "Please enter a case"
            return template("views/warehouse/update_pallet",
                        wh_info = wh_info,
                        inv = True, wh = wh, case_boxes = case_boxes,
                        pallet_info = pallet_info, pid = pid,
                        err = err)
    if wh_info:
        return template("views/warehouse/update_pallet",
                        wh_info = wh_info,
                        inv = True, wh = wh, case_boxes = case_boxes,
                        pallet_info = pallet_info, pid = pid,
                        err = None)

@route("/warehouses/<wh>/create-pallet")
def warehouse_pallets(wh):
    check_user()
    pid = generate_pallet_id()
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid[0][0])
    redirect(url)

@route("/warehouses/<wh>/pallets")
def warehouse_pallets(wh):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template("views/warehouse/pallets",
                        wh_info = wh_info,
                        pallet_location_list = pallet_location_list,
                        inv = True)
    else:
        error404("err")


@route("/warehouses/<wh>/pallet-locations/update-loc-<pid>")
def warehouse_pallet_locations(wh, pid):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template("views/warehouse/pallet_locations",
                        wh_info = wh_info,
                        pallet_location_list = pallet_location_list,
                        inv = True)
    else:
        return error404("err")
        
@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template("views/warehouse/pallet_locations",
                        wh_info = wh_info,
                        pallet_location_list = pallet_location_list,
                        inv = True)

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    check_user()
    wh_info = warehouse_information(wh)
    if wh_info:
        if wh_info[0][6] == 'B&M':
            return template("views/warehouse/wh_page",
                            wh_info = wh_info, inv = True)
        if wh_info[0][6] == '3PL':
            return template("views/warehouse/wh3pl_page",
                            wh_info = wh_info, inv = True)
        
@route("/warehouses")
def warehouse():
    check_user()
    wh = valid_warehouses()
    return template("views/warehouse/warehouse_main", wh = wh,
                    inv = True)
