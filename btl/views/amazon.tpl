% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>
      <div class="expanded row">
      	   <div class="medium-2 columns">
	       <h4>Amazon</h4>
	   	<ul class="vertical menu">
			<li>
				<a href = "/amazon">All</a>
			</li>
			% for i in reg:
			<li>
				<a href = "/channels/amazon/{{i[1]}}">{{i[2]}}</a>
			</li>
			% end			
			
		</ul>
	   </div>
      	   <div class="medium-10 columns">
		 
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')