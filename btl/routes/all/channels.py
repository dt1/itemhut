# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

# amazon pages
@route("/channels/amazon/<section>/new-item")
def add_amazon_item(section):
    valid_list = valid_amazon_list()
    fdict = collections.OrderedDict()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_amazon_reg_fields(s)
        for f in fields:
            fdict[f[0]] = {}
            fdict[f[0]]["cname"] = f[1]
            fdict[f[0]]["data_type"] = f[3]
            if f[4]:
                fdict[f[0]]["valid_array"] = get_amazon_valid_arrays(s, f[4])
        return template("views/amazon/new_item",
                        amz_header = amz_header, fields = fields,
                        section = section, fdict = fdict, inv = False)
    
@route("/channels/amazon/<section>")
def amazon_section(section):
    valid_list = valid_amazon_list()
    if section in valid_list:
        amz_header = section.replace("-", " ").title()
        s = "amazon_{0}".format(section.replace("-", "_"))
        s = s.strip()
        fields = get_base_amazon_data(s)
        return template("views/amazon/section",
                        amz_header = amz_header, fields = fields,
                        section = section, inv = False)

@route("/channels/<storefront>")
def product_store(storefront = None):
    if storefront in ["amazon"]:
        a = select_amazon_regular()
        return template("views/amazon/main", reg = a)
    if storefront in ["ebay"]:
        return template("views/ebay/main")
    else:
        error404("err")

@route("/channels")
def products():
    return template("views/channels")
