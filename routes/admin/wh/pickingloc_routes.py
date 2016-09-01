# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import routes.admin.wh.wh_utils as whu

@route(whu.gen_route("/<wh>/add-picking-locations"))
@post(whu.gen_route("/<wh>/add-picking-locations"))
@view(whu.gen_view("add_picking_location"))
@check_admin
def add_picking_location(wh):
    wh_info = admwh.select_warehouse_info(wh)
    if not wh_info:
        return erro404("err")

    whu.check_bm(wh_info[0][6])

    d = {"wh" : wh}
    
    if request.POST.get("add-picking-location"):
        d["plname"] = request.POST.get("location-name")
        d["upc"] = request.POST.get("upc")
        err = admpic.insert_picking_location(d)
        if err:
            err = "{0} already exists".format(location_name)
            return dict(wh_info = wh_info, message = err)
        else:
            message = "Added {0}".format(d["plname"])
            return dict(wh_info = wh_info, message = message)

    elif request.POST.get("upload"):
        d["locfile"] = request.POST.get("loc-file")
        message = whu.upload_csv(admpic.bulk_load_pickinglocs, d["locfile"], d["wh"])
        return dict(wh_info = wh_info, message = message)

    else:
        return dict(wh_info = wh_info, message = None)

@route(whu.gen_route("/<wh>/picking-locations/edit-<plid>"))
@post(whu.gen_route("/<wh>/picking-locations/edit-<plid>"))
@view(whu.gen_view("edit_pickingloc"))
@check_admin
def edit_picking_location(wh, plid):
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
@check_admin
def delete_picking_location(wh, plid):
    adm.delete_pickingloc(plid)
    url = "/admin/manage-warehouses/{0}/picking-locations".format(wh)
    redirect(url)

@route(whu.gen_route("/<wh>/picking-locations"))
@view(whu.gen_view("manage_pickinglocs"))
@check_admin
def manage_picking_locs(wh):
    wh_info = admwh.select_warehouse_info(wh)
    whu.check_bm(wh_info)
    pickingloc_list = admpic.select_pickinglocs_list(wh)
    return dict(pickingloc_list = pickingloc_list,
                wh_info = wh_info)
