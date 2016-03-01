# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from full_route_utils import *

@route("/vendors/<vid>/contacts/edit-contact-<cid>")
@post("/vendors/<vid>/contacts/edit-contact-<cid>")
@view("views/vendors/edit_contact", inv = inv)
def edit_vendor_contact(vid, cid):
    check_user()
    contact_info = select_vendor_contact_info(cid)
    if request.POST.get("edit-contact"):
        contact_name = request.POST.get("name")
        contact_title = request.POST.get("title")
        phone = request.POST.get("phone")
        alt_phone = request.POST.get("alt-phone")
        email = request.POST.get("email")
        update_vendor_contact(cid, contact_name, contact_title, phone,
                              alt_phone, email)
        redirect("/vendors/{0}/contacts/edit-contact-{1}".format(vid, cid))
    else:
        return dict(contact_info = contact_info, vid = vid)

@route("/vendors/<vid>/products/add-product")
@post("/vendors/<vid>/products/add-product")
@view("views/vendors/add_product", inv = inv)
def add_vendor_product(vid):
    check_user()
    item_list = select_upc_list()
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        insert_product_vendor(vid, upc)
        return dict(upc = upc, item_list = item_list, vid = vid)
    else:
        return dict(upc = None, item_list = item_list, vid = vid)
    
@route("/vendors/<vid>/contacts/add-contact")
@post("/vendors/<vid>/contacts/add-contact")
@view("views/vendors/add_contact", inv = inv)
def add_vendor_contact(vid):
    check_user()
    if request.POST.get("add-contact"):
        contact_name = request.POST.get("name")
        contact_title = request.POST.get("title")
        phone = request.POST.get("phone")
        alt_phone = request.POST.get("alt-phone")
        email = request.POST.get("email")
        insert_vendor_contact(vid, contact_name, contact_title, phone,
                       alt_phone, email)
        return dict(contact_name = contact_name, vid = vid)
    else:
        return dict(contact_name = None, vid = vid)
    
@route("/vendors/<vid>/contacts")
@view("views/vendors/vendor_contacts", inv = inv)
def vendor_contacts(vid):
    check_user()
    v_info = get_vendor_info(vid)
    v_contacts = select_vendor_contacts(vid)
    return dict(contacts = v_contacts,
                    vendor_info = v_info)

@route("/vendors/<vid>/products")
@view("views/vendors/vendor_products", inv = inv)
def vendor_contacts(vid):
    check_user()
    v_info = get_vendor_info(vid)
    v_products = select_vendor_products(vid)
    return dict(vendor_products = v_products,
                    vendor_info = v_info)
    
@route("/vendors/<vid>")
@view("views/vendors/vendor_info", inv = inv)
def vendor_info(vid):
    check_user()
    v_info = get_vendor_info(vid)
    v_contacts = select_vendor_contacts(vid)
    v_products = select_vendor_products(vid)
    return dict(vendor_info = v_info, contacts = v_contacts,
                    vendor_products = v_products)

@route("/vendors/<vid>/edit-vendor")
@post("/vendors/<vid>/edit-vendor")
@view("views/vendors/edit_vendor", inv = inv)
def edit_vendor(vid):
    check_user()
    vendor_info = get_vendor_info(vid)
    if request.POST.get("update-vendor"):
        old_vendor_id = vid
        new_vendor_id = request.POST.get("vendor-id")
        vendor_name = request.POST.get("vendor-name")
        phone = request.POST.get("phone")
        fax = request.POST.get("fax")
        website = request.POST.get("website")
        email = request.POST.get("email")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        country = request.POST.get("country")
        update_vendor_info(old_vendor_id, new_vendor_id, vendor_name,
                       phone, fax, website, email, street, city, state,
                       zip, country)
        redirect("/vendors/{0}/edit-vendor".format(new_vendor_id))
    else:
        return dict(vendor_info = vendor_info)

@route("/vendors/add-vendor")
@post("/vendors/add-vendor")
@view("views/vendors/add_vendor", inv = inv)
def add_vendor():
    check_user()
    vendors = select_vendors()
    if request.POST.get("add-vendor"):
        vendor_id = request.POST.get("vendor-id")
        vendor_name = request.POST.get("vendor-name")
        phone = request.POST.get("phone")
        fax = request.POST.get("fax")
        website = request.POST.get("website")
        email = request.POST.get("email")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        country = request.POST.get("country")
        insert_new_vendor(vendor_id, vendor_name, phone, fax, website,
                          email, street, city, state, zip, country)
        return dict(new_vendor = vendor_name)
    else:
        return dict(new_vendor = None)

@route("/vendors")
@view("views/vendors/main", inv = inv)
def vendors():
    check_user()
    vendors = select_vendors()
    return dict(vendors = vendors)
