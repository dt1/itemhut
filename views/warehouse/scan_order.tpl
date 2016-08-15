<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Scan Order</h4>
  </div>
  
  <div class="medium-10 columns">
    % if err:
    <p>{{err}}</p>
    % end
    <h5>Internal Order Id: {{oid}}</h5>
    <h5>Order Id: {{order[0][1]}}</h5>
    <h5>Ship By: {{order[0][3]}}</h5>

    <h5>Items</h5>
    <form method="POST"action="">
    % for i in order[0][2]:
    <p>{{i}}</p>
    % end
    <input class="button" type="submit" value="OK" />
      
    </form>
  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>

<style>

  .dataTables_length{
  width: 5em;
  }

  .dataTables_filter{
  width:15em;
  margin-left:-25em;
  }

  .dataTables_paginate{
  margin-left:-20em;
  }
</style>
