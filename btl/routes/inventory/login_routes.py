# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
from cork import Cork
import json

aaa = Cork("routes/inventory")

@route('/login')
@route('/login', method="POST")
def login():
    """Authenticate users"""
    return template("views/login/login_page")
    username = post_get('username')
    password = post_get('password')
    aaa.login(username, password, success_redirect='/', fail_redirect='/login')
