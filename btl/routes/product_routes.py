# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

@route("/products/update-product-<pid>")
@post("/products/update-product-<pid>")
@view("views/products/update_product_inv")
def update_product(pid):
    check_user()
    sku_data = prd.get_sku_data(pid)
    stypes = prd.sku_types()
    if request.POST.get("update-product"):
        sku = request.POST.get("sku")
        upc = request.POST.get("upc")
        sku_type = request.POST.get("sku-type")
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        main_image = request.POST.get("main-image")

        if main_image:
            save_path = "uploaded_files/images/{0}".format(main_image)

            if not os.path.exists(save_path):
                os.makedirs(save_path)

                main_image.save(save_path, overwrite=True)

                image_path = "{0}/{1}".format(main_image,
                                              main_image.filename)
        
                prd.update_product_data(pid, sku, upc, sku_type,
                                        product_name,
                                        product_description,
                                        image_path)
        else:
            prd.update_product_data(pid, sku, upc, sku_type,
                                    product_name, product_description,
                                    None)

        redirect("/products/update-product-{0}".format(sku))
    return dict(sku_data = sku_data, sku_types = stypes,
                    sku = pid)


@route("/products/delete-kit-child-<master>/<child>")
def delete_kit_child(master, child):
    check_user()
    prd.delete_kit_child(master, child)
    url = "/products/add-kit-children-{0}".format(master)
    redirect(url)

@route("/products/add-kit-children-<sku>")
@post("/products/add-kit-children-<sku>")
@view("views/products/add_kit_children")
def update_kit(sku):
    check_user()
    sku_upc = prd.sku_kit_candidates(sku)
    kit_list = prd.select_sku_kits(sku)
    if request.POST.get("add-product"):
        kit_sku = request.POST.get("kit-sku")
        qty = request.POST.get("qty")
        prd.insert_kit(sku, kit_sku, qty)
        url = "/products/add-kit-children-{0}".format(sku)
        redirect(url)
    return dict(sku_upc = sku_upc, sku = sku, kit_list = kit_list)

@route("/products/update-kit-<sku>")
@post("/products/update-kit-<sku>")
@view("views/products/add_kit", err = None, new_sku = None)
def update_kit(sku):
    check_user()
    pass

@route("/products/add-kit")
@post("/products/add-kit")
@view("views/products/add_kit", err = None, new_sku = None)
def add_kit():
    check_user()
    if request.POST.get("add-product"):
        sku = request.POST.get("sku")
        upc = None
        sku_type = "master"

        prd.insert_sku_upc(sku, upc, sku_type)
        
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        bullet_one = request.POST.get("bullet-one")
        bullet_two = request.POST.get("bullet-two")
        bullet_three = request.POST.get("bullet-three")
        bullet_four = request.POST.get("bullet-four")
        bullet_five = request.POST.get("bullet-five")

        prd.insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five)
        
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

        if main_image:
            save_path = "uploaded_files/images/{0}".format(main_image)

            if not os.path.exists(save_path):
                os.makedirs(save_path)

                main_image.save(save_path, overwrite=True)

                image_path = "{0}/{1}".format(main_image, main_image.filename)


                prd.insert_images(sku, image_path, image_one,
                                  image_two,
                                  image_three, image_four, image_five,
                                  image_six, image_seven, image_eight,
                                  image_nine, image_ten, image_eleven,
                                  image_twelve, swatch_image)
        else:
            prd.insert_images(sku, None, image_one, image_two,
                          image_three, image_four, image_five,
                          image_six, image_seven, image_eight,
                          image_nine, image_ten, image_eleven,
                          image_twelve, swatch_image)

        url = "/products/update-kit-{0}".format(sku)
        redirect(url)
    else:
        return dict()

@route("/products/kits")
@view("views/products/kits")
def all_kits():
    check_user()
    k = prd.select_kits()
    return dict(kits = k)

@route("/products/add-product")
@post("/products/add-product")
@view("views/products/add_product_inv")
def add_products():
    check_user()
    sku_upc = prd.sku_upcs()
    stypes = prd.sku_types()
    if request.POST.get("add-product"):
        sku = request.POST.get("sku")
        upc = request.POST.get("upc")
        sku_type = request.POST.get("sku-type")

        prd.insert_sku_upc(sku, upc, sku_type)
        
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        bullet_one = request.POST.get("bullet-one")
        bullet_two = request.POST.get("bullet-two")
        bullet_three = request.POST.get("bullet-three")
        bullet_four = request.POST.get("bullet-four")
        bullet_five = request.POST.get("bullet-five")

        prd.insert_product_descriptions(sku, product_name,
                                        product_description,
                                        bullet_one, bullet_two,
                                        bullet_three, bullet_four,
                                        bullet_five)
        
        main_image = request.POST.get("main-image")
        
        save_path = "uploaded_files/images/{0}".format(main_image)

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        main_image.save(save_path, overwrite=True)

        image_path = "{0}/{1}".format(main_image, main_image.filename)
        
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

        prd.insert_images(sku, image_path, image_one, image_two,
                          image_three, image_four, image_five,
                          image_six, image_seven, image_eight,
                          image_nine, image_ten, image_eleven,
                          image_twelve, swatch_image)

        return dict(sku_upc = sku_upc, sku_types = stypes,
                    new_sku = sku)
    else:
        return dict(sku_upc = sku_upc, sku_types = stypes,
                    new_sku = None)

@route("/products")
@view("views/products/product_main")
def products():
    check_user()
    sku_upc = prd.select_reg_products()
    return dict(sku_upc = sku_upc)
