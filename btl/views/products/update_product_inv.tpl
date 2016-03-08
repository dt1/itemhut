<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <p>Update <b>{{sku_data[0][0]}}</b></p>
  </div>

  <div class="medium-10 columns">
    <form action="/products/update-product-{{sku_data[0][0]}}"
	  method="POST" enctype="multipart/form-data">

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
	  % if sku_data[0][5]:
	  <img src="/uploaded_files/images/{{sku_data[0][5]}}"
	       width="100px;"/>
	  % else:
	  <p>no image</p>
	  % end
	  <label>Replace Image
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
	      <input type="submit" class="button" value="Update Product" name="update-product">
	    </div>
	  </div>
	</div>
      </div>
    </form>
  </div>
</div>

