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
			<li><a href = "/products/amazon/{{section}}/new-item">New Item</a></li>
		</ul>
	   </div>
	   
      	   <div class="medium-10 columns">
	     <div class = "row">
	   <form action="/add-amazon-item" method="post">
	     % for k, v in fdict.items():
	     <div class = "medium-4 columns">
	     <label>{{v["cname"]}}
	     % if "valid_array" in v:
	     	     <select>
	     	     %for item in v["valid_array"]:
		     <option value="{{item[0]}}">{{item[0]}}</option>
	     	     % end
  	     	     </select>
	     % else:
		<input type = "text">
	     % end
	     </label>
	     </div>
	     % end
	     <div class = "large-12 columns">
	   <input value="Add product" type="submit" class="button" />
	   </div>
	   </form>
	     </div>

	   </div>      
      </div>

    </div>



  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')