<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->


% include('global/header_inv.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% include('global/top_nav_inv.tpl')

    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   <h4 color = >{{wh_info[0][1]}}</h4>

	   	<ul class="vertical menu">
		<li><a href = "/warehouses/{{wh_info[0][0]}}/information">Information</a></li>
		<li><a href = "/warehouses/{{wh_info[0][0]}}/running-inventory">Running Inventory</a></li>
		<li><a href = "/warehouses/{{wh_info[0][0]}}/pallet-locations">Pallet Locations</a></li>
		<li><a href = "/warehouses/{{wh_info[0][0]}}/pallets">Pallets</a></li>
		<li><a href = "/warehouses/{{wh_info[0][0]}}/product-status">Product Status</a></li>
		<li><a href = "/warehouses/{{wh_info[0][0]}}/qc-log">QC Logs</a></li>
		</ul>
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

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

<script>
$(document).ready( function () {
    $('#table_id').DataTable();
} );
</script>


% include('global/end_body.tpl')