<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Add Order</h4>
    % include('orders/orders_side_nav.tpl')
  </div>

  <div class="medium-10 columns">
    % if clist[0][1]:
    <h4>Companies (order: {{clist[0][2]}})</h4>
    % else:
    <h4>Companies (order: {{clist[0][1]}})</h4>
    % end
    <table>
      <thead>
	% for h in ["Company Name", "Deliver By", "Ship By",
	% "", ""]:
	<th>{{h}}</th>
	% end
      </thead>
      <tbody>
	% for i in clist:
	<tr>
	  <td>{{i[4]}}</td>
	  <td>{{i[5]}}</td>
	  <td>{{i[6]}}</td>
	  <td><a>Edit / View</a></td>
	  <td><a href="/orders/add-order/order{{i[1]}}/company{{i[0]}}-add-products">Add Products</a></td>
	  <td><a href="/orders/add-order/order{{i[1]}}/company{{i[0]}}-add-files">Add Files</a></td>
	</tr>
	% end
      </tbody>
    </table>
  </div>      
</div>
