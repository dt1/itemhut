# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from route_utils import *
import bcrypt

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

## pallet locations
@route("/admin/manage-warehouses/<wh>/add-pallet-locations")
@post("/admin/manage-warehouses/<wh>/add-pallet-locations")
@view("views/admin/add_pallet_location")
def add_pallet_location(wh):
    check_admin()
    wh_info = adm.select_warehouse_info(wh)
    if wh_info:
        check_bm(wh_info[0][6])
        if request.POST.get("add-pallet-location"):
            location_name = request.POST.get("location-name")
            err = adm.insert_pallet_location(wh, location_name)
            if err:
                err = "{0} already exists".format(location_name)
                return dict(wh_info = wh_info, message = err)
            else:
                message = "Added {0}".format(location_name)
                return dict(wh_info = wh_info, message = message)

        elif request.POST.get("upload"):
            locfile = request.POST.get("loc-file")
            message = upload_csv(adm.bulk_load_palletlocs, locfile, wh)
            return dict(wh_info = wh_info, message = message)

        else:
            return dict(wh_info = wh_info, message = None)

    else:
        return error404("err")

@route("/admin/manage-palletlocs-<wh>/edit-<plid>")
@post("/admin/manage-palletlocs-<wh>/edit-<plid>")
@view("views/admin/edit_palletloc_name")
def edit_pallet_location(wh, plid):
    check_admin()
    pl_name = adm.select_palletloc_name(plid)
    if request.POST.get("update-pallet-location"):
        locname = request.POST.get("location-name")
        err = adm.update_palletloc_name(plid, locname, wh)
        if err:
            err = "pallet location name {0} already in use.".format(locname)
            return dict(pl_name = pl_name, wh = wh, plid = plid,
                        err = err)
        else:
            url = "/admin/manage-palletlocs-{0}".format(wh)
            redirect(url)
    return dict(pl_name = pl_name, wh = wh, plid = plid, err = None)


@route("/admin/manage-warehouses/<wh>/delete-palletloc-<plid>")
def delete_pallet_location(wh, plid):
    check_admin()
    adm.delete_palletloc(plid)
    url = "/admin/manage-warehouses/{0}/pallet-locations".format(wh)
    redirect(url)

@route("/admin/manage-warehouses/<wh>/pallet-locations")
@view("views/admin/manage_palletlocs")
def manage_pallet_locs(wh):
    wh_info = adm.select_warehouse_info(wh)
    if wh_info[0][6] != "B&M":
        return error404("err")
    palletloc_list = adm.select_palletlocs_list(wh)
    return dict(palletloc_list = palletloc_list,
                wh_info = wh_info)

@route("/admin/add-warehouse")
@post("/admin/add-warehouse")
@view("views/admin/add_warehouse", wh_err = None)
def add_warehouse():
    check_admin()
    wh_types = adm.select_warehouse_types()
    if request.POST.get("add-warehouse"):
        warehouse_id = request.POST.get("warehouse-id")
        warehouse_name = request.POST.get("warehouse-name")
        street = request.POST.get("street")
        state = request.POST.get("state")
        zip = request.POST.get("zip_code")
        country = request.POST.get("country")
        warehouse_type = request.POST.get("wh-type")
        wh_id = adm.select_warehouse_id(warehouse_id)

        if " " in warehouse_id:
            err = "Warehouse ID has spaces in it."
            return dict (wh_err = err,
                         new_warehouse = warehouse_name,
                         wh_types = wh_types)

        if wh_id:
            wh_err = "{0} already exists. Try another ID".format(warehouse_id)
            return dict(new_warehouse = warehouse_name,
                        wh_types = wh_types, wh_err = wh_err)
        adm.insert_warehouse(warehouse_id, warehouse_name, street,
                             state,
                         zip, country, warehouse_type)
        return dict(new_warehouse = warehouse_name,
                    wh_types = wh_types)
    return dict(new_warehouse = None,
                wh_types = wh_types)

@route("/admin/manage-warehouses/<wh>")
@post("/admin/manage-warehouses/<wh>")
@view("views/admin/manage_warehouses_whinfo")
def manage_warehouses(wh):
    check_admin()
    wh_info = adm.select_warehouse_info(wh)
    if request.POST.get("update-warehouse"):
        wh_id = request.POST.get("wh-id")
        wh_name = request.POST.get("wh-name")
        wh_street = request.POST.get("wh-street")
        wh_state = request.POST.get("wh-state")
        wh_zip = request.POST.get("wh-zip")
        wh_country = request.POST.get("wh-country")

        if " " in wh_id:
            err = "Warehouse ID has spaces in it."
            return dict (wh_info = wh_info, err = err)

        err = adm.update_warehouse_info(wh, wh_id, wh_name, wh_street,
                                        wh_state, wh_zip, wh_country)
        if err:
            err = "Warehouse id {0} already in use.".format(wh_id)
            return dict (wh_info = wh_info, err = err)
        else:
            url = "/admin/manage-warehouses/{0}".format(wh_id)
            redirect (url)

    return dict(wh_info = wh_info, err = None)

@route("/admin/manage-warehouses")
@view("views/admin/manage_warehouses")
def manage_warehouses():
    check_admin()
    wh_list = adm.select_warehouse_list()
    return dict(wh_list = wh_list)
