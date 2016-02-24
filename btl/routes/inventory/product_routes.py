# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/products/update-product-<pid>")
@post("/products/update-product-<pid>")
def update_product(pid):
    check_user()
    sku_data = get_sku_data(pid)
    stypes = sku_types()
    if request.POST.get("update-product"):
        sku = request.POST.get("sku")
        upc = request.POST.get("upc")
        sku_type = request.POST.get("sku-type")
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        main_image = request.POST.get("main-image")
        update_product_data(pid, sku, upc, sku_type, product_name,
                       product_description, main_image)
        redirect("/products/update-product-{0}".format(sku))
    return template("views/products/update_product_inv",
                    sku_data = sku_data, sku_types = stypes,
                    sku = pid, inv = True)

@route("/products/add-kit")
@post("/products/add-kit")
def add_kit():
    check_user()
    sku_upc = sku_upcs()
    if request.POST.get("add-kit"):
        master_sku = request.POST.get("master-sku")
        for i in range(1, 11):
            kit_name = request.POST.get("kit-name-{0}".format(i))
            kit_amt = request.POST.get("kit-amt-{0}".format(i))
            if kit_name:
                if kit_amt:
                    insert_sku_upc(master_sku, None, "master")
                    insert_kit(master_sku, kit_name, kit_amt)
                else:
                    return template("views/products/add_kit",
                                    sku_upc = sku_upc,
                                    new_sku = None,
                                    err = "Please add an amount for your kits", inv = True)
        return template("views/products/add_kit",
                        sku_upc = sku_upc, new_sku = master_sku,
                        err = None, inv = True)
    else:
        return template("views/products/add_kit", sku_upc = sku_upc,
                        new_sku = None, err = None, inv = True)

@route("/products/kits")
def all_kits():
    check_user()
    k = kits()
    return template("views/products/kits", kits = k, inv = True)

@route("/products/add-product")
@post("/products/add-product")
def add_products():
    check_user()
    sku_upc = sku_upcs()
    stypes = sku_types()
    if request.POST.get("add-product"):
        sku = request.POST.get("sku")
        upc = request.POST.get("upc")
        sku_type = request.POST.get("sku-type")

        insert_sku_upc(sku, upc, sku_type)
        
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        bullet_one = request.POST.get("bullet-one")
        bullet_two = request.POST.get("bullet-two")
        bullet_three = request.POST.get("bullet-three")
        bullet_four = request.POST.get("bullet-four")
        bullet_five = request.POST.get("bullet-five")

        insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five)
        
        main_image = request.POST.get("main-image")
        
        image_one = request.POST.get("image-one")
        image_two = request.POST.get("image-two")
        image_three = request.POST.get("image-three")
        image_four = request.POST.get("image-four")
        image_five = request.POST.get("image-five")
        image_six = request.POST.get("image-six")
        image_seven = request.POST.get("image-seven")
        image_eight = request.POST.get("image-eight")
        image_nine = request.POST.get("image-nine")
        image_ten = request.POST.get("image-ten")
        image_eleven = request.POST.get("image-eleven")
        image_twelve = request.POST.get("image-twelve")
        swatch_image = request.POST.get("swatch-image")

        insert_images(sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image)

        return template("views/products/add_product_inv",
                        sku_upc = sku_upc, sku_types = stypes,
                        new_sku = sku, inv = True)
    else:
        return template("views/products/add_product_inv",
                        sku_upc = sku_upc, sku_types = stypes,
                        new_sku = None, inv = True)
@route("/products")
def products():
    check_user()
    sku_upc = select_reg_products()
    return template("views/products/product_main", sku_upc = sku_upc,
                    inv = True)
