<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4 color = >{{wh_info[0][1]}}</h4>
    % include('warehouse/side_nav_menu.tpl', wh_id = wh_info[0][0])
  </div>

  <div class="medium-10 columns">

    % if location_name:
    <p>Added {{location_name}}</p>
    % end
    <h4>Add Pallet Location</h4>
    <form action="/warehouses/{{wh_info[0][0]}}/add-pallet-location" method="POST">
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


  </div>
</div>
