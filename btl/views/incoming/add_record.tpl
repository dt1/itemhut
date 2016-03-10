<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

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

    <form action="/incoming/add-record" method="POST"
	  enctype="multipart/form-data">

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
