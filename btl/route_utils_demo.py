# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from bottle import *

import psycopg2
import psycopg2.extras
import collections
from beaker.middleware import SessionMiddleware
import bottle

from models.amazon import *
from models.product import *
from models.warehouse import *
from models.vendors import *
from models.admin import *
from models.incoming import *

import sys
sys.path.append("/itemhut/pydb")
import dbconn

@error(404)
def error404(err):
    return "404; please press the back button"

def check_user():
    return "user A"


def check_admin():
    return "user A"

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 14400,
    'session.data_dir': './data',
    'session.auto': True
}

myapp = SessionMiddleware(bottle.app(), session_opts)

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']
