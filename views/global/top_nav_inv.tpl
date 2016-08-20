<!-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/. -->

% from bottle import *
% from beaker.middleware import SessionMiddleware
% request.session = request.environ['beaker.session']
% role = request.session["user_role"]

<div id="widemenu" class="top-bar">
  <div class="top-bar-left">
    <ul class="menu">
      <li class="menu-text">XYZ Company</li>
      <li>
        <a href="/">Home</a>
      </li>
      % if role in ["admin", "original admin", "products", "user"]:
      <li>
        <a href="/products">Products</a>
      </li>
      % end
      % if role in ["admin", "original admin", "incoming", "user"]:
      <li>
        <a href="/incoming">Incoming</a>
      </li>
      % end
      % if role in ["admin", "original admin", "warehouses", "user"]:
      <li>
        <a href="/warehouses">Warehouses</a>
      </li>
      % end
      % if role in ["admin", "original admin", "vendors", "user"]:
      <li>
        <a href="/vendors">Vendors</a>
      </li>
      % end
      % if role in ["admin", "original admin", "orders", "user"]:
      <li>
        <a href="/orders">Orders</a>
      </li>
      % end
      % if role in ["admin", "original admin", "customers", "user"]:
      <li>
        <a href="/companies">Customers</a>
      </li>
      % end
      <li>
        <a href="/tools">Tools</a>
      </li>
      % if role in ["admin", "original admin", "user"]:
      <li>
        <a href="/admin">Admin</a>
      </li>
      % end
    </ul>
  </div>
  <div class="top-bar-right">
    <ul class="menu">
      <!--          <li><input type="search" placeholder="Search"></li>
		    <li><button class="button">Search</button></li>
		    -->	 
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

