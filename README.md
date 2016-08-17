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

System Requiremnts (install with your package manager)
* PostgreSQL 9.5
* PostgreSQL 9.5 Server
* PostgreSQL 9.5 Devel
* gcc
* python3-devel
* redhat-rpm-config (if on redhad / fedora / CentOS)
* Python3
* Python3 Devel


running pip3 install will download the following packages (see setup.py):
* Python3 Bottle 0.12.9
* Psycopg2 2.6.2
* Beaker 1.8.0
* bcrypt 3.1.0
* py-bcrypt 0.4
* google-api-python-client

####Installation
These instructions assume you have .pgpass enabled.

clone to ~/itemhut:
```bash
$ git clone https://github.com/dt1/itemhut.git
```

cd to directory:
```bash
$ cd /itemhut
```

run setup:
```bash
$ pip3 install . --upgrade
```

setup the database
```bash
$ python3 build_db.py
```

run bottle:
```
$ python3 inventory.py
```

open localhost:8082

You will see a "Create First User" page.

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
