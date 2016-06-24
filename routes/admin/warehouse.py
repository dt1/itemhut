# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bcrypt

def gen_view(v):
    return "views/admin/{0}".format(v)

def gen_route(r):
    return "/admin/manage-warehouses{0}".format(r)
    
## picking locations
@route(gen_route("<wh>/add-picking-locations"))
@post(gen_route("<wh>/add-picking-locations"))
@view(gen_view("add_picking_location"))
def add_picking_location(wh):
    check_admin()
    wh_info = adm.select_warehouse_info(wh)
    if wh_info:
        check_bm(wh_info[0][6])
        if request.POST.get("add-picking-location"):
            location_name = request.POST.get("location-name")
            err = adm.insert_picking_location(wh, location_name)
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

    else:
        return error404("err")

@route("/admin/manage-pickinglocs-<wh>/edit-<plid>")
@post("/admin/manage-pickinglocs-<wh>/edit-<plid>")
@view("views/admin/edit_pickingloc_name")
def edit_picking_location(wh, plid):
    check_admin()
    pl_name = adm.select_pickingloc_name(plid)
    if request.POST.get("update-picking-location"):
        locname = request.POST.get("location-name")
        err = adm.update_pickingloc_name(plid, locname, wh)
        if err:
            err = "picking location name {0} already in use.".format(locname)
            return dict(pl_name = pl_name, wh = wh, plid = plid,
                        err = err)
        else:
            url = "/admin/manage-pickinglocs-{0}".format(wh)
            redirect(url)
    return dict(pl_name = pl_name, wh = wh, plid = plid, err = None)


@route("/admin/manage-warehouses/<wh>/delete-pickingloc-<plid>")
def delete_picking_location(wh, plid):
    check_admin()
    adm.delete_pickingloc(plid)
    url = "/admin/manage-warehouses/{0}/picking-locations".format(wh)
    redirect(url)

@route(gen_route("/<wh>/picking-locations"))
@view(gen_view("manage_pickinglocs"))
def manage_picking_locs(wh):
    check_admin()    
    wh_info = adm.select_warehouse_info(wh)
    check_bm(wh_info)
    pickingloc_list = adm.select_pickinglocs_list(wh)
    return dict(pickingloc_list = pickingloc_list,
                wh_info = wh_info)
