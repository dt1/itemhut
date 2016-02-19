# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/admin/add-warehouse")
def add_warehouse():
    return template("views/admin/add_warehouse",
                    new_warehouse = None, inv = True)

# admin
@route("/admin")
def admin():
    return template("views/admin/admin", inv = True)
