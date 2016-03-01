# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bcrypt

@route("/admin/add-user")
@post("/admin/add-user")
@view("views/admin/add_user", inv = inv)
def add_user():
    check_admin()
    if request.POST.get("add-user"):
        uname = request.POST.get("user-name")
        password = request.POST.get("password")
        urole = request.POST.get("role")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user_error = insert_new_user(uname, hashed, urole)
        return dict(new_user = uname,
                    role_types = ['admin', 'user'],
                    user_error = user_error)
    return dict(new_user = None, role_types = ['admin', 'user'],
                user_error = None)

@route("/admin/add-warehouse")
@post("/admin/add-warehouse")
@view("views/admin/add_warehouse", inv = inv, wh_err = None)
def add_warehouse():
    check_admin()
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
            return dict(new_warehouse = warehouse_name,
                        wh_types = wh_types, wh_err = wh_err)
        insert_warehouse(warehouse_id, warehouse_name, street, state,
                         zip, country, warehouse_type)
        return dict(new_warehouse = warehouse_name,
                    wh_types = wh_types)
    return dict(new_warehouse = None,
                wh_types = wh_types)

# admin
@route("/admin")
@view("views/admin/admin_inv", inv = inv)
def admin():
    check_admin()
