# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bottle
import beaker
from bottle.ext import auth
from bottle.ext.auth.decorator import login
import bcrypt
import hmac

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def login_user(username, password):
    user_info = select_user_password_role(username)
    if user_info:
        hashed = user_info[0][0]
        urole = user_info[0][1]
        if (hmac.compare_digest(bcrypt.hashpw(password, hashed), hashed)):
            request.session["username"] = username
            request.session["usertype"] = urole

            redirect("/")
    return "fail"
        
@route('/logout')
#@post('/logout')
def logout():
    request.session.delete()
    redirect('/login')

@route('/login')
@post('/login')
def login():
    """Authenticate users"""
    if request.POST.get("login"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        t = login_user(username, password)
        return template("views/login/login_page", t = "Login Failed")
    return template("views/login/login_page", t = None)
