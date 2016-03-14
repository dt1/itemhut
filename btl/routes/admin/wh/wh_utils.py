# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from datetime import datetime
import os as os
from route_utils import *

def gen_view(v):
    return "views/admin/{0}".format(v)

def gen_route(r):
    return "/admin/manage-warehouses{0}".format(r)

def check_bm(wh):
    if wh != "B&M":
        return error404("err")

def upload_csv(f, locfile, wh):
    phash = abs(hash(datetime.now()))
    save_path = "uploaded_files/palletloc_files/{0}".format(phash)

    name, ext = os.path.splitext(locfile.filename)
    if ext not in (".csv"):
        return "Pleae upload CSV"

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    locfile.save(save_path)

    copy_from = "{0}/{1}/{2}".format(os.getcwd(), save_path,
                                     locfile.filename)
    f(copy_from, wh)

    os.remove("{0}/{1}".format(save_path, locfile.filename))
    os.rmdir(save_path)

    return "Upload Complete"
