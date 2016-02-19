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
def warehouse_pallet_locations(wh = None):
    wh_list = validate_warehouse(wh)
    sku_count = running_inventory(wh)
    if wh_list:
        return template("views/warehouse/running_inventory",
                        wh_list = wh_list,
                        sku_count = sku_count, inv = True)
    # else:
    #     error404("err")


@route("/warehouses/<wh>/pallet-locations")
def warehouse_pallet_locations(wh = None):
    wh_list = validate_warehouse(wh)
    pallet_location_list = pallet_locations(wh)
    if wh_list:
        return template("views/warehouse/pallet_locations",
                        wh_list = wh_list,
                        pallet_location_list = pallet_location_list,
                        inv = True)
    else:
        error404("err")

@route("/warehouses/<wh>")
def warehouse_n(wh = None):
    wh_list = validate_warehouse(wh)
    if wh_list:
        return template("views/warehouse/wh_page", wh_list = wh_list, inv = True)
    else:
        error404("err")
    
@route("/warehouses")
def warehouse():
    wh = valid_warehouses()
    return template("views/warehouse/main", wh = wh,
                    inv = True)
