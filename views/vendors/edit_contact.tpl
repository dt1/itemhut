<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    % include('vendors/vendor_side_nav.tpl', vendor_info = vendor_info)
  </div>

  <div class="medium-10 columns">
    <div class="row">
      <div class="medium-4 columns">
	<h4>Edit Contact</h4>
	<form action="/vendors/{{vid}}/contacts/edit-contact-{{contact_info[0][0]}}" method="POST">
	  <label>Name
	    <input type="text" name="name" required="required"
		   value="{{contact_info[0][1]}}">
	  </label>

	  <label>Title
	    <input type="text" name="title"
		   value="{{contact_info[0][2]}}">
	  </label>

	  <label>Phone
	    <input type="text" name="phone"
		   value="{{contact_info[0][3]}}">
	  </label>

	  <label>Phone 2
	    <input type="text" name="alt-phone"
		   value="{{contact_info[0][4]}}">
	  </label>

	  <label>email
	    <input type="text" name="email"
		   value="{{contact_info[0][5]}}">
	  </label>
	  <input type="submit" class="button" name="edit-contact"
		 value="Update Contact">
	  <form>
      </div>
    </div>
  </div>
</div>
