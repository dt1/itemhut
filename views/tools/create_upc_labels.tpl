<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

<!doctype html>
<head>
  <meta http-equiv="Cache-control" content="no-cache">
  <meta http-equiv="Expires" content="-1">
  
  <link rel="stylesheet" type="text/css"  href="https://cdn.jsdelivr.net/foundation/6.2.1/foundation.min.css">
</head>

<body>
  <form id="mf">
    <label style="width:300px;">Top:
      <input type="text" id="ttl" width="100px;">
    </label>

    <label style="width:300px;">Code:
      <input type="text" id="code" width="100px;">
    </label>

    <label style="width:300px;">Qty:
      <input type="number" id="cnt" min="1">
    </label>

    <input class="button" type="submit" name="submit"
	   value="generate barcodes">
  </form>

  <form id="prn">
    <input class="button" type="submit" name="print-page"
	   value="print barcodes">
  </form>
  
  <div id="imgs">
  </div>

  <script src="https://cdn.jsdelivr.net/jsbarcode/3.3.7/JsBarcode.all.min.js"></script>  

  <script>

mf.addEventListener("submit", function(e) {
    e.preventDefault();

    var ttl = document.getElementById("ttl").value;
    var code = document.getElementById("code").value;
    var cnt = document.getElementById("cnt").value;
    var imgDiv = document.getElementById("imgs");
    var newImgClass = "barcode" + code;
    
    for (var i = 0; i < cnt; i++) {
	var newTitlePar = document.createElement("p");
	newTitlePar.setAttribute("style", "margin-bottom:0");
	var newImg = document.createElement("img");
	var br = document.createElement("br");
	
	newImg.className = newImgClass;
	
	newTitlePar.textContent = ttl;
	
	imgDiv.appendChild(newTitlePar);
	imgDiv.appendChild(newImg);
	imgDiv.appendChild(br);
	newTitlePar.style.textAlign = "center";
    }
    
    JsBarcode("." + newImgClass, code,{
	fontOptions: "bold",
    });

    var w = newImg.clientWidth;
    imgDiv.setAttribute("style","width:" + w + "px");

});

prn.addEventListener("submit", function(e) {
    e.preventDefault();
    mf.outerHTML = "";
    delete mf;

    prn.outerHTML = "";
    delete prn;

    window.print();
    location.reload(true);

});

</script>

</body>

</html>
