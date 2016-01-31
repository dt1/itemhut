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
	   <p>Pallet Locations</p>
	   </div>
	   
      	   <div class="medium-10 columns">
	   <table>
		<tr>
		<th>pallet_location</th>
		<th>pallet #</th>
		</tr>
		% for item in pallet_location_list:
		<tr>
		<td>{{item[1]}}</td>
		% if item[2]:
		<td><a href = "#">{{item[2]}}</a></td>
		% else:
		<td>Empty</td>
		% end
		</tr>
		% end
	   </table>
	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')