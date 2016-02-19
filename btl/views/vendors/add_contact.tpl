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
	   	<h4>Add Contact</h4>
	   	<ul class="vertical menu">
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   % if contact_name:
	   <p>{{contact_name}} added</p>
	   % end
	   <div class="row">
      	   <div class="medium-4 columns">
	   <form action="/vendors/{{vid}}/add-contact" method="POST">
	   	 <label>Name
		 <input type="text" name="name" required="required">
		 </label>
	   	 
		 <label>Title
		 <input type="text" name="title">
		 </label>
	   	 
		 <label>Phone
		 <input type="text" name="phone">
		 </label>
	   	 
		 <label>Phone 2
		 <input type="text" name="alt-phone">
		 </label>

		 <label>email
		 <input type="text" name="email">
		 </label>
	   <input type="submit" class="button" name="add-contact" value="Add Contact">
	   <form>
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