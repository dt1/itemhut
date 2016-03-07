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
	   % include('warehouse/side_nav_menu.tpl', wh_id = wh_info[0][0])
	   </div>
	   
      	   <div class="medium-10 columns">
	   <h4>Add Picking Location</h4>
	   % if message:
	   <p>{{message}}</p>
	   % end
	   <form action="/warehouses/{{wh_info[0][0]}}/add-picking-location" method="POST">
	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Picking Location
	   <input type="text" name="picking-location" required="required">
	   </label>

	   <div class="medium-9 columns">
	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>SKU
		<select name="sku">
		<option value=""></option>
		% for item in sku_upc:
		<option value="{{item[0]}}">{{item[0]}}</option>
           	% end
		</select>
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>Qty
		<input type="number" min="1" name="qty">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>

	   </div>

	    <input type="submit" class="button"
	    value="Add Picking Location" name="add-picking-location">
	    </form>
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