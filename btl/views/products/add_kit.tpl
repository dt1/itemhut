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
			Add Kit
			</li>
		</ul>
	   </div>

      	   <div class="medium-10 columns">

	   % if new_sku:
	   	   <p>New Master Sku Added: {{new_sku}}
	   % end

	   % if err:
	     <p>{{err}}</p>
	   % end
	   
	   <form action="/products/add-kit" method="POST">
	   <div class="row">
	   <div class="medium-3 columns">
	   <label> Master SKU
		<input type="text" name="master-sku" required="required">
	   </label>

	   <div class="medium-9 columns">
	   </div>
	   </div>
	   </div>

	   % for i in range(1, 11):
	   <div class="row">
	   <div class="medium-3 columns">
	   <label>SKU
		<select name="kit-name-{{i}}">
		<option value=""></option>
		% for item in sku_upc:
		<option value="{{item[0]}}">{{item[0]}}</option>
           	% end
		</select>
	   </label>
	   </div>
	   <div class="medium-3 columns">
	   <label>Qty
		<input type="number" min="1" name="kit-amt-{{i}}">
	   </label>
	   </div>
	   <div class="medium-6 columns">
	   </div>

	   </div>
	   % end

	    <input type="submit" class="button" value="Add Kit" name="add-kit">
	    </form>


	   </div>
      </div>

    </div>


  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')