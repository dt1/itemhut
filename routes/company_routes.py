# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/companies/<cid:int>/contacts/edit-contact-<cnid:int>")
@post("/companies/<cid:int>/contacts/edit-contact-<cnid:int>")
@view("views/companies/edit_contact")
def edit_company_contact(cid, cnid):
    check_user()
    cinfo = com.select_company_info(cid)
    contact_info = com.select_contact(cnid)
    if request.POST.get("edit-contact"):
        contact_name = request.POST.get("contact-name")
        position = request.POST.get("position")
        phone1 = request.POST.get("phone-one")
        phone2 = request.POST.get("phone-two")
        email = request.POST.get("email")
        com.update_contact(cnid, contact_name, position, phone1,
                           phone2, email)
        url = "/companies/{0}/contacts/edit-contact-{1}".format(cid, cnid)
        redirect(url)
    if contact_info:
        return dict(cinfo = cinfo[0], contact_info = contact_info[0])
    else:
        return error404("err")

@route("/companies/<cid:int>/add-contact")
@post("/companies/<cid:int>/add-contact")
@view("views/companies/add_contact")
def add_company_contact(cid):
    check_user()
    cinfo = com.select_company_info(cid)
    if request.POST.get("add-contact"):
        contact_name = request.POST.get("contact-name")
        position = request.POST.get("position")
        phone1 = request.POST.get("phone-one")
        phone2 = request.POST.get("phone-two")
        email = request.POST.get("email")
        cnid = com.add_contact(cid, contact_name, position, phone1,
                               phone2, email)
        url = "/companies/{0}/contacts/edit-contact-{1}".format(cid, cnid[0][0])
        redirect(url)
    return dict(cinfo = cinfo[0])

@route("/companies/<cid:int>/contacts")
@view("views/companies/contacts")
def company_contacts(cid):
    check_user()
    cinfo = com.select_company_info(cid)
    contact_list = com.select_company_contacts(cid)
    return dict(cinfo = cinfo[0], contact_list = contact_list)

@route("/companies/<cid:int>")
def reroute_company(cid):
    check_user()
    url = "/companies/edit-company-{0}".format(cid)
    redirect(url)

@route("/companies/edit-company-<cid:int>")
@post("/companies/edit-company-<cid:int>")
@view("views/companies/edit_company")
def edit_company(cid):
    check_user()
    cinfo = com.select_company_info(cid)
    if request.POST.get("edit-company"):
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
        com.update_company(cid, uid, cname, phone1, phone2, fax,
                                 email, street, state, zipcode,
                                 country)
        url = "/companies/edit-company-{0}".format(cid)
        redirect(url)
    return dict(cinfo = cinfo[0])


@route("/companies/add-company")
@post("/companies/add-company")
@view("views/companies/add_company")
def add_company():
    check_user()
    if request.POST.get("add-company"):
        uid = request.POST.get("company-uid")
        cname = request.POST.get("company-name")
        phone1 = request.POST.get("phone-one")
        phone2 = request.POST.get("phone-two")
        fax = request.POST.get("fax")
        email = request.POST.get("email")
        city = request.POST.get("city")
        street = request.POST.get("street")
        state = request.POST.get("state")
        zipcode = request.POST.get("zip")
        country = request.POST.get("country")
        cid = com.insert_company(uid, cname, phone1, phone2, fax,
                                 email, street, city, state, zipcode,
                                 country)
        url = "/companies/edit-company-{0}".format(cid[0][0])
        redirect(url)
    return dict()

@route("/companies")
@view("views/companies/company_main")
def companies():
    check_user()
    cinfo = com.select_all_companies()
    return dict(cinfo = cinfo)
