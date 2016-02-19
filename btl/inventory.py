# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from routes.product_routes import *
from routes.warehouse_routes import *
from routes.vendor_routes import *
from routes.admin_routes import *

@error(404)
def error404(err):
    return "404; please press the back button"

# for css, js, img, etc
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")

# home page    
@route("/")
def index():
    return template("views/home/home.tpl", inv = True)

debug(True)
run(reloader=True, host="localhost", port=8080)
