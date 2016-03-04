<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% if inv:
% include('global/header_inv.tpl')
% else:
% include('global/header.tpl')
%end

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% if inv:
% include('global/top_nav_inv.tpl')
% else:
% include('global/top_nav.tpl')
% end


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   <h4>Add Product</h4>
	   % include('products/product_side_nav')
	   </div>

      	   <div class="medium-10 columns">
	   % if new_sku:
	   <p>Added {{new_sku}}</p>
	   % end
	   <form action="/products/add-kit" method="POST"
	   enctype="multipart/form-data">

	   <div class="row">
	   <div class="medium-2 columns">
	   <label>Sku
	   	  <input type="text" name="sku" required="required">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>Product Name
	   	  <input type="text" name="product-name" required="required">
	   </label>
	   </div>

	   <div class="medium-4 columns">
	   </div>

	   </div>
	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Product Description
	   		  <textarea name="product-description"></textarea>
           </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Image
		<input type="file" name="main-image">
	   </label>
	   <div class="medium-6 columns">
 	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-6 columns">

	   <div class="row">
	   <div class="medium-2 columns">
	   <input type="submit" class="button" value="Add Kit" name="add-product">
	   </div>
	   </div>

	   </form>
	   </div>
      </div>

    </div>
  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')