<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
  </div>

  <div class="medium-10 columns">
    
    <h4>Edit Picking Location ({{pl_info[0][1]}})</h4>
    % if err:
    {{err}}
    % end
    
    <form action="/admin/manage-warehouses/{{wh}}/picking-locations/edit-{{plid}}"
	  method="POST">
      <div class="row">
	<div class="medium-3 columns">
	  <label>Location Name
	    <input type="text" name="location-name"
		   required="required" value="{{pl_info[0][1]}}">
	  </label>
	</div>

	<div class="medium-3 columns">
	  <label>UPC
	    <input type="text" name="upc"
		   % if pl_info[0][3]:
		   value="{{pl_info[0][3]}}"
		   % end
		   >
	  </label>
	</div>

	<div class="medium-6 columns">
	</div>

      </div>

      <div class="row">
	<div class="medium-3 columns">
	  <input type="submit" class="button"
		 value="Update Picking Location"
		 name="update-picking-location">
	</div>
      </div>
    </form>

  </div>
</div>
