# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

# product routes
from routes.product.main_product_page import *
from routes.product.products import *
from routes.product.kits import *

# warehouse routes
from routes.warehouse.warehouse_routes import *

# vendor routes
from routes.vendor.vendor_routes import *

# admin routes
from routes.admin.admin_routes import *

# incoming routes
from routes.incoming.incoming_routes import *

# login routes
from routes.login.login_routes import *

# order routes
from routes.order.order_routes import *

# company routes
from routes.company.company_routes import *

# tools routes
from routes.tools.tools_routes import *

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
@check_user
def index():
    return template("views/home/home", inv = True)

debug(True)
run(reloader=True, host="localhost", port=8082, app=myapp)
