<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% if inv:
% include('global/header_inv.tpl')
% else:
% include('global/header.tpl')
%end

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% if inv:
% include('global/top_nav_inv.tpl')
% else:
% include('global/top_nav.tpl')
% end


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>
      <div class="expanded row">
      	   <div class="medium-2 columns">
	   <h4 color = >{{wh_info[0][1]}}</h4>
	   % include('warehouse/side_nav_menu.tpl', wh_id = wh_info[0][0])
	   </div>
      	   <div class="medium-10 columns">
	   <h4>Pallet Locations</h4>

	   <a href="/warehouses/{{wh_info[0][0]}}/add-pallet-location">
	   Add Pallet Location</a>

	   <table id="table_id" class="display">
	   <thead>
		<tr>
		<th width="200px">Pallet Location</th>
		<th width="150px">pallet #</th>
		<th>Information</th>
		<th>Qty</th>
		<th></th>
		</tr>
	    </thead>
	    </tbody>
		% for item in pallet_location_list:
		<tr class="table-anchor"
		onclick="location.href='/warehouses/{{wh_info[0][0]}}/update-pallet-{{item[2]}}'">
		<td>{{item[1]}}</td>
		% if item[2]:
		<td>{{item[2]}}</td>
		% else:
		<td>Empty</td>
		% end
		% if item[3]:
		<td>
		% for ii in item[3].split(";;"):
		{{ii}}<br>
		% end
		</td>
		% else:
		<td>Empty</td>
		% end
		% if item[4]:
		<td>
		% for ii in item[4].split(";;"):
		{{ii}}<br>
		% end
		% else:
		<td>Empty</td>
		% end
		<td><a href="/warehouses/{{wh_info[0][0]}}/delete-pallet-location-{{item[0]}}">delete</a></td>
		</tr>
		% end
	   </tbody>
	   </table>
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
margin-left:-27em;
}

.dataTables_paginate{
margin-left:-5em;
}
</style>

% include('global/end_body.tpl')