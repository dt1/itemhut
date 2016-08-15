# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import routes.admin.wh.wh_utils as whu

@route(whu.gen_route("/<wh>/add-pallet-locations"))
@post(whu.gen_route("/<wh>/add-pallet-locations"))
@view(whu.gen_view("add_pallet_location"))
def add_pallet_location(wh):
    check_admin()
    wh_info = admwh.select_warehouse_info(wh)
    if not wh_info:
        return error404("err")

    whu.check_bm(wh_info[0][6])
    if request.POST.get("add-pallet-location"):
        location_name = request.POST.get("location-name")
        err = admpal.insert_pallet_location(wh, location_name)
        if err:
            err = "{0} already exists".format(location_name)
            return dict(wh_info = wh_info, message = err)
        else:
            message = "Added {0}".format(location_name)
            return dict(wh_info = wh_info, message = message)

    elif request.POST.get("upload"):
        locfile = request.POST.get("loc-file")
        message = whu.upload_csv(admpal.bulk_load_palletlocs, locfile, wh)
        return dict(wh_info = wh_info, message = message)

    else:
        return dict(wh_info = wh_info, message = None)

@route(whu.gen_route("/<wh>/pallet-locations/edit-<plid>"))
@post(whu.gen_route("/<wh>/pallet-locations/edit-<plid>"))
@view(whu.gen_view("edit_palletloc_name"))
def edit_pallet_location(wh, plid):
    check_admin()
    pl_name = admpal.select_palletloc_name(plid)
    if request.POST.get("update-pallet-location"):
        locname = request.POST.get("location-name")
        err = admpal.update_palletloc_name(plid, locname, wh)
        if err:
            err = "pallet location name {0} already in use.".format(locname)
            return dict(pl_name = pl_name, wh = wh, plid = plid,
                        err = err)
        else:
            url = whu.gen_route("/{0}/pallet-locations/edit-{1}".format(wh, plid))
            redirect(url)
    return dict(pl_name = pl_name, wh = wh, plid = plid, err = None)


@route(whu.gen_route("/<wh>/delete-palletloc-<plid>"))
def delete_pallet_location(wh, plid):
    check_admin()
    admpal.delete_palletloc(plid)
    url = whu.gen_route("/{0}/pallet-locations".format(wh))
    redirect(url)

@route(whu.gen_route("/<wh>/pallet-locations"))
@view(whu.gen_view("manage_palletlocs"))
def manage_pallet_locs(wh):
    wh_info = admwh.select_warehouse_info(wh)
    whu.check_bm(wh_info[0][6])
    palletloc_list = admpal.select_palletlocs_list(wh)
    return dict(palletloc_list = palletloc_list,
                wh_info = wh_info)
