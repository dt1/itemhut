<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% include('global/header_inv.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')

% include('global/top_nav_inv.tpl')

    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<h4>Add Contact</h4>
	   	<ul class="vertical menu">
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <form action="/vendors/{{vid}}/add-contact" method="POST">
	   <form>

	   </div>

    </div>

  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')