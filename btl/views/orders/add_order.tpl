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

	   <div class="medium-9 columns">
	   </div>      
	   </div>      

	   <div class="row">
	   <div class="medium-3 columns">
	   	   <label>Marketplace:
	   	   <input type="text" name="marketplace"
		   required="required">
	   	   </label>
	   </div>      

	   <div class="medium-9 columns">
	   </div>      
	   </div>      

	   <div class="row">
	   <div class="medium-3 columns">
	   <input list="mskus" name="msku"></label>
	   <datalist id="mskus">
		% for item in msku_list:
		<option value="{{item[0]}}">
           	% end
		</datalist>
	   </div>      

	   <div class="medium-9 columns">
	   </div>      
	   </div>      

	   <div class="row">
	   <div class="medium-3 columns">
	   	   <label>Qty:
	   	   <input type="number" name="qty" required="required">
	   	   </label>
	   </div>      

	   <div class="medium-9 columns">
	   </div>      
	   </div>      

	   <input type="submit" class="button" name="add-order"
	   value="Add Order">


	   </form>
	   </div>      
      </div>
    </div>

  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')