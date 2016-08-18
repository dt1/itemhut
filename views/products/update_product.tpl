<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <p>Update <b>{{sku_data[0][0]}}</b></p>

    <svg id="barcode"></svg>

  </div>

  <div class="medium-10 columns">
    <form action="/products/update-product-{{sku_data[0]['sku']}}"
	  method="POST" enctype="multipart/form-data">

      <div class="row">
	<div class="medium-2 columns">
	  <label>Sku
	    <input type="text" name="sku" required="required"
		   value="{{sku_data[0]['sku']}}">
	  </label>
	</div>

	<div class="medium-2 columns">
	  <label>UPC
	    <input type="text" name="upc"
		   value="{{sku_data[0]['upc']}}">
	  </label>
	</div>

	<div class="medium-2 columns">
	  <label>SKU Type
	    <select name="sku-type">
	      % for item in sku_types:
	      % if item[0] == sku_data[0]['sku_type']:
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
		   value="{{sku_data[0]['product_name']}}">
	  </label>
	</div>

	<div class="medium-4 columns">
	</div>

      </div>

      <div class="row">
	<div class="medium-6 columns">
	  <label>Product Description
	    % if sku_data[0][4]:
	    <textarea name="product-description">{{sku_data[0]["product_description"]}}</textarea>
	    % else:
	    <textarea name="product-description"></textarea>
	    % end
	  </label>
	  <div class="medium-6 columns">
	  </div>
	</div>
      </div>

      % for item in ["one", "two", "three", "four", "five"]:
      % bnum = "bullet_" + item
      <div class="row">
	<div class="medium-6 columns">
	  <label>Bullet {{item.title()}}
	    <input type="text" name="bullet-{{item}}"
		   value = "{{sku_data[0][bnum]}}">
	  </label>
	  <div class="medium-6 columns">
	  </div>
	</div>
      </div>
      % end

      <div class="row">
	<div class="medium-6 columns">
	  % if sku_data[0]["main_image"]:
	  <img
	    src="/uploaded_files/images/{{sku_data[0]['main_image']}}"
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

      % for item in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]:
      % inum = "image_" + item
      <div class="row">
	<div class="medium-6 columns">
	  % if sku_data[0][inum]:
	  <img
	    src="/uploaded_files/images/{{sku_data[0][inum]}}"
	    width="100px;"/>
	  % else:
	  <p>no image</p>
	  % end
	  
	  <label>Image {{item.title()}}
	    <input type="file" name="image-{{item}}">
	  </label>
	  <div class="medium-6 columns">
	  </div>
	</div>
      </div>
      % end

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
<!-- JsBarcode -->
<!-- http://lindell.me/JsBarcode/ -->
<script src="https://cdn.jsdelivr.net/jsbarcode/3.3.7/JsBarcode.all.min.js"></script>  

<script>

  JsBarcode("#barcode", String({{sku_data[0][1]}}),{
  fontOptions: "bold",
  });

</script>
