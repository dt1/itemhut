<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% include('global/header_inv.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% include('global/top_nav_inv.tpl')

    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<h4>Vendors</h4>
	   	<ul class="vertical menu">
			<li>
			<a href = "/vendors">All</a>
			</li>
			<li>
			<a href = "/vendors/add-vendor">Add Vendor</a>
			</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <table id="table_id" class="display">
	   <thead>
		<tr>
		% for h in ["ID", "Name", ""]:
		<th>{{h}}</th>
		% end
		</tr>
	   </thead>
	   <tbody>
	   % for i in vendors:
	     <tr>
	     <td>{{i[0]}}</td>
	     <td>{{i[1]}}</td>
	     <td><a href="/vendors/{{i[0]}}">View / Edit</a></td>
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