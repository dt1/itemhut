<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

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
	  % for h in ["SKU", "UPC", "SKU Type", "Product Name",
	  % ""]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for i in sku_upc:
	<tr>
	  <td>{{i["sku"]}}</td>
	  <td>{{i["upc"]}}</td>
	  <td>{{i["sku_type"]}}</td>
	  <td>{{i["product_name"]}}</td>
	  <td><a href="/products/update-product-{{i[0]}}">View / Edit</a></td>
	</tr>
	% end
      </tbody>
    </table>
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
