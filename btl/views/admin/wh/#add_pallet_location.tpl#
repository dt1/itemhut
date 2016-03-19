<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>{{wh_info[0][1]}}</h4>
    % if wh_info[0][6] == "B&M":
    % include('admin/wh/side_nav_menu', whid = wh_info[0][0])
    % end
  </div>

  <div class="medium-10 columns">

    % if message:
    <p>{{message}}</p>
    % end
    <h4>Add Pallet Location</h4>
    <form action="/admin/manage-warehouses/{{wh_info[0][0]}}/add-pallet-locations"
	  method="POST">
      <div class="row">
	<div class="medium-3 columns">
	  <label>Location Name
	    <input type="text" name="location-name" required="required">
	  </label>
	</div>

      </div>
      <div class="row">
	<div class="medium-3 columns">
	  <input type="submit" class="button" value="Add Pallet Location" name="add-pallet-location">
	</div>
      </div>
    </form>

    <h4>or bulk load</h4>
    <form action="/admin/manage-warehouses/{{wh_info[0][0]}}/add-pallet-locations"
	  method="POST"
	  enctype="multipart/form-data">
      <div class="row">
	<div class="medium-3 columns">
	  <label>Location Name
	    <input type="file" name="loc-file" required="required">
	  </label>
	</div>

      </div>
      <div class="row">
	<div class="medium-3 columns">
	  <input type="submit" class="button" value="Load Pallet Locations"
		 name="upload">
	</div>
      </div>
    </form>


  </div>
</div>
