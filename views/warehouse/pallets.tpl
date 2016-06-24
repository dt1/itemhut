<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4 color = >{{wh_info[0][1]}}</h4>
    % include('warehouse/side_nav_menu.tpl', wh_id = wh_info[0][0])
  </div>

  <div class="medium-10 columns">
    <h4>Pallets</h4>
    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["Pallet Location", "Pallet #",
	  % "Information", "Qty"]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for item in pallet_location_list:
	<tr class="table-anchor"
	    onclick="location.href='/warehouses/{{wh_info[0][0]}}/update-pallet-{{item[0]}}'">
	  <td>{{item[1]}}</td>
	  % if item[2]:
	  <td>{{item[2]}}</td>
	  % else:
	  <td>Empty</td>
	  % end
	  % if item[3]:
	  <td>{{item[3]}}</td>
	  % else:
	  <td>Empty</td>
	  % end
	  % if item[4]:
	  <td>{{item[4]}}</td>
	  % else:
	  <td>Empty</td>
	  % end
	</tr>
	% end
      </tbody>
    </table>
    <a href="/warehouses/{{wh_info[0][0]}}/create-pallet">
      Add Pallet</a>
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
