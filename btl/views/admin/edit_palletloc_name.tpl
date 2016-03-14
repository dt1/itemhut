<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
  </div>

  <div class="medium-10 columns">
    
    <h4>Edit Pallet Location ({{pl_name[0][0]}})</h4>

    % if err:
    {{err}}
    % end
    
    <form action="/admin/manage-warehouses/{{wh}}/pallet-locations/edit-{{plid}}"
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
	  <input type="submit" class="button" value="Update Pallet Location" name="update-pallet-location">
	</div>
      </div>
    </form>

  </div>
</div>
