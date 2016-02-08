% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">	   
      	   <div class="large-12 columns">
	   	<h5>
		    <a href="/" style = "color: #004291;">New Orders</a>
		</h5>
		<span>300 new orders</span>
		<br>
		<br>
	   	<h5>
		    <a href="/" style = "color: #004291;">New Emails</a>
		</h5>
		<span>300 new emails</span>

	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')