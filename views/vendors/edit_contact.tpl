<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

% contact_info = contact_info[0]

<div class="expanded row">
  <div class="medium-2 columns">
    % include('vendors/vendor_side_nav.tpl', vendor_info = vendor_info)
  </div>

  <div class="medium-10 columns">
    <div class="row">
      <div class="medium-4 columns">
	<h4>Edit Contact</h4>
	<form action="/vendors/{{vid}}/contacts/edit-contact-{{contact_info['contact_id']}}" method="POST">
	  <label>Name
	    <input type="text" name="name" required="required"
		   value="{{contact_info['name']}}">
	  </label>

	  <label>Title
	    <input type="text" name="title"
		   value="{{contact_info['title']}}">
	  </label>

	  <label>Phone
	    <input type="text" name="phone"
		   value="{{contact_info['phone']}}">
	  </label>

	  <label>Phone 2
	    <input type="text" name="alt-phone"
		   value="{{contact_info['alt_phone']}}">
	  </label>

	  <label>email
	    <input type="text" name="email"
		   value="{{contact_info['email']}}">
	  </label>
	  <input type="submit" class="button" name="edit-contact"
		 value="Update Contact">
	  <form>
      </div>
    </div>
  </div>
</div>
