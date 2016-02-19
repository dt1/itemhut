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
      	   <h4>Warehouses</h4>
      	   <div class="medium-2 columns">
	   	<ul class="vertical menu">
		% for i in wh:
		<li><a href = "/warehouses/{{i[0]}}">{{i[1]}}</a></li>
		% end
		</ul>

		<h4>Base Management</h4>
	   	<ul class="vertical menu">
		    <li><a href = "/warehouses/cases">Cases & Boxes</a></li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	         <p>stuff here</p>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')