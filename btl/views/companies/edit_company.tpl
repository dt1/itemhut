<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    % include('companies/companies_side_nav')
  </div>
  
  <div class="medium-10 columns">
    <h4>Edit Company</h4>
    <div class="row">
      <form action="/companies/edit-company-{{cinfo[0]}}"
	    method="POST">
	<div class="medium-3 columns">
	  <label>Company ID
	    <input type="text" name="company-uid"
		   value="{{cinfo[1]}}" required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	  <label>Company Name
	    <input type="text" name="company-name"
		   value="{{cinfo[2]}}" required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	</div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Phone 1
	  <input type="text" name="phone-one"
		 value="{{cinfo[3]}}">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Phone 2
	  <input type="text" name="phone-two"
		 value="{{cinfo[4]}}">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Fax
	  <input type="text" name="fax"
		 value="{{cinfo[5]}}">
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
	  <input type="email" name="email"
		 value="{{cinfo[6]}}">
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
	  <input type="text" name="street"
		 value="{{cinfo[7]}}">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>State
	  <input type="text" name="state"
		 value="{{cinfo[8]}}">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Zip
	  <input type="text" name="zip"
		 value="{{cinfo[9]}}">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Country
	  <input type="text" name="country"
		 value="{{cinfo[10]}}">
	</label>
      </div>
    </div>

    <div class="row">
      <input type="submit" class="button" name="edit-company"
	     value="Edit Company">
    </div>
  </form>
  </div>
</div>
