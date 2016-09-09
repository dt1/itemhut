# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.products.product as prd

def gen_route(r):
    return "/products/{0}".format(r)

def gen_view(v):
    return "views/products/{0}".format(v)

IMAGE_LIST = ["main-image", "image-one", "image-two",
              "image-three", "image-four","image-five",
              "image-six", "image-seven", "image-eight",
              "image-nine", "image-ten", "image-eleven",
              "image-twelve", "swatch-image"]

PRODUCT_DATA_LIST = ["sku", "upc", "sku-type",
                     "product-name", "product-description",
                     "bullet-one", "bullet-two", "bullet-three",
                     "bullet-four", "bullet-five"]

KIT_DATA_LIST = ["sku", "product-name", "product-description",
                 "bullet-one", "bullet-two", "bullet-three",
                 "bullet-four", "bullet-five",]

def add_product_images(d):
    image_list = pus.IMAGE_LIST
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

