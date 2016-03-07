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
	   	<h4>Products</h4>
		% include('products/product_side_nav')
	   </div>
	   
      	   <div class="medium-10 columns">
	   <h4>All Products</h4>
	   <table id="table_id" class="display">
	   <thead>
		<tr>
		<th>SKU</th>
		<th>UPC</th>
		<th>SKU Type</th>
		<th>Product Name</th>
		<th></th>
		</tr>
	   </thead>
	   <tbody>
	   % for i in sku_upc:
		<tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
		<td>{{i[3]}}</td>
		<td><a href="/products/update-product-{{i[0]}}">View / Edit</a></td>
		</tr>
		% end
	   </tbody>
	   </table>	   </div>      
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