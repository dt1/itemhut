# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from full_route_utils import *

# warehouse pages:
@route("/warehouses/cases/new-config")
@post("/warehouses/cases/new-config")
@view("views/warehouse/add_case_box", inv = inv, err = None)
def new_warehouse_case_config():
    check_user()
    upc_list = get_upcs()
    if request.POST.get("add-config"):
        upc = request.POST.get("upc")
        box_qty = request.POST.get("box-qty")
        case_qty = request.POST.get("case-qty")
        if int(upc) in upc_list:
            insert_new_case_box(upc, box_qty, case_qty)
            return dict(upc_list = upc_list)
        else:
            err = "UPC invalid: {0}".format(upc)
            return dict(upc_list = upc_list, err = err)
    else:
        return dict(upc_list = upc_list)

@route("/warehouses/cases")
@view("views/warehouse/case_boxes", inv = inv)
def warehouse_cases():
    check_user()
    case_boxes = get_case_boxes()
    return dict(case_boxes = case_boxes)

@route("/warehouses/<wh>/information")
def warehouse_gen_information(wh):
    check_user()
    wh_info = warehouse_information(wh)
    if wh_info[0][6] == 'B&M':
        return template("views/warehouse/information",
                        wh_info = wh_info, inv = inv)
    elif wh_info[0][6] == '3PL':
        return template("views/warehouse/information_3pl",
                        wh_info = wh_info, inv = inv)
    else:
        return error404("err")

@route("/warehouses/<wh>/add-product")
@post("/warehouses/<wh>/add-product")
@view("views/warehouse/add_3pl_product", inv = inv, upc = None)
def warehouse_add_product(wh):
    check_user()
    wh_info = warehouse_information(wh)
    sku_upc = select_sku_upc_not_in_3pl(wh)
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        qty = request.POST.get("qty")
        insert_3pl_product(wh, upc, qty)
        return dict(wh_info = wh_info, sku_upc = sku_upc, upc=upc)
    if wh_info[0][6] == '3PL':
        return dict(wh_info = wh_info, sku_upc = sku_upc)
    else:
        return error404("err")

@route("/warehouses/<wh>/update-running-inventory-<sku>")
@post("/warehouses/<wh>/update-running-inventory-<sku>")
@view("views/warehouse/update_running_3pl_inventory", inv = inv)
def update_warehouse_running_inventory(wh, sku):
    check_user()
    wh_info = warehouse_information(wh)
    sku_count = select_3pl_running_inventory_sku(wh, sku)
    if wh_info[0][6] == '3PL' and sku_count:
        if request.POST.get("update-qty"):
            qty = request.POST.get("qty")
            picking_loc = sku_count[0][3]
            update_3pl_running_inventory(picking_loc, qty)
            url = "/warehouses/{0}/update-running-inventory-{1}".format(wh, sku)
            redirect(url)
        return dict(sku_count = sku_count, wh_info = wh_info)
    else:
        return error404("err")

@route("/warehouses/<wh>/running-inventory")
def warehouse_running_inventory(wh):
    check_user()
    wh_info = warehouse_information(wh)
    if wh_info[0][6] == 'B&M':
        sku_count = running_inventory(wh)
        return template("views/warehouse/running_inventory",
                        sku_count = sku_count,
                        wh_info = wh_info, inv = inv)
    elif wh_info[0][6] == '3PL':
        sku_count = select_3pl_running_inventory(wh)
        return template("views/warehouse/running_3pl_inventory",
                        sku_count = sku_count,
                        wh_info = wh_info, inv = inv)
    else:
        return error404("err")


@route("/warehouses/<wh>/update-picking-location-<pid>")
@post("/warehouses/<wh>/update-picking-location-<pid>")
@view("views/warehouse/update_picking_location", inv = inv)
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
        url = "/warehouses/{0}/update-picking-location-{1}".format(wh, pid)
        redirect(url)
        return dict(pid = pid, wh_info = wh_info, sku_upc = sku_upc,
                    pl_info = pl_info)
    if wh_info:
        return dict(pid = pid, wh_info = wh_info, sku_upc = sku_upc,
                    pl_info = pl_info)
    else:
        return error404("err")


