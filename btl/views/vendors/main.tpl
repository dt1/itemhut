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
	   	<h4>Vendors</h4>
	   	<ul class="vertical menu">
			<li>
				<a href = "/vendors/add-vendor">Add Vendor</a>
			</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <table id="table_id" class="display">
	   <thead>
		<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Phone</th>
		<th>Fax</th>
		<th>website</th>
		<th>email</th>
		<th>Street</th>
		<th>City</th>
		<th>State</th>
		<th>Zip</th>
		<th>Country</th>
		</tr>
	   </thead>
	   <tbody>
	   % for i in vendors:
	     <tr class="table-anchor" onclick="location.href='/vendors/{{i[0]}}'">
	     <td>{{i[0]}}</td>
	     <td>{{i[1]}}</td>
	     <td>{{i[2]}}</td>
	     <td>{{i[3]}}</td>
	     <td>{{i[4]}}</td>
	     <td>{{i[5]}}</td>
	     <td>{{i[6]}}</td>
	     <td>{{i[7]}}</td>
	     <td>{{i[8]}}</td>
	     <td>{{i[9]}}</td>
	     <td>{{i[10]}}</td>
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
margin-left:-17em;
}

.dataTables_paginate{
margin-left:-12em;
}
</style>

% include('global/end_body.tpl')