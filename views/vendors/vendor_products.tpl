<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    % include('vendors/vendor_side_nav.tpl', vendor_info = vendor_info)
  </div>

  <div class="medium-10 columns">

    <div class="row">
      <div class="medium-7 columns">
	<h5>Products</h5>
	<table id="table_id" class="display">
	  <thead>
	    <tr>
	      % for h in ["SKU", "UPC", ""]:
	      <th>{{h}}</th>
	      % end
	    </tr>
	  </thead>
	  <tbody>
	    % for product in vendor_products:
	    <tr>
	      <td>{{product[1]}}</td>
	      <td>{{product[0]}}</td>
	      <td><a href="/vendors/{{vendor_info[0][0]}}/products/delete-product-{{product[0]}}">delete</a></td>
	    </tr>
	    % end
	  </tbody>
	</table>
      </div>

    </div>
  </div>


</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>
