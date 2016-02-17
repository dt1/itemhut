<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   <h4 color = >{{warehouse_name}}</h4>
	   <p>Pallet Locations</p>
	   </div>
	   
      	   <div class="medium-10 columns">
	   
	   <table id="table_id" class="display">
	   <thead>
		<tr>
		<th>pallet_location</th>
		<th>pallet #</th>
		<th>Information</th>
		<th>Qty</th>
		</tr>
	    </thead>
	    </tbody>
		% for item in pallet_location_list:
		<tr>
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


% include('global/end_body.tpl')