<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="off-canvas-content" data-off-canvas-content>

  <div class="expanded row">
    <div class="medium-2 columns">
      <h4>Orders</h4>
      % include('orders/orders_side_nav.tpl')
    </div>
{{shipto_info}}
    <div class="medium-10 columns">
      % if mlist[0][1]:
      <h4>Add Deliver To (order: {{mlist[0][1]}})</h4>
      % else:
      <h4>Add Deliver To (order: {{mlist[0][0]}})</h4>
      % end

      <form action="/orders/order{{shipto_info[0][0]}}/edit-deliver-to-{{shipto_info[0][1]}}" method="POST">
	<div class="row">
	  <div class="medium-3 columns">
	    <label>Company:
	      <input type="text" name="company"
		     value="{{shipto_info[0][3]}}"
		     required="required">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Attn:
	      <input type="text" name="attn"
		     value="{{shipto_info[0][4]}}">
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Street
	      <input type="text" name="street"
		     value="{{shipto_info[0][5]}}">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>City
	      <input type="text" name="city"
		     value="{{shipto_info[0][6]}}">
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>State
	      <input type="text" name="state"
		     value="{{shipto_info[0][7]}}">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Zip
	      <input type="text" name="zip"
		     value="{{shipto_info[0][8]}}">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Country
	      <input type="text" name="country"
		     value="{{shipto_info[0][9]}}">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Ship By
	      <input type="text" name="ship-by"
		     % if shipto_info[0][10]:
		     value="{{shipto_info[0][10]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Deliver By
	      <input type="text" name="deliver-by"
		     % if shipto_info[0][11]:
		     value="{{shipto_info[0][11]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<input type="submit" class="button" name="edit-company"
	       value="Submit">

	<a href="/orders/view-order-{{mlist[0][0]}}"
	   class="button">
	  Done With Companies</a>
	
      </form>
    </div>
  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>

