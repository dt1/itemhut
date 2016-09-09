# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from bottle import *

import psycopg2
import psycopg2.extras
import collections
from beaker.middleware import SessionMiddleware
import bottle
import bcrypt
import hmac

from models.amazon import *
import models.warehouse.warehouse as whs
import models.vendors.vendors as ven
# admin
#import models.admin.admin as adm
import models.admin.users.users as admus
import models.admin.wh.wh_info as admwh
import models.admin.wh.pallet_locs as admpal
import models.admin.wh.picking_locs as admpic

import models.incoming.incoming as icm
import models.orders.orders as ords
import models.companies.companies as com
import models.login.login as lgn
import models.tools.tools as tls

from pydb.dbconn import cur, dcur

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 14400,
    'session.data_dir': './data',
    'session.auto': True
}

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']
    #request.session["username"] = "sally"
    #request.session["user_role"] = "user"

@hook('before_request')
def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

    
@error(404)
def error404(error):
    return "404; please press the back button"

@error(403)
def error403(error):
    return "page restricted. Please press the back button"

def check_user(f):
    def wrapper(*args, **kwargs):
        if 'username' not in request.session:
            redirect("/login")
        return f(*args, **kwargs)
    return wrapper

def check_admin(f):
    def wrapper(*args, **kwargs):
        role = request.session["user_role"]
        if role not in ["admin", "original admin"]:
            redirect("/")
        return f(*args, **kwargs)
    return wrapper

def check_warehouse_user(f):
    def wrapper(*args, **kwargs):
        role = request.session["user_role"]
        if role not in ["admin", "original admin", "warehouses"]:
            redirect("/")
        return f(*args, **kwargs)
    return wrapper

def check_orders_user(f):
    def wrapper(*args, **kwargs):
        role = request.session["user_role"]
        if role not in ["admin", "original admin", "orders"]:
            redirect("/")
        return f(*args, **kwargs)
    return wrapper

myapp = SessionMiddleware(bottle.app(), session_opts)

inv = True
