Item Hut Documentation
======================

What is Item Hut?
-----------------

Item Hut is free and open source channel's manager, ERP, CRM, inventory, and marketing analysis system, mainly focusing on B2B and online portals, written in Python3 and PostgreSQL 9.5+.

Versioning and release schedule
--------------------------------

Item Hut is a rolling release, however, we do not currently supply update scripts. For the Python code, this will not matter much, however, the database often goes through structural changes, and migration scripts are currently not included in the SQL files.

Item Hut keeps up with the latest stable releases of each needed project and we do not consider backwards compatibility to prior versions of PostgreSQL, Python, or any other needed library. When later versions of PostgreSQL are released, Item Hut will require that version of the database to run without errors.

Goals of the project, for the end-user
---------------------------------------

Item Hut is presently not a single-click install system. This may change in the future.

We have attempted to make installation as simple as possible, however, you will have to have some technical know-how.

Systems and Programs
---------------------

Item Hut is built on the most recent version of Fedora Linux. It has not been tested on any other version of Linux, nor has it been tested on Mac OS or Windows.

Further details of the installation are included in the install section.

System Design Goals
-------------------

Item Hut is, first and foremost, an engine, which should be able to be used on any backend system or even a headless command line, on a local machine or a server. For this reason, we ignore some web-building best practices.
