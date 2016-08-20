<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

<!doctype html>

<head>
  <meta http-equiv="Cache-control" content="no-cache">
  <meta http-equiv="Expires" content="-1">
</head>

<body>
    % for i in imgs:
  <form action="/tools/image-library"
	method="POST" enctype="multipart/form-data">
    <img src="/uploaded_files/images/{{i['image']}}">
    <input type="hidden" name="img-del" value="{{i['image']}}">
    <p>{{i["image"].rsplit("/")[-1]}}</p>
    <input type="submit" class="button" name="delete-image"
	   value="Delete Image"/>
    <br>
    <p>replace image:</p>
    <input type="file" class="button" name="new-img">
    <br>
    <input type="submit" class="button" value="Replace Image"
	   name="replace-image">
    <br>
    <br>
  </form>
  % end
  
</body>
</html>
