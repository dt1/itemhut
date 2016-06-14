<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="off-canvas-content" data-off-canvas-content>

  <div class="expanded row">
    <div class="medium-2 columns">
      <h4>Orders</h4>
      % include('orders/orders_side_nav.tpl')
    </div>

    <div class="medium-10 columns">
      <h4>Add Order</h4>
      % if err:
      <p>{{err}}</p>
      % elif new_order:
      <p>{{new_order}} added</p>
      % end

      <form action="/orders/add-order" method="POST">

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Order ID:
	      <input type="text" name="order-id"
		     required="required">
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Marketplace:
	      <select name="marketplace">
		% for i in market_list:
		<option value="{{i[0]}}">{{i[0]}}</option>
		% end
	      </select>
	    </label>
	  </div>

	  <div class="medium-3 columns">
	    <label>Salesperson ID:
	      <select name="salesperson-id" required="required">
		% for s in salesteam_list:
		<option name="salesperson-id" value="{{s[0]}}">
		  {{s[0]}} ; {{s[1]}}</option>
		% end
	      </select>
	    </label>
	  </div>

	  <div class="medium-3 columns">
	  </div>

	</div>

	<div class="row">
	  <div class="medium-3 columns">
	    <label>Ship to Customer?
	      <input type="checkbox" name="sameship">
	    </label>
	  </div>

	  <div class="medium-9 columns">
	  </div>

	</div>

	
	<div class="row">
	  <div class="medium-5 columns">
	    <table id="table_id" class="display">
	      <thead>
		<tr>
		  % for h in ["", "Company ID", "Company Name",
		  %           "Contact Name"]:
		  <th>{{h}}</th>
		  % end
		</tr>
	      </thead>
	      <tbody>
		% for i in companies:
		<tr>
		  <td><input type="radio" name="com-info"
			     value="{{i[0]}},{{i[1]}}"></td>
		  <td>{{i[2]}}</td>
		  <td>{{i[3]}}</td>
		  % if i[4]:
		  <td>{{i[4]}}</td>
		  % else:
		  <td></td>
		  % end
		</tr>
		% end
	      </tbody>
	    </table>

	  </div>
	</div>

	<div class="medium-9 columns">
	</div>

	<input type="submit" class="button" name="add-order"
	       value="Add Order">

      </form>
    </div>
  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>

