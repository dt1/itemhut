<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

<!doctype html>

<head>
  <meta http-equiv="Cache-control" content="no-cache">
  <meta http-equiv="Expires" content="-1">

  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/foundation/6.2.1/foundation.min.css">
  <style>
    div.barcode {
    margin-bottom: 15px;
    }
    p.top {
    margin-bottom:0;
    text-align:center;
    }
    #mf {
    margin-top: 35px;
    }
    
    #mf label {
    width: 300px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="row">
      <div class="large-12 columns">
        <form id="mf">
          <label>Top:
            <input type="text" id="ttl">
          </label>

          <label>Code:
            <input type="text" id="code">
          </label>

          <label>Qty:
            <input type="number" id="cnt" min="1">
          </label>

          <input class="button" type="submit" name="submit" value="generate barcodes">
        </form>

        <input id="prn" class="button" type="submit" name="print-page" value="print barcodes">

        <div id="imgs">
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/jsbarcode/3.3.7/JsBarcode.all.min.js"></script>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>

  <script>
$('#mf').submit(function (e) {
    e.preventDefault();

    var cnt = $('#cnt').val();
    var code = $('#code').val();
    var ttl = $('#ttl').val();
    
    if(cnt && code && ttl) { //hacky form validation to ensure we have values for everything
	
	var newImgClass = 'barcode' + code.replace(/\s+/g, ''); //remove spaces from code input so it doesn't break as a CSS class

	for (var i = 0; i < cnt; i++) {
	    var newBarcode = $('<div />', {class: 'barcode'}); //create a wrapper div for each barcode
	    $(newBarcode).append($('<p />', {text: ttl, class: 'top'})); //create the "top" paragraph element
	    $(newBarcode).append($('<canvas />', {class: newImgClass})); //create the image
	    $('#imgs').append(newBarcode); //append the new barcode div to #imgs
	}

	JsBarcode("." + newImgClass, code, {
	    fontOptions: "bold",
	});
	
	$('#imgs').width($('.' + newImgClass).width());  
    }
    
});

$('#prn').on('click', function () { //remove the form since there isn't any way for it to be submitted without being clicked.
    $('#mf, #prn').remove();
    window.print();
    location.reload(true);
});        
</script>

</body>

</html>
</html>
