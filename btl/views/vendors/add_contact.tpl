<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    % include('vendors/vendor_side_nav.tpl', vendor_info = vendor_info)
  </div>

  <div class="medium-10 columns">
    % if contact_name:
    <p>{{contact_name}} added</p>
    % end
    <div class="row">
      <div class="medium-4 columns">
	<form action="/vendors/{{vid}}/contacts/add-contact" method="POST">
	  <label>Name
	    <input type="text" name="name" required="required">
	  </label>

	  <label>Title
	    <input type="text" name="title">
	  </label>

	  <label>Phone
	    <input type="text" name="phone">
	  </label>

	  <label>Phone 2
	    <input type="text" name="alt-phone">
	  </label>

	  <label>email
	    <input type="text" name="email">
	  </label>
	  <input type="submit" class="button" name="add-contact" value="Add Contact">
	  <form>
      </div>
    </div>
  </div>

</div>
