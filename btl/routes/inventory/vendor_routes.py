# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/vendors/<vid>/add-contact")
@route("/vendors/<vid>/add-contact", method="POST")
def add_vendor_contact(vid):
    if request.POST.get("add-contact"):
        contact_name = request.POST.get("name")
        contact_title = request.POST.get("title")
        phone = request.POST.get("phone")
        alt_phone = request.POST.get("alt_phone")
        email = request.POST.get("email")
        insert_vendor_contact(vid, contact_name, contact_title, phone,
                       alt_phone, email)
        return template("views/vendors/add_contact",
                        contact_name = contact_name, vid = vid)
    else:
        return template("views/vendors/add_contact",
                        contact_name = None, vid = vid, inv = True)
    

@route("/vendors/<vid>")
def vendor_info(vid):
    v_info = get_vendor_info(vid)
    v_contacts = select_vendor_contacts(vid)
    return template("views/vendors/vendor_info", vendor_info = v_info,
                    contacts = v_contacts, inv = True)

@route("/vendors/add-vendor")
@route("/vendors/add-vendor", method="POST")
def vendors():
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
