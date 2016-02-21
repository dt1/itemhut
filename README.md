#Item Hut

Item Hut is a free and open-source marketing, ERP, CRM, and channel-management tool mainly focusing on B2B.

###Web Site

www.itemhut.com

###Current Status
Under active development. To keep things progressing along smoothly, Item Hut is going to begin as an inventory system.

###Why?

In various professional roles, I have discovered that the marketing, ERP, CRM, and channel-management tools (all closed source) have never met the needs and expectations of the companies I have worked for. In response to these short-comings, I have always developed in-house databases and programs to further manage the complexity of the jobs I had to do.

This program can serve as a cheat-sheet for those who find themselves in my position and don't know where to start, or it can serve as a foundation for those who want to build their own solutions. This program is fundamentally different because it is created by someone who has found himself in the mud.

####Inventory System Setup
PostgreSQL 9.5

Python packages:
* Python3
* Python Bottle
* bcrypt
* hmac
* Psycopg2

clone to /itemhut:
```bash
$ git clone https://github.com/dt1/item-hut.git
```

setup the database
```bash
$su - postgres
$createdb itemhut
$psql -d itemhut -U postgres -f /itemhut/build_database/products/products.sql 
$psql -d itemhut -U postgres -f /itemhut/build_database/warehouse/warhouse.sql 
$psql -d itemhut -U postgres -f /itemhut/build_database/vendors/vendors.sql
```

run bottle:
```
$ python3 /itemhut/btl/inventory.py
```

open localhost:8082

####Full System Setup
(same as Inventory System Setup)

Python packages:
* BeutifulSoup2
* pandas

Python eBay SDK:
https://github.com/timotheus/ebaysdk-python

setup the yaml files

By default, the eBay SDK does not function with Python3. On Fedora:

```bash
[your-editor] /usr/lib/python3.4/site-packages/ebaysdk-2.1.2-py3.4.egg/ebaysdk/response.py
line 65:
change:
if i is None or isinstance(i, str) or isinstance(i, unicode):
to:
if i is None or isinstance(i, str): #or isinstance(i, unicode):
```

(to be continued...)

###Expected Features
* B2B Customer Management
* Inventory Management
* Basic Warehouse Management
* Intensive marketing analysis
* "Feature Complete" Ebay and Amazon API integration.
* Flat File creation
* Excellent Documentation

####Permissions and Licensing

While I am unable to enforce this, I am a strong believer that a customer's data is their data. I ask that, if you use this program, you allow your customers to own all the data they have supplied to you either through their own input or through the APIs.

While I do not require this, I am interested in spreading the word about this program. If you wish to use this program, please offer attribution.

Released under the [Mozilla Public License
Version 2.0](http://www.mozilla.org/MPL/2.0/)
