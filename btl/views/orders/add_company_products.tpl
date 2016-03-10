<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Add Order</h4>
    % include('orders/orders_side_nav.tpl')
  </div>
  <div class="medium-10 columns">
    <div class="row">
      % if mlist[0][1]:
      <h4>Add Product to {{mlist[0][3]}} (order: {{mlist[0][1]}})</h4>
      % else:
      <h4>Add Product to {{mlist[0][3]}} (order: {{mlist[0][0]}})</h4>
      % end

      % if added_plist:
      % for i in added_plist:
      <p>{{i[0]}} ({{i[1]}}) <a href="/orders/add-order/order{{oid}}/company{{sid}}-delete-product-{{i[0]}}">delete</a></p>
      % end
      % end
      
      <form action="/orders/add-order/order{{oid}}/company{{sid}}-add-products"
	    method="POST">
	<table id="table_id" class="display">
	  <thead>
	    % for h in ["", "sku", "marketplace sku", "Name"]:
	    <th>{{h}}</th>
	    % end
	  </thead>
	  <tbody>
	    % for i in pclist:
	    <tr>
	      <td>
		<input type="radio" name="msku" value="{{i[1]}}">
	      </td>
	      <td>{{i[0]}}</td>
	      <td>{{i[1]}}</td>
	      <td>{{i[2]}}</td>
	    </tr>
	    % end
	  </tbody>
	</table>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<input type="number" name="qty" min="1" required="required">
      </div>
    </div>

    <input type="submit" class="button" name="add-product"
	   value="Add Product">
    <a href="/orders/add-order/order{{oid}}/list-companies"
       class="button">Done</a>
    </form>
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
  margin-left:-10em;
  }
</style>
