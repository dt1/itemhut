<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>{{wh_info[0][1]}}</h4>
    % if wh_info[0][6] == "B&M":
    % include('admin/wh/side_nav_menu', whid = wh_info[0][0])
    % end
  </div>

  <div class="medium-10 columns">

    <h4>Picking Locations</h4>

    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["Picking Location", "sku", "upc", "", ""]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for i in pickingloc_list:
	<tr>
	  <td>{{i[1]}}</td>
	  <td>{{i[2]}}</td>
	  <td>{{i[3]}}</td>
	  <td><a href="/admin/manage-warehouses/{{wh_info[0][0]}}/picking-locations/edit-{{i[0]}}">
	      edit</a></td>
	  % if not i[2]:
	  <td><a href="/admin/manage-warehouses/{{wh_info[0][0]}}/delete-pickingloc-{{i[0]}}">
	      delete</a></td>
	  % else:
	  <td></td>
	  % end
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
