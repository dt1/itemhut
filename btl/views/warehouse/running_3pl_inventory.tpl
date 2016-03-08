<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4 color = >{{wh_info[0][1]}}</h4>
    % include('warehouse/side_nav_3pl_menu.tpl', wh_id = wh_info[0][0])
  </div>

  <div class="medium-10 columns">
    <h4>Running Inventory</h4>
    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["SKU", "UPC", "Qty", ""]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for item in sku_count:
	<tr>
	  <td>{{item[0]}}</td>
	  <td>{{item[1]}}</td>
	  <td>{{item[2]}}</td>
	  <td><a href="/warehouses/{{wh_info[0][0]}}/update-running-inventory-{{item[0]}}">View / Edit</a></td>
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