@route("/warehouses/<wh>/add-picking-location")
@post("/warehouses/<wh>/add-picking-location")
@view("views/warehouse/add_picking_location", inv = inv)
def add_warehouse_picking_location(wh):
    check_user()
    wh_info = warehouse_information(wh)
    sku_upc = sku_upcs()
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
@view("views/warehouse/picking_locations", inv = inv)
def warehouse_picking_locations(wh):
    check_user()
    wh_info = warehouse_information(wh)
    picking_location_list = select_picking_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    picking_location_list = picking_location_list)
    else:
        return error404("err")

@route("/warehouses/<wh>/move-to-picking-<pid>")
def move_to_pickingloc(wh, pid):
    add_full_pallet_to_pickingloc(wh, pid)
    url = "/warehouses/{0}/pallet-locations".format(wh)
    redirect(url)
    
@route("/warehouses/<wh>/delete-pallet-location-<pid>")
def delete_pallet_location(wh, pid):
    delete_pallet_loc_cascades(pid)
    url = "/warehouses/{0}/pallet-locations".format(wh)
    redirect(url)
        
## pallet locations
@route("/warehouses/<wh>/add-pallet-location")
@post("/warehouses/<wh>/add-pallet-location")
@view("views/warehouse/add_pallet_location", inv = inv)
def add_pallet_location(wh):
    check_user()
    wh_info = warehouse_information(wh)
    if request.POST.get("add-pallet-location"):
        location_name = request.POST.get("location-name")
        insert_pallet_location(wh, location_name)
        return dict(wh_info = wh_info, location_name = location_name)
    if wh_info:
        return dict(wh_info = wh_info, location_name = None)
    else:
        return error404("err")

@route("/warehouses/<wh>/update-pallet-<pid>/delete-case-<cid>")
def delete_case_from_pallet(wh, pid, cid):
    delete_pallet_case(pid, cid)
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
    redirect(url)
        
# pallets
@route("/warehouses/<wh>/update-pallet-<pid>")
@post("/warehouses/<wh>/update-pallet-<pid>")
@view("views/warehouse/update_pallet", inv = inv, err = None)
def warehouse_pallets(wh, pid):
    check_user()
    wh_info = warehouse_information(wh)
    case_boxes = select_case_boxes(pid)
    pallet_info = select_pallet_info(pid)
    if request.POST.get("update-loc"):
        ploc = request.POST.get("pallet-location")
        pl_id = pallet_info[0][7]
        update_pallet_location(pl_id, ploc)
        url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid)
        redirect(url)
    if request.POST.get("add-case"):
        cid = request.POST.get("case-id")
        qty = request.POST.get("qty")
        if cid:
            insert_pallet_case(pid, cid, qty)
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
def add_pallet_to_loc(wh, pl_id):
    new_pallet = insert_new_pallet_palletloc(pl_id)
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, new_pallet[0][0])
    redirect(url)
    
@route("/warehouses/<wh>/create-pallet")
def warehouse_pallets(wh):
    check_user()
    pid = generate_pallet_id()
    url = "/warehouses/{0}/update-pallet-{1}".format(wh, pid[0][0])
    redirect(url)

@route("/warehouses/<wh>/pallets")
@view("views/warehouse/pallets", inv = inv)
def warehouse_pallets(wh):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    pallet_location_list = pallet_location_list)
    else:
        return error404("err")

@route("/warehouses/<wh>/pallet-locations/update-loc-<pid>")
@view("views/warehouse/pallet_locations", inv = inv)
def warehouse_pallet_locations(wh, pid):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template(wh_info = wh_info,
                        pallet_location_list = pallet_location_list)
    else:
        return error404("err")
        
@route("/warehouses/<wh>/pallet-locations")
@view("views/warehouse/pallet_locations", inv = inv)
def warehouse_pallet_locations(wh):
    check_user()
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return dict(wh_info = wh_info,
                    pallet_location_list = pallet_location_list)
    
@route("/warehouses/<wh>")
def warehouse_n(wh):
    check_user()
    wh_info = warehouse_information(wh)
    if wh_info:
        if wh_info[0][6] == 'B&M':
            return template("views/warehouse/wh_page",
                            wh_info = wh_info, inv = inv)
        if wh_info[0][6] == '3PL':
            return template("views/warehouse/wh3pl_page",
                            wh_info = wh_info, inv = inv)
        
@route("/warehouses")
@view("views/warehouse/warehouse_main", inv = inv)
def warehouse():
    check_user()
    wh = valid_warehouses()
    running_inventory = select_all_running_inventory()
    return dict(wh = wh, running_inventory = running_inventory)
