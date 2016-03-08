<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="off-canvas-content" data-off-canvas-content>

  <div class="expanded row">
    <div class="medium-2 columns">
      <h4>Incoming</h4>
      % include('incoming/side_nav_menu')
      
    </div>
    
    <div class="medium-10 columns">
      <div class="row">
      	<div class="medium-4 columns">
	  
	  <p><b>Invoice</b>: {{order_info[0][1]}}<p>
	  <p><b>Vendor ID</b>: {{order_info[0][2]}}<p>
	  <p><b>Order Date</b>: {{order_info[0][3]}}<p>
	  <p><b>ETA</b>: {{order_info[0][4]}}<p>
	  <p><b>Completed?</b> {{order_info[0][5]}}<p>
	  <p><a href="/uploaded_files/invoices/{{order_info[0][6]}}">Invoice File</a><p>
	    <form action="/incoming/update-order-{{order_info[0][0]}}"
		  method="POST">
	      <input type="submit" class="button" name="arrived"
		     value="Arrived">
	    </form>
	</div>

      	<div class="medium-3 columns">
	  <h5>Products:</h5>
	  <table>
	    <thead>
	      <tr>
		% for h in ["SKU", "UPC", "qty"]:
		<th>{{h}}</th>
		% end
	      </tr>
	    </thead>
	    <tbody>
	      % for i in products:
	      <tr>
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
		% end
	      </tr>
	    </tbody>
	  </table>
	  <form action="/incoming/update-order-{{order_info[0][0]}}"
		method="POST" id="input-form">
	    
	    <p>Add Product</p>
	    <label>UPC
	      <input name="upc" list="upc" required="required"></label>
	    <datalist id="upc">
	      % for i in upc_list:
	      <option value="{{i[0]}}">{{i[0]}}</option>
	      % end
	    </datalist>
	    
	    <label>Qty
	      <input type="number" min="1" required="required" name="qty">
	    </label>
	    <input type="submit" class="button" name="add-product"
		   value="Add Product">
	  </form>
	</div>

      	<div class="medium-5 columns">

	</div>      

      </div>      



    </div>
  </div>

</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );

  $('#input-form input, #input-form select').change(function() {
  $('#upc').val(this.value);
  });

</script>
