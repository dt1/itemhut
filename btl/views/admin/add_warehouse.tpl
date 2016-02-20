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
	   </div>

      	   <div class="medium-10 columns">

	   <h4>Add Warehouse</h4>
	   % if new_warehouse:
	   <p>Added {{new_warehouse}}</p>
	   % end
	   <form action="/products/add-product" method="POST">

	   <div class="row">
	   <div class="medium-2 columns">
	   <label>Warehouse ID
	   	  <input type="text" name="warehouse-id" required="required">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>Warehouse Name
	   	  <input type="text" name="warehouse-name">
	   </label>
	   </div>
	   <div class="medium-8 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-4 columns">
	   <label>Street Address
	   <input type="text" name="street">
	   </select>
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>State
	   	  <input type="text" name="state">
	   </label>
	   </div>

	   <div class="medium-6 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-2 columns">
	   <label>Zip Code
		<input type="text" name="zip-code">
           </label>
	   </div>
	   <div class="medium-2 columns">
	   <label>Country
		<input type="text" name="country">
	   </label>
	   </div>
	   <div class="medium-2 columns">
	   <label>Warehouse Type
		<input type="text" name="wh-type">
	   </label>
 	   </div>
	   <div class="medium-6 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-2 columns">
	   <input type="submit" class="button" value="Add Warehouse"
	   name="add-warehouse">
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