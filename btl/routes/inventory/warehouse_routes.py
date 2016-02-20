# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

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
            return template("views/warehouse/new_case_box", err = None,
                            inv = True)
        else:
            return template("views/warehouse/new_case_box",
                            err = "UPC invalid: " + upc, inv = True)
    else:
        return template("views/warehouse/new_case_box",
                        err = None, inv = True)

@route("/warehouses/cases")
def warehouse_cases():
    case_boxes = get_case_boxes()
    return template("views/warehouse/case_boxes",
                    case_boxes = case_boxes, inv = True)

@route("/warehouses/<wh>/information")
def warehouse_gen_information(wh = None):
    wh_info = warehouse_information(wh)
    if wh_info:
        return template("views/warehouse/information",
                        wh_info = wh_info, inv = True)
    else:
        error404("err")


@route("/warehouses/<wh>/running-inventory")
def warehouse_running_inventory(wh = None):
    wh_info = warehouse_information(wh)
    sku_count = running_inventory(wh)
    if wh_info:
        return template("views/warehouse/running_inventory",
                        wh_info = wh_info,
                        sku_count = sku_count, inv = True)
    else:
        error404("err")


@route("/warehouses/<wh>/update-picking-location-<pid>")
@route("/warehouses/<wh>/update-picking-location-<pid>", method="POST")
def update_picking_location(wh, pid):
    wh_info = warehouse_information(wh)
    pl_info = select_picking_location_info(pid)
    sku_upc = sku_upcs()
    if request.POST.get("update-picking-location"):
        picking_location = request.POST.get("picking-location")
        sku = request.POST.get("sku")
        qty = request.POST.get("qty")
        update_picking_location_info(pid, picking_location, sku, qty)
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
@route("/warehouses/<wh>/add-picking-location", method="POST")
def add_warehouse_picking_location(wh = None):
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
@route("/warehouses/<wh>/add-pallet-location", method="POST")
def add_pallet_location(wh):
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

@route("/warehouses/<wh>/pallets")
def warehouse_pallets(wh = None):
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template("views/warehouse/pallets",
                        wh_info = wh_info,
                        pallet_location_list = pallet_location_list,
                        inv = True)
    else:
        error404("err")

@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh = None):
    wh_info = warehouse_information(wh)
    pallet_location_list = select_pallet_locations(wh)
    if wh_info:
        return template("views/warehouse/pallet_locations",
                        wh_info = wh_info,
                        pallet_location_list = pallet_location_list,
                        inv = True)
    else:
        error404("err")

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    wh_info = warehouse_information(wh)
    return template("views/warehouse/wh_page",
                    wh_info = wh_info, inv = True)

@route("/warehouses")
def warehouse():
    wh = valid_warehouses()
    return template("views/warehouse/main", wh = wh,
                    inv = True)
