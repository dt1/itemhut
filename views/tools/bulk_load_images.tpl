<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

<!doctype html>

<head>
  <meta http-equiv="Cache-control" content="no-cache">
  <meta http-equiv="Expires" content="-1">
</head>

<body>
  <form action="/tools/bulk-load-images"
	method="POST" enctype="multipart/form-data">
    <input type="file" name="imgs" multiple="multiple"/>
    <br>
    <br>
    <input type="submit" class="button" value="Upload Images"
	   name="upload-images">
  </form>
  
</body>
</html>
