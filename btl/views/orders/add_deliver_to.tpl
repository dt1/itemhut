<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="off-canvas-content" data-off-canvas-content>

  <div class="expanded row">
    <div class="medium-2 columns">
      <h4>Orders</h4>
      % include('orders/orders_side_nav.tpl')
    </div>
{{mlist}}
    <div class="medium-10 columns">
      % if mlist[0][1]:
      <h4>Add Deliver To (order: {{mlist[0][1]}})</h4>
      % else:
      <h4>Add Deliver To (order: {{mlist[0][0]}})</h4>
      % end

      <form action="/orders/add-order" method="POST">
	<div class="row">
	  <div class="medium-3 columns">
	    <label>Order ID:
	      <input type="text" name="company" required="required">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Attn:
	      <input type="text" name="attn">
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
	      <input type="text" name="street">
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<div class="row">
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
	    <label>Country
	      <input type="text" name="country">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Ship By
	      <input type="text" name="state">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Deliver By
	      <input type="text" name="zip">
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<input type="submit" class="button" name="another-company"
	       value="Add Another Company">

	<a href="/orders/add-order/order{{mlist[0][0]}}/list-companies"
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

