<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4 color = >{{wh_info[0][1]}}</h4>
    % include('warehouse/side_nav_3pl_menu.tpl', wh_id = wh_info[0][0])
  </div>
  <div class="medium-10 columns">
    <h4>Update Inventory</h4>
    <p><b>SKU: </b>{{sku_count[0][0]}} ({{sku_count[0][2]}})</p>
    <form action="/warehouses/{{wh_info[0][0]}}/update-running-inventory-{{sku_count[0][0]}}" method="POST">
      <div class="row">
	<div class="medium-3 columns">
	  <input type="number" name="qty" min="1">
	  <input type="submit" class="button" name="update-qty"
		 value="Update QTY">
	</div>
      </div>
  </div>
</div>
