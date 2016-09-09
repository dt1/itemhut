# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/vendors/<vid>/contacts/edit-contact-<cid>")
@post("/vendors/<vid>/contacts/edit-contact-<cid>")
@view("views/vendors/edit_contact")
@check_user
def edit_vendor_contact(vid, cid):
    vendor_info = ven.get_vendor_info(vid)
    contact_info = ven.select_vendor_contact_info(cid)
    d = {}
    d["cid"] = cid
    L = ["name", "title", "phone", "alt-phone" "email"]
    if request.POST.get("edit-contact"):
        for i in L:
            d[i] = request.POST.get(i)
        ven.update_vendor_contact(d)
        redirect("/vendors/{0}/contacts/edit-contact-{1}".format(vid, d["cid"]))
    else:
        return dict(contact_info = contact_info, vid = vid,
                    vendor_info = vendor_info)
    
# products
@route("/vendors/<vid>/products/delete-product")
@check_user
def reroute_delete_product(vid):
    url = "/vendors/{0}/products".format(vid)
    redirect(url)

@route("/vendors/<vid>/products/delete-product-<pid:int>")
@check_user
def delete_vendor_product(vid, pid):
    ven.delete_vendor_product(vid, pid)
    url = "/vendors/{0}/products".format(vid)
    redirect(url)

@route("/vendors/<vid>/products/add-product")
@post("/vendors/<vid>/products/add-product")
@view("views/vendors/add_product")
@check_user
def add_vendor_product(vid):
    vendor_info = ven.get_vendor_info(vid)
    item_list = ven.select_upc_list()
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        ven.insert_product_vendor(vid, upc)
        url = "/vendors/{0}/products/add-product".format(vid)
        redirect(url)
    else:
        return dict(upc = None, item_list = item_list, vid = vid,
                    vendor_info = vendor_info)

@route("/vendors/<vid>/products")
@view("views/vendors/vendor_products")
@check_user
def vendor_contacts(vid):
    vendor_info = ven.get_vendor_info(vid)
    v_products = ven.select_vendor_products(vid)
    return dict(vendor_products = v_products,
                    vendor_info = vendor_info)
    
@route("/vendors/<vid>")
@view("views/vendors/vendor_info")
@check_user
def vendor_info(vid):
    vendor_info = ven.get_vendor_info(vid)
    v_contacts = ven.select_vendor_contacts(vid)
    v_products = ven.select_vendor_products(vid)
    return dict(vendor_info = vendor_info, contacts = v_contacts,
                    vendor_products = v_products)

@route("/vendors/<vid>/contacts/add-contact")
@post("/vendors/<vid>/contacts/add-contact")
@view("views/vendors/add_contact", contact_name = None)
@check_user
def add_vendor_contact(vid):
    vendor_info = ven.get_vendor_info(vid)
    d = {}
    d["vid"] = vid
    L = ["name", "title", "phone", "alt-phone", "email"]
    if request.POST.get("add-contact"):
        for i in L:
            d[i] = request.POST.get(i)
        ven.insert_vendor_contact(d)
        return dict(contact_name = d["name"], vid = vid,
                    vendor_info = vendor_info)
    else:
        return dict(vid = vid,
                    vendor_info = vendor_info)
    
@route("/vendors/<vid>/contacts")
@view("views/vendors/vendor_contacts")
@check_user
def vendor_contacts(vid):
    vendor_info = ven.get_vendor_info(vid)
    v_contacts = ven.select_vendor_contacts(vid)
    return dict(contacts = v_contacts,
                    vendor_info = vendor_info)

@route("/vendors/<vid>/edit-vendor")
@post("/vendors/<vid>/edit-vendor")
@view("views/vendors/edit_vendor")
@check_user
def edit_vendor(vid):
    vendor_info = ven.get_vendor_info(vid)
    d = {}
    d["old-vid"] = vid
    L = ["vendor-id", "vendor-name", "phone", "fax", "website",
         "email", "street", "city", "state", "zip", "country"]
    if request.POST.get("update-vendor"):
        for i in L:
            d[i] = request.POST.get(i)
        ven.update_vendor_info(d)
        redirect("/vendors/{0}/edit-vendor".format(d["vendor-id"]))
    else:
        return dict(vendor_info = vendor_info)

@route("/vendors/add-vendor")
@post("/vendors/add-vendor")
@view("views/vendors/add_vendor", new_vendor = None)
@check_user
def add_vendor():
    vendors = ven.select_vendors()
    d = {}
    L = ["vendor-id", "vendor-name", "phone", "fax", "website",
         "email", "street", "city", "state", "zip", "country"]
    if request.POST.get("add-vendor"):
        for i in L:
            d[i] = request.POST.get(i)
        ven.insert_new_vendor(d)
        return dict(new_vendor = d["vendor-name"])
    else:
        return dict()

@route("/vendors")
@view("views/vendors/main")
@check_user
def vendors():
    vendors = ven.select_vendors()
    return dict(vendors = vendors)
