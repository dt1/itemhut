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
	   	<h4>Cases & Boxes</h4>
	   	<ul class="vertical menu">
		    <li>New Configuration</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   % if err:
	     <p>{{err}}</p>
	   % end
	   <form action="/warehouses/cases/new-config", method="POST">
	   <div class="row">
	   <div class="medium-3 columns">
	   <label>UPC
		 <select name="upc">
		 % for i in upc_list:
		 <option value="{{i}}">{{i}}</option>
		 % end
		 </select>
	   </label>
	   </div>
 
	   <div class="medium-3 columns">
	   	 <label>QTY in Box
		 <input name="box-qty" type="number" min="1" required="required">
		 </label>
	   </div>

	   <div class="medium-3 columns">
	   	 <label>Boxes in Case
		 <input name="case-qty" type="number" min="1" required="required">
		 </label>
	   </div>
	   <div class="medium-3 columns">
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-3 columns">
	   	<input type="submit" name="add-config" class="button" value="Add Config">
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