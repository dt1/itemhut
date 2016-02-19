<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% if inv:
% include('global/header_inv.tpl')
% else:
% include('global/header.tpl')
%end

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% if inv:
% include('global/top_nav_inv.tpl')
% else:
% include('global/top_nav.tpl')
% end


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

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
		<th>Case Id</th>
		<th>Box Id</th>
		<th>Box Qty</th>
		<th>Piece Qty</th>
		<th>UPC</th>
		<th>SKU</th>
		<th>Product Name</th>
		<th>Total Pieces</th>
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
    </div>
  <!-- close wrapper, no more content after this -->
  </div>
</div>

<script>
$(document).ready( function () {
    $('#table_id').DataTable();
} );
</script>

% include('global/end_body.tpl')