# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.products.product as prd
import routes.product.product_utils as pus

@route(pus.gen_route("delete-kit-child-<master>/<child>"))
@check_user
def delete_kit_child(master, child):
    prd.delete_kit_child(master, child)
    url = "/products/add-kit-children-{0}".format(master)
    redirect(url)

@route(pus.gen_route("add-kit-children-<sku>"))
@post(pus.gen_route("add-kit-children-<sku>"))
@view(pus.gen_view("add_kit_children"))
@check_user
def add_kit_children(sku):
    d = {"sku": sku}
    L = ["kit-sku", "qty"]
    sku_upc = prd.sku_kit_candidates(sku)
    kit_list = prd.select_sku_kits(sku)
    if request.POST.get("add-product"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        prd.insert_kit_child(d)
        url = "/products/add-kit-children-{0}".format(sku)
        redirect(url)
    return dict(sku_upc = sku_upc, sku = sku, kit_list = kit_list)

@route(pus.gen_route("update-kit-<sku>"))
@post(pus.gen_route("update-kit-<sku>"))
@view(pus.gen_view("add_kit"), err = None, new_sku = None)
@check_user
def update_kit(sku):
    pass

@route(pus.gen_route("add-kit"))
@post(pus.gen_route("add-kit"))
@view(pus.gen_view("add_kit"), err = None, new_sku = None)
@check_user
def add_kit():
    d = {"upc": None,
         "sku-type": "master"}
    L = pus.KIT_DATA_LIST + pus.IMAGE_LIST
    if request.POST.get("add-kit"):
        d = {**{i : request.POST.get(i) for i in L}, **d}
        prd.insert_sku_upc(d)
        prd.insert_product_descriptions(d)
        pus.add_product_images(d)
        
        url = "/products/update-kit-{0}".format(d["sku"])
        redirect(url)
    else:
        return dict()

@route(pus.gen_route("kits"))
@view(pus.gen_view("kits"))
@check_user
def all_kits():
    k = prd.select_kits()
    return dict(kits = k)
