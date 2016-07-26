<!doctype html>

<head>

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
	   value="generate barcode">
  </form>

  <div id="imgs">
  </div>

  <script src="https://cdn.jsdelivr.net/jsbarcode/3.3.7/JsBarcode.all.min.js"></script>  

  <script>


    mf = document.getElementById("mf")
    
    mf.addEventListener("submit", function(e) {

    var ttl = document.getElementById("ttl").value;
    var code = document.getElementById("code").value;
    var cnt = document.getElementById("cnt").value;
    var imgDiv = document.getElementById("imgs");
    var newImgClass = "barcode" + code;
    
    for (var i = 0; i < cnt; i++) {
			var newTitlePar = document.createElement("p");
			var newImg = document.createElement("img");
			var br = document.createElement("br");
			newImg.className = newImgClass;
			newTitlePar.textContent = ttl;
			imgDiv.appendChild(newTitlePar);
			imgDiv.appendChild(newImg);
			imgDiv.appendChild(br);
			}
			
			JsBarcode("." + newImgClass, code,{
			fontOptions: "bold"
			});

			//mf.outerHTML = "";
			//delete mf
			e.preventDefault();
			});
			
			</script>

</body>

</html>
