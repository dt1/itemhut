# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bcrypt

@route("/admin/update-user-password-<uid>")
@post("/admin/update-user-password-<uid>")
@view("views/admin/user/update_user_password", err = None)
@check_user
@check_admin
def update_user_password(uid):
    if request.POST.get("update-password"):
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            admus.update_user_password(uid, hashed)
        else:
            err = "Passwords do not match"
            return dict(err = err, uid = uid)

        url = "/admin/manage-users"
        redirect(url)
    return dict(uid = uid)


@route("/admin/update-user-<uid>")
@post("/admin/update-user-<uid>")
@view("views/admin/user/update_user", new_user = None,
      user_error = None)
@check_user
@check_admin
def add_user(uid):
    role_types = admus.select_valid_roles()
    user_types = admus.select_valid_usertypes()
    user_info = admus.select_user_info(uid)
    if request.POST.get("update-user"):
        uname = request.POST.get("user-name")
        real_name = request.POST.get("real-name")
        urole = request.POST.get("urole")
        utype = request.POST.get("utype")

        user_error = admus.update_user(uid, uname, real_name, utype,
                                     urole)

        url = "/admin/update-user-{0}".format(uname)
        redirect(url)
    return dict(role_types = role_types,
                user_types = user_types, user_info = user_info)

@route("/admin/manage-users")
@post("/admin/manage-users")
@view("views/admin/user/manage_users")
@check_user
@check_admin
def manage_users():
    usrs = admus.select_users()
    role_types = admus.select_valid_roles()
    user_types = admus.select_valid_usertypes()
    return dict(usrs = usrs, role_types = role_types,
                user_types = user_types)

@route("/admin/add-user")
@post("/admin/add-user")
@view("views/admin/user/add_user", new_user = None, user_error = None)
@check_user
@check_admin
def add_user():
    role_types = admus.select_valid_roles()
    user_types = admus.select_valid_usertypes()
    if request.POST.get("add-user"):
        uname = request.POST.get("user-name")
        password = request.POST.get("password")
        real_name = request.POST.get("real-name")
        urole = request.POST.get("urole")
        utype = request.POST.get("utype")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user_error = admus.insert_new_user(uname, hashed, real_name,
                                         utype, urole)
        return dict(new_user = uname,
                    role_types = role_types,
                    user_error = user_error,
                    user_types = user_types)
    return dict(role_types = role_types,
                user_types = user_types)
