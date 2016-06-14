<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Order Scan Out</h4>
  </div>
  
  <div class="medium-10 columns">
    % if err:
    <p>{{err}}</p>
    % end
    <form action="/warehouses/cases/new-config", method="POST">
      <table id="table_id" class="display">
	<thead>
	  <tr>
	    % for h in ["Internal Order ID", "Order ID", "SKU", "QTY", "Ship By Date"]:
	    <th>{{h}}</th>
	    % end
	  </tr>
	</thead>
	<tbody>
	  % for i in orders:
	  <tr>
	    <td>{{i[0]}}</td>
	    <td>{{i[1]}}</td>
	    <td>{{i[2]}}</td>
	    <td>{{i[3]}}</td>
	    <td>{{i[4]}}</td>
	  </tr>
	  % end
	<tbody>
      </table>
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
