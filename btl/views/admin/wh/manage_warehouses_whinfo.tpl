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
    <h4></h4>
    % if err:
    <p>{{err}}</p>
    % end
    
    <form action="/admin/manage-warehouses/{{wh_info[0][0]}}"
	  method="POST">

      <div class="row">
	<div class="medium-2 columns">
	  <label>ID:
	    <input type="text" name="wh-id" required="required"
		   value="{{wh_info[0][0]}}">
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-4 columns">
	  <label>Name:
	    <input type="text" name="wh-name"
		   % if wh_info[0][1]:
		   value="{{wh_info[0][1]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>


      <div class="row">
	<div class="medium-4 columns">
	  <label>Street:
	    <input type="text" name="wh-street"
		   % if wh_info[0][1]:
		   value="{{wh_info[0][2]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-2 columns">
	  <label>State:
	    <input type="text" name="wh-state"
		   % if wh_info[0][1]:
		   value="{{wh_info[0][3]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-6 columns">
	</div>
      </div>
      
      <div class="row">
	<div class="medium-4 columns">
	  <label>Zip:
	    <input type="text" name="wh-zip"
		   % if wh_info[0][1]:
		   value="{{wh_info[0][4]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-2 columns">
	  <label>Country:
	    <input type="text" name="wh-country"
		   % if wh_info[0][1]:
		   value="{{wh_info[0][5]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-6 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-2 columns">
	  <input type="submit" class="button" value="Update Warehouse"
		 name="update-warehouse">
	</div>
      </div>
    </form>

  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>

<style>

  .dataTables_length{
  width: 5em;
  }

  .dataTables_filter{
  width:15em;
  margin-left:-25em;
  }

  .dataTables_paginate{
  margin-left:-20em;
  }
</style>
