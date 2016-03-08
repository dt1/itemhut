<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>{{wh_info[0][1]}}</h4>
    % include('warehouse/side_nav_3pl_menu.tpl', wh_id = wh_info[0][0])
  </div>

  <div class="medium-10 columns">
    <p>{{wh_info[0][0]}}</p>
    <p>{{wh_info[0][1]}}</p>
    <p>{{wh_info[0][2]}} {{wh_info[0][3]}}, {{wh_info[0][4]}}</p>
    <p>warehouse type: {{wh_info[0][5]}}</p>
  </div>
</div>
