<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Add Company</h4>
  </div>

  <div class="medium-10 columns">
    <h4>Add Company</h4>

    <div class="row">
      <form action="/companies/add-company" method="POST">
	<div class="medium-3 columns">
	  <label>Company ID
	    <input type="text" name="company-uid"
		   required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	  <label>Company Name
	    <input type="text" name="company-name"
		   required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	</div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Phone 1
	  <input type="text" name="phone-one">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Phone 2
	  <input type="text" name="phone-two">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Fax
	  <input type="text" name="fax">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>email
	  <input type="email" name="email">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Street
	  <input type="text" name="street">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>City
	  <input type="text" name="city">
	</label>
      </div>
      <div class="medium-6 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>State
	  <input type="text" name="state">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Zip
	  <input type="text" name="zip">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Country
	  <input type="text" name="country">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <input type="submit" class="button" name="add-company"
	     value="Add Company">
    </div>
  </form>
  </div>
</div>
