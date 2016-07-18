<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
  </div>

  <div class="medium-10 columns">
    <h4>Update {{user_info[0][0]}}</h4>
    % if user_error and new_user:
    <p>{{new_user}} already exists</p>
    % elif new_user:
    <p>Added {{new_user}}</p>
    % end

    <form action="/admin/update-user-{{user_info[0][0]}}"
	  method="POST">

      <div class="row">
	<div class="medium-2 columns">
	  <label>username:
	    <input type="text" name="user-name" required="required"
		   value="{{user_info[0][0]}}">
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-4 columns">
	  <label>Name:
	    <input type="text" name="real-name"
		   % if user_info[0][1]:
		   value="{{user_info[0][1]}}"
		   %end
		   >
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-2 columns">
	  <label>role
	    <select name="urole">
	      % for i in role_types:
	      <option value="{{i[0]}}">{{i[0]}}</option>
	      % end
	    </select>
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>

      <div class="row">
	<div class="medium-2 columns">
	  <label>type
	    <select name="utype">
	      <option value="">-</option>
	      % for i in user_types:
	      <option value="{{i[0]}}">{{i[0]}}</option>
	      % end
	    </select>
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>


      <div class="row">
	<div class="medium-2 columns">
	  <input type="submit" class="button" value="Update User"
		 name="update-user">
	</div>
      </div>

    </form>
  </div>
</div>
