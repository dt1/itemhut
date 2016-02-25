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
	   <h4>Add Kit</h4>
	   	<ul class="vertical menu">
		</ul>
		% include('products/product_side_nav')
	   </div>

      	   <div class="medium-10 columns">

	   % if new_sku:
	   	   <p>New Master Sku Added: {{new_sku}}
	   % end

	   % if err:
	     <p>{{err}}</p>
	   % end
	   
	   <form action="/products/add-kit" method="POST" id="input-form">
	   <div class="row">
	   <div class="medium-3 columns">
	   <label> Master SKU
		<input type="text" name="master-sku" required="required">
	   </label>

	   <div class="medium-9 columns">
	   </div>
	   </div>
	   </div>

	   % for i in range(1, 11):
	   <div class="row">
	   <div class="medium-3 columns" style="margin-top:2em;">
	   <label>SKU
	   <input list="kits" name="kit-name-{{i}}"></label>
	   <datalist id="kits">
		<option value=""></option>
		% for item in sku_upc:
		<option value="{{item[0]}}">
           	% end
		</datalist>
	   </div>
	   <div class="medium-3 columns">
	   <label>Qty
		<input type="number" min="1" name="kit-amt-{{i}}">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>

	   </div>
	   % end

	    <input type="submit" class="button" value="Add Kit" name="add-kit">
	    </form>


	   </div>
      </div>

    </div>


  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')