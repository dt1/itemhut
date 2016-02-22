# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from routes.full.product_routes import *
from routes.full.warehouse_routes import *
from routes.full.vendor_routes import *
from routes.full.admin_routes import *
from routes.full.channel_routes import *
from routes.full.order_routes import *
from routes.full.incoming_routes import *

# for css, js, img, etc
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")

# home page    
@route("/")
def index():
    return template("views/home/home.tpl", inv = False)

debug(True)
run(reloader=True, host="localhost", port=8081)
