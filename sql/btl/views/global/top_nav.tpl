    <div id="widemenu" class="top-bar">
      <div class="top-bar-left">
        <ul class="menu">
          <li class="menu-text">XYZ Company</li>
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a href="/products">Products</a>
          </li>
          <li>
            <a href="/channels">Channels</a>
          </li>
          <li>
            <a href="/warehouses">Warehouses</a>
          </li>
          <li>
            <a href="/orders">Orders</a>
          </li>
          <li>
            <a href="/emails">Emails</a>
          </li>
          <li>
            <a href="/customers">Customers</a>
          </li>
          <li>
            <a href="/analytics">Analytics</a>
          </li>
          <li>
            <a href="/admin">Admin</a>
          </li>
      </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button class="button">Search</button></li>
        </ul>
      </div>
    </div>
    <script>
//Bread crumb script - Kevin Lynn Brown
//Duplicate directory names bug fix by JavaScriptKit.com
//Visit JavaScript Kit (http://javascriptkit.com) for script

var path = "";
var href = document.location.href;
var s = href.split("/");
for (var i=2;i<(s.length-1);i++) {
path+="<A HREF=\""+href.substring(0,href.indexOf("/"+s[i])+s[i].length+1)+"\">"+s[i]+"</A> / ";
}
i=s.length-1;
path+="<A HREF=\""+href.substring(0,href.indexOf(s[i])+s[i].length)+"\">"+s[i]+"</A>";
var url = window.location.protocol + "//" + path;
document.writeln(url);
</script>
