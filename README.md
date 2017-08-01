Item Hut
========

Item Hut is a free and open-source marketing, ERP, CRM, and channel-management tool mainly focusing on B2B.

Current Status
==============

This project is, for the moment, unmaintained / dead. If you are interested in taking this project over, please feel free to contact me. I will do everything I can to make the transition as smooth as possible.

Even though this project is currently considered dead, if you find a bug, have questions about setup or how to to use the system, please open a bug report. 

Documentation
-------------

https://itemhut.readthedocs.io/en/latest/

Features
--------
* Warehousing / inventory - locations, QC in, QC out, movement tracking, pallet creations, etc
* Local B&M + 3PL warehousing
* Product management - descriptions, pictures, upc's, model numbers, etc.
* extra tools, such as upc label creation
* Company Suppliers CRM
* Customer CRM - emails, order history, etc info
* Invoices for incoming Supplies
* Load images, invoices, other documentation
* Personnel - Admins, sales, inventory, forklift, managers, etc.
* Order history from end-user customers.

* Channels Management
* Ebay - order history, automated listing, feedback, etc (probably doesn't work since eBay constantly updates it's API)
* Amazon - Flat File generation (the database is partly built by downloading and generating the database from the flat flies).
* B&M store. This was a work-in-progress, but allowed for some localized storefront inventory and order history. No POS integration though.
* email integration with g-suite (not sure how well this one was working, but the idea was to have customer orders show up in a side-box and what-have-you)

I haven't used it myself for over a year, so this is all from memory, so possibly missing some information.


Was Working On
--------------
* Order Picking.
* Order Scan out and Quality Control.
* User roles and groups.
* Email fetching.
* Documentation.

Contributions Needed
---------------------

* UX / UI -- I'm not a designer by any stretch of the imagination and any ideas for fixing the look and UX is definitely appreciated.
* User roles and groups --  the current iteration is flaky at best, and I'm not happy with the current layout. This is a very difficult problem and placed on the back burner for now. Any ideas will be considered.

Code Layout
-----------
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

Viewing ER Diagrams
-------------------

The ER Diagrams were created using Dia:
http://dia-installer.de/

Installation
------------

see the documentation: https://itemhut.readthedocs.io/en/latest/

Expected Features
-----------------
* B2B Customer Management
* Inventory Management
* Basic Warehouse Management
* Intensive marketing analysis
* "Feature Complete" Ebay and Amazon API integration.
* Flat File creation
* Excellent Documentation

Permissions and Licensing
-------------------------

While I am unable to enforce this, I am a strong believer that a customer's data is their data. I ask that, if you use this program, you allow your customers to own all the data they have supplied to you either through their own input or through the APIs.

While I do not require this, I am interested in spreading the word about this program. If you wish to use this program, please offer attribution.

Released under the [Mozilla Public License
Version 2.0](http://www.mozilla.org/MPL/2.0/)
