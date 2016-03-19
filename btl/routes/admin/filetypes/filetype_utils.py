# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *

def gen_view(v):
    return "views/admin/filetypes/{0}".format(v)

def gen_route(r = None):
    if r:
        return "/admin/manage-filetypes{0}".format(r)
    return "/admin/manage-filetypes"
