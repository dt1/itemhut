<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
  </div>

  <div class="medium-10 columns">

    <h4>Add User</h4>
    % if user_error and new_user:
    <p>{{new_user}} already exists</p>
    % elif new_user:
    <p>Added {{new_user}}</p>
    % end

    <form action="/admin/add-user" method="POST">

      <div class="row">
	<div class="medium-2 columns">
	  <label>username:
	    <input type="text" name="user-name" required="required">
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-2 columns">
	  <label>password:
	    <input type="password" name="password" required="required">
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-2 columns">
	  <label>role
	    <select name="role">
	      % for i in role_types:
	      <option value="{{i}}">{{i}}</option>
	      % end
	    </select>
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>
      

      <div class="row">
	<div class="medium-2 columns">
	  <input type="submit" class="button" value="Add User"
		 name="add-user">
	</div>
      </div>

    </form>
  </div>
</div>
