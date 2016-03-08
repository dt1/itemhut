<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4 color = >{{wh_info[0][1]}}</h4>
    <p>Add Product</p>
    % include('warehouse/side_nav_3pl_menu.tpl', wh_id = wh_info[0][0])

  </div>

  <div class="medium-10 columns">
    % if upc:
    <p>Added {{upc}}</p>
    % end
    <div class="row">
      <div class="medium-3 columns">
	<form action="/warehouses/{{wh_info[0][0]}}/add-product"
	      method="POST">

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
</div>
