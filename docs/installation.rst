Installation
============

System Requirements
-------------------
**note**: Item Hut has not been built or tested on Mac OS or Windows.

(install with your package manager)

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

The Database
------------

Initial Setup
^^^^^^^^^^^^^

create the itemhut database::

   $ su - postgres
   $ createdb itemhut

If this is your first time using PostgreSQL, you have to create a password for the postgres user::

  $ psql
  postgres=# alter user postgres with encrypted password "<password>"
  postgres=# \q

edit the pg_hba.conf (still as postgres)::

  $ cd data
  $ [editor] pg_hba.conf

change peer to md5 then restart the PostgreSQL server.
Create a .pgpass File:

cd to the home directory of the user who is running the system::

  $ cd

create .pgpass::

  $ touch .pgpass

edit .pgpass with your prefered editor::

  $ [editor] .pgpass

add the following, filling in the bracketed::

  <host>:<port>:itemhut:postgres:<password>

in general, the .pgpass file will look like this, where password is whatever you made the password when you updated the postgres user password::

  localhost:5432:itemhut:postgres:<password>

Install Item Hut
----------------

clone the repo::

  $ git clone https://github.com/dt1/itemhut.git

cd to directory::

  $ cd itemhut

run setup::

  $ pip3 install . --upgrade

setup the database::

  $ python3 build_db.py

Run Itemhut::

  $ python3 inventory.py

open localhost:8082 in your browser.

You will see a "Create First User" page.
