# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bcrypt

from routes.admin.wh.warehouse_routes import *
from routes.admin.wh.palletloc_routes import *
from routes.admin.wh.pickingloc_routes import *
from routes.admin.users import *

# admin
@route("/admin")
@view("views/admin/admin_main")
def admin():
    check_admin()
