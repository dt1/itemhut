# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import routes.admin.filetypes.filetype_utils as aff

@route(aff.gen_route())
@view(aff.gen_view("filetypes_main"))
@check_user
@check_admin
def filetypes():
    return dict()
