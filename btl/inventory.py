# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from routes.inventory.product_routes import *
from routes.inventory.warehouse_routes import *
from routes.inventory.vendor_routes import *
from routes.inventory.admin_routes import *
from routes.inventory.incoming_routes import *
from routes.inventory.login_routes import *
from routes.inventory.order_routes import *
from routes.inventory.company_routes import *

# for css, js, img, etc
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")

@route("/uploaded_files/invoices/<filename:path>")
def get_invoices(filename):
    return static_file(filename, root="uploaded_files/invoices/")

@route("/uploaded_files/images/<filename:path>")
def get_images(filename):
    return static_file(filename, root="uploaded_files/images/")

@route("/uploaded_files/orders/<filename:path>")
def get_images(filename):
    return static_file(filename, root="uploaded_files/orders/")


# home page    
@route("/")
def index():
    check_user()
    return template("views/home/home", inv = True)

debug(True)
run(reloader=True, host="localhost", port=8082, app=myapp)
