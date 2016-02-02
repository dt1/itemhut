% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   <h4 color = >{{warehouse_name}}</h4>
	   <p>Information</p>
	   </div>
	   
      	   <div class="medium-10 columns">
	   	<p>{{wh_info[0][0]}}</p>
	   	<p>{{wh_info[0][1]}}</p>
	   	<p>{{wh_info[0][2]}} {{wh_info[0][3]}}, {{wh_info[0][4]}}</p>
	   	<p>warehouse type: {{wh_info[0][5]}}</p>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')