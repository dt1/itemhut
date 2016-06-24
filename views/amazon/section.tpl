<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<h4 style = "color: #004291;">{{amz_header}}</h4>
	   	<ul class="vertical menu">
			<li><a href = "/channels/amazon/{{section}}/new-item">New Item</a></li>
		</ul>
	   </div>
      	   <div class="medium-10 columns">
	   <table>
		<tr>
		<th>Item Sku</th>
		<th>Item Name</th>
		<th>Quantity</th>
		<th>Listed Price</th>	
		</tr>
	   </table>
	   	% for f in fields:
	         <label>{{f[1]}}</label>
		 <input></input>
		% end

	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')