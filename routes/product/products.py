# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.products.product as prd
import product_utils as pus
    
@route(pus.gen_route("update-product-<pid>"))
@post(pus.gen_route("update-product-<pid>"))
@view(gen_view("update_product"))
@check_user
def update_product(pid):
    sku_data = prd.get_sku_data(pid)
    stypes = prd.sku_types()
    d = {}
    d["pid"] = pid
    L = pus.IMAGE_LIST + pus.PRODUCT_DATA_LIST
    if request.POST.get("update-product"):
        for i in L:
            d[i] = request.POST.get(i)
        d["remove-image"] = request.POST.getall("remove-image")
        if d["remove-image"]:
            prd.update_product_set_img_null(d)
        prd.update_product_data(d)
        pus.add_product_images(d)
        
        redirect("/products/update-product-{0}".format(d["sku"]))
    return dict(sku_data = sku_data, sku_types = stypes,
                sku = pid)

@route(pus.gen_route("add-product")
@post(pus.gen_route("add-product")
@view(pus.gen_view("add_product"), new_sku = None)
@check_user
def add_product():
    stypes = prd.sku_types()
    d = {}
    L = pus.IMAGE_LIST + pus.PRODUCT_DATA_LIST
    if request.POST.get("add-product"):
        for i in L:
            d[i] = request.POST.get(i)

        prd.insert_sku_upc(d)
        
        prd.insert_product_descriptions(d)

        pus.add_product_images(d)

        return dict(sku_types = stypes, new_sku = d["sku"])
    else:
        return dict(sku_types = stypes)
