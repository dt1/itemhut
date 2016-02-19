# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from bottle import *

import psycopg2
import psycopg2.extras
import collections

from models.amazon import *
from models.product import *
from models.warehouse import *
from models.vendors import *
from models.admin import *

import sys
sys.path.append("/itemhut/pydb")
import dbconn

@error(404)
def error404(err):
    return "404; please press the back button"
