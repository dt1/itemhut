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
	   <h4>Add Company</h4>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <h4>Add Company</h4>

	   <div class="row">
	   <form action="/companies/add-company" method="POST">
	   <div class="medium-3 columns">
	   	  <label>Company ID
		  <input type="text" name="company-uid"
		  required="required">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	   	  <label>Company Name
		  <input type="text" name="company-name"
		  required="required">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	  <label>Phone 1
		  <input type="text" name="phone-one">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	   	  <label>Phone 2
		  <input type="text" name="phone-two">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	  <label>Fax
		  <input type="text" name="fax">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	  <label>email
		  <input type="email" name="email">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	  <label>Street
		  <input type="text" name="street">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	   	  <label>State
		  <input type="text" name="state">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	   	  <label>Zip
		  <input type="text" name="zip">
		  </label>
	    </div>
	   <div class="medium-3 columns">
	    </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	  <label>Country
		  <input type="text" name="country">
		  </label>
	    </div>
	    </div>

	   <div class="row">
		<input type="submit" class="button" name="add-company"
		value="Add Company">
	   </div>
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

% include('global/end_body.tpl')