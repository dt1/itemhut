# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

def add_product_images(d):
    image_list = ["main-image", "image-one", "image-two",
                  "image-three", "image-four","image-five",
                  "image-six", "image-seven", "image-eight",
                  "image-nine", "image-ten", "image-eleven",
                  "image-twelve", "swatch-image"]
    for i in image_list:
        if d[i]:
            save_path = "uploaded_files/images/{0}".format(d[i])

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            d[i].save(save_path, overwrite=True)
            d[i + "-path"] = "{0}/{1}".format(d[i], d[i].filename)
        
        else:
            d[i + "-path"] = None
    prd.insert_images(d)

@route("/products/update-product-<pid>/gallery-<img>")
@post("/products/update-product-<pid>/gallery-<img>")
@view("views/products/update_product_image_gallery")
def update_product_image_gallery(pid, img):
    imgs = prd.select_image_gallery()
    d = {}
    d["image-column"] = img.replace("-", "_")
    d["sku"] = pid
    if request.POST.get("update-image"):
        d["new-image"] = request.POST.get("new-image")
        prd.update_product_image(d)
        redirect("/products/update-product-{0}".format(d["sku"]))
    return dict(sku = pid, img = img, imgs = imgs)

    
@route("/products/update-product-<pid>")
@post("/products/update-product-<pid>")
@view("views/products/update_product")
@check_user
def update_product(pid):
    sku_data = prd.get_sku_data(pid)
    stypes = prd.sku_types()
    d = {}
    d["pid"] = pid
    L = ["sku", "upc", "sku-type",
         "product-name", "product-description", "bullet-one",
         "bullet-two", "bullet-three", "bullet-four", "bullet-five",
         "main-image", "image-one", "image-two", "image-three",
         "image-four", "image-five", "image-six", "image-seven",
         "image-eight", "image-nine", "image-ten", "image-eleven",
         "image-twelve", "swatch-image"]
    if request.POST.get("update-product"):
        for i in L:
            d[i] = request.POST.get(i)
        d["remove-image"] = request.POST.getall("remove-image")
        if d["remove-image"]:
            prd.update_product_set_img_null(d)
        prd.update_product_data(d)
        add_product_images(d)
        
        redirect("/products/update-product-{0}".format(d["sku"]))
    return dict(sku_data = sku_data, sku_types = stypes,
                sku = pid)

@route("/products/delete-kit-child-<master>/<child>")
@check_user
def delete_kit_child(master, child):
    prd.delete_kit_child(master, child)
    url = "/products/add-kit-children-{0}".format(master)
    redirect(url)

@route("/products/add-kit-children-<sku>")
@post("/products/add-kit-children-<sku>")
@view("views/products/add_kit_children")
@check_user
def update_kit(sku):
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
@check_user
def update_kit(sku):
    pass

@route("/products/add-kit")
@post("/products/add-kit")
@view("views/products/add_kit", err = None, new_sku = None)
@check_user
def add_kit():
    d = {}
    d["upc"] = None
    d["sku-type"] = "master"
    L = ["product-name", "product-description", "bullet-one",
         "bullet-two", "bullet-three", "bullet-four", "bullet-five",
         "main-image", "image-one", "image-two", "image-three",
         "image-five", "image-six", "image-seven", "image-eight",
         "image-nine", "image-ten", "image-eleven", "image-twelve",
         "swatch-image"]
    if request.POST.get("add-product"):
        for i in L:
            d[i] = request.POST.get(i)

        prd.insert_sku_upc(sku, upc, sku_type)
        
        prd.insert_product_descriptions(sku, product_name, product_description, bullet_one, bullet_two, bullet_three, bullet_four, bullet_five)
        
        if d["main-image"]:
            main_image = d["main_image"]
            save_path = "uploaded_files/images/{0}".format(main_image)

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            main_image.save(save_path, overwrite=True)

            image_path = "{0}/{1}".format(main_image, main_image.filename)


        prd.insert_images(d)

        url = "/products/update-kit-{0}".format(d["sku"])
        redirect(url)
    else:
        return dict()

@route("/products/kits")
@view("views/products/kits")
@check_user
def all_kits():
    k = prd.select_kits()
    return dict(kits = k)

@route("/products/add-product")
@post("/products/add-product")
@view("views/products/add_product", new_sku = None)
@check_user
def add_product():
    stypes = prd.sku_types()
    d = {}
    L = ["sku", "upc", "sku-type",
         "product-name", "product-description", "bullet-one",
         "bullet-two", "bullet-three", "bullet-four", "bullet-five",
         "main-image", "image-one", "image-two", "image-three",
         "image-four", "image-five", "image-six", "image-seven",
         "image-eight", "image-nine", "image-ten", "image-eleven",
         "image-twelve", "swatch-image"]
    if request.POST.get("add-product"):
        for i in L:
            d[i] = request.POST.get(i)

        prd.insert_sku_upc(d)
        
        prd.insert_product_descriptions(d)

        add_product_images(d)

        return dict(sku_types = stypes, new_sku = d["sku"])
    else:
        return dict(sku_types = stypes)
   
@route("/products")
@view("views/products/product_main")
@check_user
def products():
    sku_upc = prd.select_reg_products()
    return dict(sku_upc = sku_upc)
