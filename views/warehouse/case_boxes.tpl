<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <h4>Cases & Boxes</h4>
    <ul class="vertical menu">
      <li><a href = "/warehouses/cases/new-config">New Configuration</a></li>
    </ul>
  </div>
  
  <div class="medium-10 columns">
    <table id="table_id" class="display">
      <thead>
	<tr>
	  % for h in ["Case Id", "Box Id", "Box Qty", "Piece Qty",
	  % "UPC", "SKU", "Product Name",
	  % "Total Pieces"]:
	  <th>{{h}}</th>
	  % end
	</tr>
      </thead>
      <tbody>
	% for item in case_boxes:
	<tr>
	  <td>{{item[0]}}</td>
	  <td>{{item[1]}}</td>
	  <td>{{item[2]}}</td>
	  <td>{{item[3]}}</td>
	  <td>{{item[4]}}</td>
	  <td>{{item[5]}}</td>
	  % if item[6]:
	  <td>{{item[6]}}</td>
	  % else:
	  <td></td>
	  % end
	  <td>{{item[7]}}</td>
	</tr>
	% end
      </tbody>
    </table>

  </div>
</div>

<script>
  $(document).ready( function () {
  $('#table_id').DataTable();
  } );
</script>
