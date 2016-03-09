<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

{{mlist}}

<div class="off-canvas-content" data-off-canvas-content>

  <div class="expanded row">
    <div class="medium-2 columns">
      <h4>Orders</h4>
      % include('orders/orders_side_nav.tpl')
    </div>

    <div class="medium-10 columns">
      % if mlist[0][1]:
      <h4>Add Deliver To (order: {{mlist[0][1]}})</h4>
      % else:
      <h4>Add Deliver To (order: {{mlist[0][0]}})</h4>
      % end

      <form action="/orders/add-order/order{{mlist[0][0]}}/deliver-to"
	    method="POST">
	<div class="row">
	  <div class="medium-3 columns">
	    <label>Company
	      <input type="text" name="company"
		     % if mlist[0][3]:
		     value="{{mlist[0][3]}}"
		     % end
		     required="required"
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Attn:
	      <input type="text" name="attn"
		     % if mlist[0][4]:
		     value="{{mlist[0][4]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Street
	      <input type="text" name="street"
		     % if mlist[0][5]:
		     value="{{mlist[0][5]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>City
	      <input type="text" name="city"
		     % if mlist[0][6]:
		     value="{{mlist[0][6]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>State
	      <input type="text" name="state"
		     % if mlist[0][7]:
		     value="{{mlist[0][7]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Zip
	      <input type="text" name="zip"
		     % if mlist[0][8]:
		     value="{{mlist[0][8]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Country
	      <input type="text" name="country"
		     % if mlist[0][9]:
		     value="{{mlist[0][9]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Ship By
	      <input type="date" name="ship-by"
		     % if mlist[0][10]:
		     value="{{mlist[0][10]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Deliver By
	      <input type="date" name="deliver-by"
		     % if mlist[0][11]:
		     value="{{mlist[0][11]}}"
		     % end
		     >
	    </label>
	  </div>

	  <div class="medium-6 columns">
	  </div>

	</div>

	<input type="submit" class="button" name="another-company"
	       value="Add Another Company">

	<input type="submit" class="button" name="done"
	       value="Done With Companies">
	
      </form>
    </div>
  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>

