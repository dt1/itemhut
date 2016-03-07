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
	   <h4 color = >{{wh_info[0][1]}}</h4>
	   <p>Add Product</p>
	   % include('warehouse/side_nav_3pl_menu.tpl', wh_id = wh_info[0][0])
	   
	   </div>


      	   <div class="expanded row">


      	   <div class="medium-2 columns">
	   % if upc:
	   <p>Added {{upc}}</p>
	   % end
	   <form action="/warehouses/{{wh_info[0][0]}}/add-product"
	   method="POST">
	   
	   <div class="row">

	   <label>UPC
	   <select name="upc">
	   % for i in sku_upc:
	   <option value="{{i[1]}}">{{i[1]}}</option>
	   % end
	   </select>
	   </label>
	   <label>QTY
	   <input type="number" min="0" name="qty">
	   </label>

	   <input type="submit" class="button" name="add-product"
	   value="Add UPC">

	   </form>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')