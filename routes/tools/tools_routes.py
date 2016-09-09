# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import models.tools.tools as tls

def gen_route(r):
    return "/tools/{0}".format(r)

def gen_view(v):
    return "views/tools/{0}".format(v)

@route(gen_route("create-upc-labels"))
@view(gen_view("create_upc_labels"))
@check_user
def create_upc_labels():
    return dict()

@route(gen_route("image-gallery"))
@post(gen_route("image-gallery"))
@view(gen_view("image_gallery"))
@check_user
def image_gallery():
    d = {}
    imgs = tls.select_all_images()
    if request.POST.get("delete-image"):
        d["img-del"] = request.POST.get("img-del")
        tls.delete_image(d)
    if request.POST.get("replace-image"):
        d["img-del"] = request.POST.get("img-del")
        d["new-img"] = request.files.get("new-img")
        return str(d)
        tls.replace_image(d)
    return dict(imgs = imgs)
    
@route(gen_route("bulk-load-images"))
@post(gen_route("bulk-load-images"))
@view(gen_view("bulk_load_images"))
@check_user
def bulk_load_images():
    L = []
    if request.POST.get("upload-images"):
        imgs = request.files.getlist("imgs")
        for i in imgs:
            save_path = "uploaded_files/images/{0}".format(i)

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            i.save(save_path, overwrite=True)

            L.append(i.filename)
        return str(L)
    return dict()

@route("/tools")
@view(gen_view("tools_main"))
@check_user
def tools():
    return dict()
