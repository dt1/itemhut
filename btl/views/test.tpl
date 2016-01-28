% include('header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('top_bar.tpl')
% include('top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<ul class="vertical menu">
			<li>menu</li>
			<li>menu</li>
			<li>menu</li>
			<li>menu</li>
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

% include('end_body.tpl')