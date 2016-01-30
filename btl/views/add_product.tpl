% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<ul class="vertical menu">
			<li>
			Add Product
			</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <form>

	   <div class = "row">
	   <div class = "medium-2 columns">
	   <label>Sku
	   	  <input type = "text">
	   </label>
	   </div>		
	   </div>		

	   <div class = "row">
	   <div class = "medium-2 columns">
	   <label>UPC
	   	  <input type = "text">
	   </label>
	   </div>		
	   </div>

	   <div class = "row">
	   <div class = "medium-2 columns">
	   <label>SKU Type
	   <select>
	   % for item in sku_types:
	     <option>{{item[0]}}</option>
	   % end
	   </select>
	   </label>
	   </div>		
	   </div>

	   <div class = "row">
	   <div class = "medium-2 columns">
	   <label>Product Name
	   	  <input type = "text">
	   </label>
	   </div>		
	   </div>


	   <div class = "row">
	   <div class = "medium-2 columns">
	   <input type = "submit" class = "button" value = "Add Product">
	   </div>		
	   </div>

	   </form>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')