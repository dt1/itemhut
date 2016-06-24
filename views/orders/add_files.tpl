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

      % if uploaded_files:
      % for f in uploaded_files:
      <p>{{f[0].split('/')[1]}} ({{f[1]}})
      <a href="/orders/add-order/order{{oid}}/delete-file{{sid}}/{{f[0]}}">delete</a></p>
      % end
      % end
      <form action="/orders/add-order/order{{oid}}/company{{sid}}-add-files"
	    method="POST"
	    enctype="multipart/form-data">

	<div class="row">
	  <div class="medium-3 columns">

	    <input type="file" name="upload">

	    <select name="ftype">
	      % for i in valid_ftypes:
	      <option value="{{i[0]}}">{{i[0]}}</option>
	      % end
	    </select>

	  </div>

	  <div class="medium-9 columns">
	  </div>
	</div>
	
	<input type="submit" class="button" name="add-file"
	       value="Add File">
	<a href="/orders/view-order-{{oid}}"
	   class="button">Done</a>
      </form>
    </div>
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
