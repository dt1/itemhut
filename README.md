#Item Hut

Item Hut is a free and open-source marketing, ERP, CRM, and channel-management tool mainly focusing on B2B.

###Web Site

https://itemhut.com/

The version found here is sligtly different. For example, you are able to create users and login. The version on the website tends to lag behind what is found here. Bugs found on the site tend to be fixed here.

###Current Status
Under active development. To keep things progressing along smoothly, Item Hut is going to begin as an inventory system. However, there are tables for ebay orders, Amazon products, etc. Please refer to the er-diagrams.

###Currently Working On
* Order Scan out and Quality Control.
* User roles and groups.
* Label Printing.
* Email fetching.
* Documentation.

###Code Layout
* / -- The running web-based system
* build_database/ -- for building out the database, which includes files I'm working on along with the files needed to build the system.
* full/ -- all routes for the full system. All are work in progress, but many have multiple pages.
* models/ -- connecting to the database.
* pydb/ -- for connecting to the database.
* pyebay/ -- working files for ebay API interaction. Work in progress.
* routes/ -- routes that are fully functional. All are found on the demo found at itemhut.com
* static/ -- css / js / img.
* views/ -- html generating templates. Many of these views are for the full system and are not shown on the demo.
* er-diagrams/ -- ER Diagrams for the database.
* pydb/ -- for connecting to the database.

####Viewing ER Diagrams

The ER Diagrams were created using Dia:
http://dia-installer.de/

####Release Schedule and Upgrading

Item Hut is a nightly rolling release. Each push to this repo should be stable.

There are no update scripts with each version. Some updates will require manual intervention. Be sure to backup your database, diff the schemas, and be prepared to do ETL.

####Inventory System Setup
PostgreSQL 9.5

Python packages:
* Python3
* Python Bottle
* Psycopg2
* bcrypt
* hmac
* beaker
* google-api-python-client

Please be sure you have the latest version of each package.
For example, Bottle version 0.12.9 is needed to do file uploads.

clone to ~/itemhut:
```bash
$ git clone https://github.com/dt1/itemhut.git
```

setup the database
```bash
$ su - postgres
$ createdb itemhut
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/products/products.sql 
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/warehouse/warhouse.sql 
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/vendors/vendors.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/incoming/incoming.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/users/users.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/orders/orders.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/customers/company.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/marketplaces/marketplace.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/orders/orders.sql
$ psql -d itemhut -U postgres -f ~/itemhut/build_database/email/gmail.sql
```

run bottle:
```
$ python3 ~/itemhut/inventory.py
```

open localhost:8082

You will see a "Create First User" page.

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
