<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Orders</h4>
    % include('orders/orders_side_nav.tpl')
  </div>

{{shipto_info}}
  
  <div class="medium-10 columns">
    <h4>View Order ({{order_info[0][1]}})</h4>

    <div class="row">
      <div class="medium-4 columns">
	<p><b>Company: </b>{{order_info[0][7]}}</p>
	<p>{{order_info[0][12]}}</p>
	<p>{{order_info[0][13]}}, {{order_info[0][14]}}</p>
	<p>{{order_info[0][15]}}</p>
      </div>

      <div class="medium-4 columns">
	<p><b>Phone: </b>{{order_info[0][8]}} ; {{order_info[0][9]}}</p>
	<p><b>Fax: </b>{{order_info[0][10]}}</p>
	<p><b>Marketplace: </b>{{order_info[0][2]}}</p>
	<p><b>Order Date: </b>{{order_info[0][4]}}</p>
      </div>

      <div class="medium-4 columns">
	<p><b>Contact: </b>{{order_info[0][16]}}</p>
	<p><b>Phone: </b>{{order_info[0][17]}}, {{order_info[0][18]}}</p>
	<p><b>email: </b>{{order_info[0][19]}}</p>
      </div>
    </div>
    <hr>

    <div class="row">
      <div class="medium-12 columns">
	<a href="/orders/add-order/order{{order_info[0][0]}}/deliver-to"
	   class="button">Add Ship-to Company</a>
	<h4>Ship-to Information</h4>

	% for i in shipto_info:
	<div class="row">
	  <div class="medium-6 columns">
	    <p><b>Company:</b></p>
	    <p>{{i[3]}}</p>
	    <p>attn: {{i[4]}}</p>
	    <p>{{i[5]}}</p>
	    <p>{{i[6]}}, {{i[7]}} {{i[8]}}</p>
	    <p>{{i[9]}}</p>
	    <p><b>Ship By: </b>{{i[10]}}</p>
	    <p><b>Deliver By: </b>{{i[11]}}</p>
	    <a href="/orders/order{{shipto_info[0][0]}}/delete-shipto-record-{{shipto_info[0][1]}}"
	       class="button">Delete Record</a>
	    	    <a href="/orders/order{{shipto_info[0][0]}}/edit-deliver-to-{{shipto_info[0][1]}}"
	       class="button">Edit Company</a>

	  </div>

	  <div class="medium-6 columns">
	    <p><b>Items</b></p>
	    <ul>
	      % for item in i[12]:
	      % if item:
	      <li>{{item}}</li>
	      % end
	      % end
	    </ul>
	    <a href="/orders/add-order/order{{i[0]}}/company{{i[1]}}-add-products"
	       class="button">Manage Items</a>

	    <p><b>Files</b></p>
	    <ul>
	      % for item in i[13]:
	      % if item:
	      <li>
		<a href="/uploaded_files/orders/{{item.split(" ")[0].split(" ")[0]}}">
		  {{item.split("/")[1]}}
		</a>
	      </li>
	      % end
	      % end
	    </ul>
	    <a href="/orders/add-order/order{{i[0]}}/company{{i[1]}}-add-files"
	       class="button">Manage Files</a>

	  </div>
	</div>
	<hr>
	% end
      </div>
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
  margin-left:-20em;
  }
</style>
