# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.products.product as prd
import product_utils as pus

@route("/products")
@view(pus.gen_view("product_main"))
@check_user
def products():
    sku_upc = prd.select_reg_products()
    return dict(sku_upc = sku_upc)
