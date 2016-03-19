<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Order Scan Out</h4>
  </div>
  
  <div class="medium-10 columns">
    % if err:
    <p>{{err}}</p>
    % end
    <form action="/warehouses/cases/new-config", method="POST">
      {{orders}}
    </form>
  </div>
</div>
