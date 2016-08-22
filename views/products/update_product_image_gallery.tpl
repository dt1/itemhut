<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% rebase('global/base.tpl')

<div class="expanded row">
  <div class="medium-2 columns">
    <p>Update <b>{{sku}}</b></p>
    <p>Update <b>{{img.replace("-", " ").title()}}</b></p>
  </div>

  <div class="medium-10 columns">
    <form action="/products/update-product-{{sku}}/gallery-{{img}}"
	  method="POST" enctype="multipart/form-data">

      % for i in imgs:
      <span><b>{{i["image"].rsplit("/")[1]}}</b></span>
      <input type="radio" name="new-image" value="{{i['image']}}" />
      <img src="/uploaded_files/images/{{i['image']}}" alt="" />
      <br>
      <hr>
      % end
      <div class="row">
	<div class="medium-6 columns">

	  <div class="row">
	    <div class="medium-2 columns">
	      <input type="submit" class="button" value="Update Image" name="update-image">
	    </div>
	  </div>
	</div>
      </div>
    </form>
  </div>
</div>
