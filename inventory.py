# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

from routes.product_routes import *
from routes.warehouse_routes import *
from routes.vendor_routes import *
from routes.admin.admin_routes import *
from routes.incoming_routes import *
from routes.login_routes import *
from routes.order_routes import *
from routes.company_routes import *

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

@route("/uploaded_files/orders/<filename:path>")
def palletloc_files(filename):
    return static_file(filename, root="uploaded_files/palletlocs/")


# home page    
@route("/")
def index():
    check_user()
    return template("views/home/home", inv = True)

debug(True)
run(reloader=True, host="localhost", port=8082, app=myapp)
#run(host="104.236.161.137", port=8082, app=myapp)
