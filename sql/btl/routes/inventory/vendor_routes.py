# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/vendors/<vid>/contacts/edit-contact-<cid>")
@route("/vendors/<vid>/contacts/edit-contact-<cid>", method="POST")
def edit_vendor_contact(vid, cid):
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
        return template("views/vendors/edit_contact",
                        contact_info = contact_info, vid = vid,
                        inv = True)

@route("/vendors/<vid>/products/add-product")
@route("/vendors/<vid>/products/add-product", method="POST")
def add_vendor_product(vid):
    item_list = select_upc_list()
    if request.POST.get("add-product"):
        upc = request.POST.get("upc")
        insert_product_vendor(vid, upc)
        return template("views/vendors/add_product", upc = upc,
                        item_list = item_list, inv = True, vid = vid)
    else:
        return template("views/vendors/add_product", upc = None,
                        item_list = item_list, inv = True, vid = vid)
    
@route("/vendors/<vid>/contacts/add-contact")
@route("/vendors/<vid>/contacts/add-contact", method="POST")
def add_vendor_contact(vid):
    if request.POST.get("add-contact"):
        contact_name = request.POST.get("name")
        contact_title = request.POST.get("title")
        phone = request.POST.get("phone")
        alt_phone = request.POST.get("alt-phone")
        email = request.POST.get("email")
        insert_vendor_contact(vid, contact_name, contact_title, phone,
                       alt_phone, email)
        return template("views/vendors/add_contact",
                        contact_name = contact_name, vid = vid, inv = True)
    else:
        return template("views/vendors/add_contact",
                        contact_name = None, vid = vid, inv = True)
    
@route("/vendors/<vid>/contacts")
def vendor_contacts(vid):
    v_info = get_vendor_info(vid)
    v_contacts = select_vendor_contacts(vid)
    return template("views/vendors/vendor_contacts",
                    contacts = v_contacts, inv = True,
                    vendor_info = v_info)

@route("/vendors/<vid>/products")
def vendor_contacts(vid):
    v_info = get_vendor_info(vid)
    v_products = select_vendor_products(vid)
    return template("views/vendors/vendor_products",
                    vendor_products = v_products, inv = True,
                    vendor_info = v_info)

    
@route("/vendors/<vid>")
def vendor_info(vid):
    v_info = get_vendor_info(vid)
    v_contacts = select_vendor_contacts(vid)
    v_products = select_vendor_products(vid)
    return template("views/vendors/vendor_info",
                        vendor_info = v_info, contacts = v_contacts,
                        inv = True, vendor_products = v_products)

@route("/vendors/<vid>/edit-vendor")
@route("/vendors/<vid>/edit-vendor", method="POST")
def edit_vendor(vid):
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
        return template("views/vendors/edit_vendor",
                        vendor_info = vendor_info, inv = True)

@route("/vendors/add-vendor")
@route("/vendors/add-vendor", method="POST")
def add_vendor():
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
        return template("views/vendors/add_vendor",
                        new_vendor = vendor_name, inv = True)
    else:
        return template("views/vendors/add_vendor", new_vendor = None,
                        inv = True)

@route("/vendors")
def vendors():
    vendors = select_vendors()
    return template("views/vendors/main", vendors = vendors,
                    inv = True)
