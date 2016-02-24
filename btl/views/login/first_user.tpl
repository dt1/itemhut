<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->


<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>
    % if e:
    {{e}}
    % end
      <div class="expanded row">
      <h4>Welcome to Item Hut</h4>
      <p><b>This is the first user for this account.</b></p>

      <form action="/initialize" method="POST">
      <label>username
      <br>
      <input type="text" name="username">
      </label>
      <br>
      <label>password
      <br>
      <input type="password" name="password">
      <br>
      </label>
      <label>retype password
      <br>
      <input type="password" name="password2">
      <br>
      </label>
      <input type="submit" name="create-user" value="Create User">
      </form>
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')