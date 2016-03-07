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
	   % include('vendors/vendor_side_nav.tpl', vendor_info = vendor_info)
	   </div>
	   
      	   <div class="medium-10 columns">

	   <div class="row">
	   <div class="medium-5 columns">
	   	<h5>Contacts</h5>
	      <table id="table_id" class="display">
	      <thead>
	      <tr>
	      % for h in ["Name", "Title", "Phone", "Phone2", "email",
	                % ""]:
	      <th>{{h}}</th>
	      % end
	      </tr>
	      </thead>
	      <tbody>
	      % for i in contacts:
	      <tr>
	      	<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
	      	<td>{{i[3]}}</td>
	      	<td>{{i[4]}}</td>
	      	<td>{{i[5]}}</td>
	      	<td><a href="/vendors/{{vendor_info[0][0]}}/contacts/edit-contact-{{i[0]}}">View / Edit</a></td>
		</tr>
		% end
		</tbody>
		</table>
	   </div>

	   </div>
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