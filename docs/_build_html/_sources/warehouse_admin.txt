Warehouse Administration
========================

To create a new warehouse, go to *admin>Add Warehouse*.

There are two kinds of warehouses in Item Hut, B&M, which is a warehouse where you control all aspects of inventory, and 3PL, which is a 3rd party warehouse.

B&M
---

A B&M warehouse allows you to create, add, and delete pallet and picking locations. You will also be allowed to create, add, delete, and move pallets.

You will also be allowed to do outbound QC. Inbound QC will be added later. The logging mechanisms do not function properly at this time.

3PL
---

A 3PL warehouse will only allow you to add products and view running inventory.

Internals
---------

Internally, B&M and 3PL warehouses behave the same. Instead of adding user-defined pallet locations, the pallet locations are added by system-generated hashes. If you switch a 3PL werehouse to a B&M warehouse, all the same features of a B&M warehouse will be available, though it will take some manual work to get all the data to reflect the reality of the B&M warehouse.

The opposite is also true: you are able to convert a B&M to 3PL and the system will behave as a 3PL. Although here is not GUI option to do this at the moment, you are able to change this setting at the database level.
