<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Kits</h4>
    % include('products/product_side_nav')
  </div>
  
  <div class="medium-10 columns">
    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["Master SKU", "Child SKU(s)", "", ""]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for i in kits:
	<tr>
	  <td>{{i[0]}}</td>
	  <td>{{i[1]}}</td>
	  <td><a href="/products/update-kit-{{i[0]}}">
	      View / Edit</a></td>
	  <td><a href="/products/add-kit-children-{{i[0]}}">
	      Add children</a></td>
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
  margin-left:-27em;
  }

  .dataTables_paginate{
  margin-left:-22em;
  }
</style>
