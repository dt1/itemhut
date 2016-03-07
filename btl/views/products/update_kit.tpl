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
	   <h4>Add Kit</h4>
	   	<ul class="vertical menu">
		</ul>
		% include('products/product_side_nav')
	   </div>

      	   <div class="medium-10 columns">
	   
	   <form action="/products/add-kit" method="POST" id="input-form">
	   <div class="row">
	   <div class="medium-3 columns">
	   <label> Master SKU
		<input type="text" name="master-sku" value="{{sku}}" required="required">
	   </label>

	   <div class="medium-9 columns">
	   </div>
	   </div>
	   </div>

	   <table id="table_id" class="display">
	   <thead>
		<tr>
		for h in ["", "SKU", "UPC"]:
		<th>{{h}}</th>
		% end
		</tr>
	   </thead>
	   <tbody>

		% for i in sku_upc:
		<tr>
		<td><input type="radio" name="upc" value="{{i[1]}}"></td>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		</tr>
		% end
	   </tbody>
	   </table>

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Qty
		<input type="number" min="1" name="qty"
		required="required">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	    <input type="submit" class="button" value="Add Kit" name="add-kit">

	   
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


% include('global/end_body.tpl')