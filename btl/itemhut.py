# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from routes.all.product_routes import *
from routes.all.warehouse_routes import *
from routes.all.vendor_routes import *
from routes.all.admin_routes import *
from routes.all.channel_routes import *

def ins_one(str):
    dbconn.cur.execute(
        """
        begin;
        insert into table_test.valid_one
        values ($${0}$$);
        commit;
        """.format(str))
    

@route("/test-insert")
@route("/test-insert", method="POST")
def test_insert():
    if request.POST.get("save", ""):
        task = request.POST.get("task").strip()
        hello = request.POST.get("hello", "").strip()
        t = request.forms.getall("task")
#        ins_one(item)
        return "{0}".format(t)

@error(404)
def error404(err):
    return "404; please press the back button"

# for css, js, img, etc
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")

# order pages
@route("/orders")
def orders():
    return template("views/orders/orders", inv = False)

# emails
@route("/emails")
def emails():
    return template("views/emails/emails", inv = False)

# customers
@route("/customers")
def customers():
    return template("views/customers/customers", inv = False)

# analytics
@route("/analytics")
def analytics():
    return template("views/analytics/analytics", inv = False)

# admin
@route("/admin")
def admin():
    return template("views/admin/admin", inv = False)

# home page    
@route("/")
def index():
    return template("views/home/home.tpl", inv = False)

debug(True)
run(reloader=True, host="localhost", port=8080)
