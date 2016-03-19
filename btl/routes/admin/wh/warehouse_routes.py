# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import routes.admin.wh.wh_utils as whu

@route(whu.gen_route("/add-warehouse"))
@post(whu.gen_route("/add-warehouse"))
@view(whu.gen_view("/add_warehouse"), wh_err = None)
def add_warehouse():
    check_admin()
    wh_types = adm.select_warehouse_types()
    if request.POST.get("add-warehouse"):
        warehouse_id = request.POST.get("warehouse-id")
        warehouse_name = request.POST.get("warehouse-name")
        street = request.POST.get("street")
        state = request.POST.get("state")
        zip = request.POST.get("zip_code")
        country = request.POST.get("country")
        warehouse_type = request.POST.get("wh-type")
        wh_id = adm.select_warehouse_id(warehouse_id)

        if " " in warehouse_id:
            err = "Warehouse ID has spaces in it."
            return dict (wh_err = err,
                         new_warehouse = warehouse_name,
                         wh_types = wh_types)

        if wh_id:
            wh_err = "{0} already exists. Try another ID".format(warehouse_id)
            return dict(new_warehouse = warehouse_name,
                        wh_types = wh_types, wh_err = wh_err)
        adm.insert_warehouse(warehouse_id, warehouse_name, street,
                             state,
                         zip, country, warehouse_type)
        return dict(new_warehouse = warehouse_name,
                    wh_types = wh_types)
    return dict(new_warehouse = None,
                wh_types = wh_types)

@route(whu.gen_route("/<wh>"))
@post(whu.gen_route("/<wh>"))
@view(whu.gen_view("manage_warehouses_whinfo"))
def manage_warehouses(wh):
    check_admin()
    wh_info = adm.select_warehouse_info(wh)
    if request.POST.get("update-warehouse"):
        wh_id = request.POST.get("wh-id")
        wh_name = request.POST.get("wh-name")
        wh_street = request.POST.get("wh-street")
        wh_state = request.POST.get("wh-state")
        wh_zip = request.POST.get("wh-zip")
        wh_country = request.POST.get("wh-country")

        if " " in wh_id:
            err = "Warehouse ID has spaces in it."
            return dict (wh_info = wh_info, err = err)

        err = adm.update_warehouse_info(wh, wh_id, wh_name, wh_street,
                                        wh_state, wh_zip, wh_country)
        if err:
            err = "Warehouse id {0} already in use.".format(wh_id)
            return dict (wh_info = wh_info, err = err)
        else:
            url = "/admin/manage-warehouses/{0}".format(wh_id)
            redirect (url)

    return dict(wh_info = wh_info, err = None)

@route(whu.gen_route(""))
@view(whu.gen_view("manage_warehouses"))
def manage_warehouses():
    check_admin()
    wh_list = adm.select_warehouse_list()
    return dict(wh_list = wh_list)
