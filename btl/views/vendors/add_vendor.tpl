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
	   	<h4>Add Vendor</h4>
	   </div>
	   
      	   <div class="medium-10 columns">
	   % if new_vendor:
	   	   <p>Added {{new_vendor}}</p>
	   % end

	   <form action="/vendors/add-vendor" method="POST">

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Vendor ID
		<input type="text" name="vendor-id" required="required">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>Vendor Name
		<input type="text" name="vendor-name" required="required">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Phone
		<input type="text" name="phone-one">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>fax
		<input type="text" name="fax">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Website
		<input type="text" name="website">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>Email
		<input type="email" name="email">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Street
		<input type="text" name="street">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>City
		<input type="text" name="city">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>State
		<input type="text" name="state">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   </div>
	   </div>


	   <div class="row">
	   <div class="medium-3 columns">
	   <label>Zip Code
		<input type="text" name="zip">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>Country
		<input type="text" name="country">
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   </div>
	   </div>
	   	   <input type="submit" class="button" value="Add Vendor" name="add-vendor">

	   </form>
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