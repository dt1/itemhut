<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Orders</h4>
    % include('orders/orders_side_nav.tpl')
  </div>
  
  <div class="medium-10 columns">
    <h4>All Orders</h4>

    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["Order ID", "Market Order ID", "Marketplace",
	  % "Company", "Order Date", "Salesperson", ""]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for i in all_orders:
	<tr>
	  <td>{{i[0]}}</td>
	  <td>{{i[1]}}</td>
	  <td>{{i[2]}}</td>
	  <td>{{i[3]}}</td>
	  <td>{{i[4]}}</td>
	  <td>{{i[5]}}</td>
	  <td><a href="/orders/view-order-{{i[0]}}">Edit / View</a></td>
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
