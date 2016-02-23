# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/admin/add-warehouse")
@route("/admin/add-warehouse", method="POST")
def add_warehouse():
    wh_types = select_warehouse_types()
    if request.POST.get("add-warehouse"):
        warehouse_id = request.POST.get("warehouse-id")
        warehouse_name = request.POST.get("warehouse-name")
        street = request.POST.get("street")
        state = request.POST.get("state")
        zip = request.POST.get("zip_code")
        country = request.POST.get("country")
        warehouse_type = request.POST.get("wh-type")
        wh_id = select_warehouse_id(warehouse_id)
        if wh_id:
            wh_err = "{0} already exists. Try another ID".format(warehouse_id)
            return template("views/admin/add_warehouse",
                            new_warehouse = warehouse_name, inv = True,
                            wh_types = wh_types, wh_err = wh_err)
        insert_warehouse(warehouse_id, warehouse_name, street, state,
                         zip, country, warehouse_type)
        return template("views/admin/add_warehouse",
                        new_warehouse = warehouse_name, inv = True,
                        wh_types = wh_types, wh_err = None)
    return template("views/admin/add_warehouse",
                    new_warehouse = None, inv = True,
                    wh_types = wh_types, wh_err = None)

# admin
@route("/admin")
def admin():
    return template("views/admin/admin_inv", inv = True)
