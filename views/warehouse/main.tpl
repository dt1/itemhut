<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Warehouses</h4>
    <ul class="vertical menu">
      % for i in wh:
      % if i[2] == 'B&M':
      <li><a href = "/warehouses/{{i[0]}}">{{i[1]}}</a></li>
      % end
      % end
    </ul>

    <h4>3PL</h4>
    <ul class="vertical menu">
      % for i in wh:
      % if i[2] == '3PL':
      <li><a href = "/warehouses/{{i[0]}}">{{i[1]}}</a></li>
      % end
      % end
    </ul>
  </div>

  <div class="medium-10 columns">
    <p>stuff here</p>
  </div>
</div>
