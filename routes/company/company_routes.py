# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.companies.companies as com

COMPANY_INFO_LIST = ["company-uid", "company-name", "phone-one",
                     "phone-two", "fax", "email", "street", "city",
                     "state", "zip", "country"]

COMPANY_CONTACT_INFO_LIST = ["contact-name", "position", "phone-one",
                             "phone-two", "email"]

@route("/companies/<cid:int>/contacts/edit-contact-<cnid:int>")
@post("/companies/<cid:int>/contacts/edit-contact-<cnid:int>")
@view("views/companies/edit_contact")
@check_user
def edit_company_contact(cid, cnid):
    cinfo = com.select_company_info(cid)
    contact_info = com.select_contact(cnid)
    d = {"cnid": cnid}
    L = COMPANY_CONTACT_INFO_LIST
    if request.POST.get("edit-contact"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        com.update_contact(d)
        url = "/companies/{0}/contacts/edit-contact-{1}".format(cid, cnid)
        redirect(url)
    if contact_info:
        return dict(cinfo = cinfo[0], contact_info = contact_info[0])
    else:
        return error404("err")

@route("/companies/<cid:int>/add-contact")
@post("/companies/<cid:int>/add-contact")
@view("views/companies/add_contact")
@check_user
def add_company_contact(cid):
    cinfo = com.select_company_info(cid)
    d = {"cid": cid}
    L = COMPANY_CONTACT_INFO_LIST
    if request.POST.get("add-contact"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        cnid = com.add_contact(d)
        url = "/companies/{0}/contacts/edit-contact-{1}".format(cid, cnid[0][0])
        redirect(url)
    return dict(cinfo = cinfo[0])

@check_user
@route("/companies/<cid:int>/contacts")
@view("views/companies/contacts")
def company_contacts(cid):
    cinfo = com.select_company_info(cid)
    contact_list = com.select_company_contacts(cid)
    return dict(cinfo = cinfo[0], contact_list = contact_list)

@route("/companies/<cid:int>")
@check_user
def reroute_company(cid):
    url = "/companies/edit-company-{0}".format(cid)
    redirect(url)

@route("/companies/edit-company-<cid:int>")
@post("/companies/edit-company-<cid:int>")
@view("views/companies/edit_company")
@check_user
def edit_company(cid):
    cinfo = com.select_company_info(cid)
    d = {"cid": cid}
    L = COMPANY_INFO_LIST
    if request.POST.get("edit-company"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        com.update_company(d)
        url = "/companies/edit-company-{0}".format(cid)
        redirect(url)
    return dict(cinfo = cinfo[0])


@route("/companies/add-company")
@post("/companies/add-company")
@view("views/companies/add_company")
@check_user
def add_company():
    L = COMPANY_INFO_LIST
    if request.POST.get("add-company"):
        d = {i : request.POST.get(i) for i in L}
        cid = com.insert_company(d)
        url = "/companies/edit-company-{0}".format(cid[0][0])
        redirect(url)
    return dict()

@route("/companies")
@view("views/companies/company_main")
@check_user
def companies():
    cinfo = com.select_all_companies()
    return dict(cinfo = cinfo)
