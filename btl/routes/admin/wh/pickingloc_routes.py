# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import routes.admin.wh.wh_utils as whu

@route(whu.gen_route("/<wh>/add-picking-locations"))
@post(whu.gen_route("/<wh>/add-picking-locations"))
@view(whu.gen_view("add_picking_location"))
def add_picking_location(wh):
    check_admin()
    wh_info = adm.select_warehouse_info(wh)
    if not wh_info:
        return erro404("err")

    whu.check_bm(wh_info[0][6])
    if request.POST.get("add-picking-location"):
        location_name = request.POST.get("location-name")
        upc = request.POST.get("upc")
        err = adm.insert_picking_location(wh, location_name, upc)
        if err:
            err = "{0} already exists".format(location_name)
            return dict(wh_info = wh_info, message = err)
        else:
            message = "Added {0}".format(location_name)
            return dict(wh_info = wh_info, message = message)

    elif request.POST.get("upload"):
        locfile = request.POST.get("loc-file")
        message = upload_csv(adm.bulk_load_pickinglocs, locfile, wh)
        return dict(wh_info = wh_info, message = message)

    else:
        return dict(wh_info = wh_info, message = None)

@route(whu.gen_route("/<wh>/picking-locations/edit-<plid>"))
@post(whu.gen_route("/<wh>/picking-locations/edit-<plid>"))
@view("views/admin/edit_pickingloc")
def edit_picking_location(wh, plid):
    check_admin()
    pl_info = adm.select_pickingloc_info(plid)
    if request.POST.get("update-picking-location"):
        locname = request.POST.get("location-name")
        upc = request.POST.get("upc")
        old_plname = pl_info[0][1]
        err = adm.update_pickingloc_info(wh, plid, old_plname,
                                         locname, upc)
        if err:
            err = "picking location name {0} already in use.".format(locname)
            return dict(pl_info = pl_info, wh = wh, plid = plid,
                        err = err)
        else:
            url = "/admin/manage-warehouses/{0}/picking-locations/edit-{1}".format(wh, plid)
            redirect(url)
    return dict(pl_info = pl_info, wh = wh, plid = plid, err = None)

@route(whu.gen_route("/<wh>/delete-pickingloc-<plid>"))
def delete_picking_location(wh, plid):
    check_admin()
    adm.delete_pickingloc(plid)
    url = "/admin/manage-warehouses/{0}/picking-locations".format(wh)
    redirect(url)

@route(whu.gen_route("/<wh>/picking-locations"))
@view(whu.gen_view("manage_pickinglocs"))
def manage_picking_locs(wh):
    check_admin()    
    wh_info = adm.select_warehouse_info(wh)
    whu.check_bm(wh_info)
    pickingloc_list = adm.select_pickinglocs_list(wh)
    return dict(pickingloc_list = pickingloc_list,
                wh_info = wh_info)
