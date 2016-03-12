<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
  </div>

  <div class="medium-10 columns">
    <h4>Change Password ({{uid}})</h4>

    % if err:
    <p>{{err}}</p>
    % end
    
    <form action="/admin/update-user-password-{{uid}}"
	  method="POST">

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
	  <label>password:
	    <input type="password" name="password2"
		   required="required">
	  </label>
	</div>
	<div class="medium-10 columns">
	</div>
      </div>
      
      <div class="row">
	<div class="medium-2 columns">
	  <input type="submit" class="button" value="Submit"
		 name="update-password">
	</div>
      </div>

    </form>
  </div>
</div>
