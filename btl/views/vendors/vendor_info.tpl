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
	   	<h4>{{vendor_info[0][1]}}</h4>
		<ul class="vertical menu">
		<li><a href="/vendors/{{vendor_info[0][0]}}">
		Information</a></li>
		<li><a href="/vendors/{{vendor_info[0][0]}}/contacts">
		 Contacts</a></li>
		<li><a href="/vendors/{{vendor_info[0][0]}}/products">
		 Products</a></li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">

	   <div class="row">
	   <div class="medium-5 columns">
	   <p><b>{{vendor_info[0][1]}}</b></p>
	   <p>{{vendor_info[0][6]}}</p>
	   <p>{{vendor_info[0][7]}}, {{vendor_info[0][8]}}
	      {{vendor_info[0][9]}}</p>
	   <p>country: {{vendor_info[0][10]}}</p>
	   </div>

	   <div class="medium-7 columns">
	   <p><b>phone</b>: {{vendor_info[0][2]}}</p>
	   <p><b>fax</b>: {{vendor_info[0][3]}}</p>
	   <p><b>website</b>: {{vendor_info[0][4]}}</p>
	   <p><b>email</b>: {{vendor_info[0][5]}}</p>
	   </div>
	   <a href="/vendors/{{vendor_info[0][0]}}/edit-vendor">
	      Edit {{vendor_info[0][1]}} Information</a>
	   </div>
	   <br>



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