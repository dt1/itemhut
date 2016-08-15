<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    % include('companies/companies_side_nav', cinfo = cinfo)
  </div>

  <div class="medium-10 columns">
    <h4>Edit Contact</h4>
    <div class="row">
      <form
	 action="/companies/{{cinfo[0]}}/contacts/edit-contact-{{contact_info[0]}}"
	 method="POST">
	<div class="medium-3 columns">
	  <label>Name
	    <input type="text" name="contact-name"
		   value="{{contact_info[1]}}" required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	  <label>Position
	    <input type="text" name="position"
		   value="{{contact_info[2]}}" required="required">
	  </label>
	</div>
	<div class="medium-3 columns">
	</div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Phone 1
	  <input type="text" name="phone-one"
		 value="{{contact_info[3]}}">
	</label>
      </div>
      <div class="medium-3 columns">
	<label>Phone 2
	  <input type="text" name="phone-two"
		 value="{{contact_info[4]}}">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <div class="medium-3 columns">
	<label>Email
	  <input type="email" name="email"
		 value="{{contact_info[5]}}">
	</label>
      </div>
      <div class="medium-3 columns">
      </div>
      <div class="medium-3 columns">
      </div>
    </div>

    <div class="row">
      <input type="submit" class="button" name="edit-contact"
	     value="Edit Contact">
    </div>
    </form>
  </div>
</div>
