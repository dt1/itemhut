# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/companies/edit-company-<cid>")
@post("/companies/edit-company-<cid>")
@view("views/companies/edit_company", inv = inv)
def edit_company(cid):
    return dict()


@route("/companies/add-company")
@post("/companies/add-company")
@view("views/companies/add_company", inv = inv)
def add_company():
    if request.POST.get("add-company"):
        uid = request.POST.get("company-uid")
        cname = request.POST.get("company-name")
        phone1 = request.POST.get("phone-one")
        phone2 = request.POST.get("phone-two")
        fax = request.POST.get("fax")
        email = request.POST.get("email")
        street = request.POST.get("street")
        state = request.POST.get("state")
        zipcode = request.POST.get("zip")
        country = request.POST.get("country")
        url = "/companies/edit-company-{0}".format(1)
        redirect(url)
    return dict()

@route("/companies")
@view("views/companies/company_main", inv = inv)
def companies():
    return dict()
