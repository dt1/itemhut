# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

def gen_route(r):
    return "/tools/{0}".format(r)

def gen_view(v):
    return "views/tools/{0}".format(v)

@route(gen_route("create-upc-labels"))
@view(gen_view("create_upc_labels"))
@check_user
def create_upc_labels():
    return dict()

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

