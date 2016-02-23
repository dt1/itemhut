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
			<p>Update <b>{{sku_data[0][0]}}</b></p>
	   </div>

      	   <div class="medium-10 columns">
	   <form action="/products/update-product-{{sku_data[0][0]}}" method="POST">

	   <div class="row">
	   <div class="medium-2 columns">
	   <label>Sku
	   	  <input type="text" name="sku" required="required"
		  value="{{sku_data[0][0]}}">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>UPC
	   	  <input type="text" name="upc"
		  value="{{sku_data[0][1]}}">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>SKU Type
	   <select name="sku-type">
	   % for item in sku_types:
	   % if item[0] == sku_data[0][2]:
	     <option value="{{item[0]}}" selected="selected">{{item[0]}}</option>
	   % else:
	     <option value="{{item[0]}}">{{item[0]}}</option>
	   % end
	   % end
	   </select>
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>Product Name
	   	  <input type="text" name="product-name"
		  value="{{sku_data[0][3]}}">
	   </label>
	   </div>

	   <div class="medium-4 columns">
	   </div>

	   </div>
	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Product Description
	   % if sku_data[0][4]:
	   <textarea name="product-description">{{sku_data[0][4]}}</textarea>
	   % else:
	   <textarea name="product-description"></textarea>
	   % end
           </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Image
	   % if sku_data[0][5]:
		<input type="text" name="main-image"
		value="{{sku_data[0][5]}}">
	   % else:
	   	<input type="text" name="main-image">
	   % end
	   </label>
	   <div class="medium-6 columns">
 	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-6 columns">

	   <div class="row">
	   <div class="medium-2 columns">
	   <input type="submit" class="button" value="Update Product" name="update-product">
	   </div>
	   </div>

	   </form>

      </div>

    </div>
  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')