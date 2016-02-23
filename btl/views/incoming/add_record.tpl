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
	   	<h4>Incoming</h4>
	   % include('incoming/side_nav_menu')
	   </div>
      	   <div class="medium-10 columns">
	         <h5>Add Record</h5>
		 % if invoice_added:
		 <p>{{invoice_added}} added.</p>
		 % end
		 <form action="/incoming/add-record" method="POST">

		 <div class="row">
		 <div class="medium-3 columns">
		       <label>Invoice
		       <input type="text" name="invoice" required="required">
		       </label>
		 </div>
		 </div>

		 <div class="row">
		 <div class="medium-3 columns">
		       <label>Vendor ID
		       <input type="text" name="vendor-id" required="required">
		       </label>
		 </div>
		 </div>

		 <div class="row">
		 <div class="medium-3 columns">
		       <label>Order Date
		       <input type="date" name="order-date" required="required">
		       </label>
		 </div>
		 </div>

		 <div class="row">
		 <div class="medium-3 columns">
		       <label>ETA
		       <input type="date" name="eta">
		       </label>
		 </div>
		 </div>

		 <div class="row">
		 <div class="medium-3 columns">
		       <label>Invoice File
		       <input type="file" name="invoice-file">
		       </label>
		 </div>
		 </div>

		 <div class="row">
		 <div class="medium-3 columns">
		 <input type="submit" name="add-record"
		 value="Add Record" class="button">
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