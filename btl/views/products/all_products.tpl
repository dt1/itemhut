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
			<a href = "/products/add-product">Add Product</a>
			</li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <table id="table_id" class="display">
	   <thead>
		<tr>
		<th>SKU</th>
		<th>UPC</th>
		<th>SKU Type</th>
		<th>Product Name</th>
		</tr>
	   </thead>
	   <tbody>
	   % for i in sku_upc:
		<tr class="table-anchor" onclick="location.href='#'">
		<td>{{i[0]}}</td>
		<td>{{i[1]}}</td>
		<td>{{i[2]}}</td>
		<td>{{i[3]}}</td>
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