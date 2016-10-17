# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bottle
import beaker
import bcrypt
import hmac

def login_user(username, password):
    user_info = lgn.select_user_password_role(username)
    if user_info:
        hashed = user_info[0][0]
        hashed = hashed.encode("utf-8")
        urole = user_info[0][1]
        if (hmac.compare_digest(bcrypt.hashpw(password, hashed), hashed)):
            request.session["username"] = username
            request.session["user_role"] = urole

            redirect("/")
    return "fail"
        
@route("/logout")
#@post("/logout")
def logout():
    request.session.delete()
    redirect("/login")

@route("/initialize")
@post("/initialize")
@view("views/login/first_user")
def initialize():
    user_cnt = lgn.select_user_count()
    if user_cnt:
        redirect("/")
    if request.POST.get("create-user"):
        uname = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            lgn.insert_original_admin(uname, hashed)
            t = login_user(uname, password)
        else:
            err = "Passwords don't match"
            return dict(e = err)
    return dict(e = None)

    
@route("/login")
@post("/login")
@view("views/login/login_page")
def login():
    user_cnt = lgn.select_user_count()
    if not user_cnt:
        redirect("/initialize")
    if request.POST.get("login"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = password.encode('utf-8')
        t = login_user(username, password)
        return dict(t = "Login Failed")
    return dict(t = None)
