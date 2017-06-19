Item Hut
========

Item Hut is a free and open-source marketing, ERP, CRM, and channel-management tool mainly focusing on B2B.

Current Status
==============

This project is, for the moment, unmaintained / dead. If you are interested in taking this project over, please feel free to contact me. I will do everything I can to make the transition as smooth as possible.

Documentation
-------------

https://itemhut.readthedocs.io/en/latest/

###Current Status
Under active development. To keep things progressing along smoothly, Item Hut is going to begin as an inventory system. However, there are tables for ebay orders, Amazon products, etc. Please refer to the er-diagrams.

The code is going through a large refactoring and documentation stage. At this time, there is a general feature freeze in lieu of bug-fixes as I find them.

###Currently Working On
* Order Picking.
* Order Scan out and Quality Control.
* User roles and groups.
* Email fetching.
* Documentation.

###Contributions Needed For:
* UX / UI -- I'm not a designer by any stretch of the imagination and any ideas for fixing the look and UX is definitely appreciated.
* User roles and groups --  the current iteration is flaky at best, and I'm not happy with the current layout. This is a very difficult problem and placed on the back burner for now. Any ideas will be considered.

###Code Layout
* / -- The running web-based system
* build_database/ -- for building out the database, which includes files I'm working on along with the files needed to build the system.
* docs/ -- documentation for Read the Docs
* email/ -- for email, gmail, gchat integration
* er-diagrams/ -- ER Diagrams for the database.
* full/ -- all routes for the full system. All are work in progress, but many have multiple pages, though none are connected to the database.
* models/ -- database query files.
* pydb/ -- for connecting to the database + cur and dcur utilities.
* pyebay/ -- working files for ebay API interaction.
* routes/ -- routes that are fully functional. All are found on the demo found at itemhut.com
* sql/ -- work in progress sql files for amazon, ebay, etc.
* static/ -- css / js / img.
* views/ -- html generating templates. Many of these views are for the full system and are not shown on the demo. The extra views connect to the full routes.

####Viewing ER Diagrams

The ER Diagrams were created using Dia:
http://dia-installer.de/

####Release Schedule and Upgrading

Item Hut is a nightly rolling release. Each push to this repo should be stable.

There are no update scripts with each version. Some updates will require manual intervention. Be sure to backup your database, diff the schemas, and be prepared to do ETL.

####Installation
see the documentation: https://itemhut.readthedocs.io/en/latest/

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
