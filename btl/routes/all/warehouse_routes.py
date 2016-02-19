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
                            inv = False)
        else:
            return template("views/warehouse/new_case_box",
                            err = "UPC invalid: " + upc, inv = False)
    else:
        return template("views/warehouse/new_case_box", err = None,
                        inv = False)

@route("/warehouses/cases")
def warehouse_cases():
    case_boxes = get_case_boxes()
    return template("views/warehouse/case_boxes",
                    case_boxes = case_boxes, inv = False)

@route("/warehouses/<wh>/information")
def warehouse_pallet_locations(wh = None):
    wh_info = warehouse_information(wh)
    if wh_info:
        return template("views/warehouse/information",
                        wh_info = wh_info, inv = False)
    else:
        error404("err")


@route("/warehouses/<wh>/running-inventory")
def warehouse_pallet_locations(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    sku_count = running_inventory(wh)
    if warehouse_name:
        return template("views/warehouse/running_inventory",
                        warehouse_name = warehouse_name,
                        sku_count = sku_count, inv = False)
    else:
        error404("err")

@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    pallet_location_list = pallet_locations(wh)
    if warehouse_name:
        return template("views/warehouse/pallet_locations", warehouse_name = warehouse_name, pallet_location_list = pallet_location_list,
                        inv = False)
    else:
        error404("err")

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    warehouse_name, warehouse_lower = validate_warehouse(wh)
    if warehouse_name:
        return template("views/warehouse/wh_page",
                        warehouse_name = warehouse_name,
                        wh_link = warehouse_lower, inv = False)
    else:
        error404("err")
    
@route("/warehouses")
def warehouse():
    wh = valid_warehouses()
    valid_wh = [i[0] for i in wh]
    return template("views/warehouse/main", wh_list = valid_wh,
                    inv = False)
