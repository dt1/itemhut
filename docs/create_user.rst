Create Users
============

Creating the Super Admin
------------------------

The Super Admin is automatically created when you start Item Hut and create the initial user. You will be redirected to the main system, logged in.

Creating Other Users
--------------------

Go to *admin>Add User*.

You will be allowed to add a username, password, real name, role, and type.

Roles
^^^^^

Roles focus the user on a particular area and match the headings in the top menu. For example, a user assigned the "customers" role will only be allowed to see the customers sub section.

**note**: User roles are still under development. In the future, we plan to add groups, warehouse views, and more refined read-only permissions.

At this point, the Admin role has all of the same permissions as the Original Admin. We suggest you create a regular admin for working with Item Hut here on out.

Types
^^^^^

User Types allow Item Hut to focus on keeping data integrity. For right now, we only have the "sales" role. In order for a user to do a sale, he or she must be a member of the "sales" role. This would prevent say, a picker, from creating a sale, and so forth.

**note**: User Types are still under development. Just as user roles, we plan to add groups, which will allow a user to, for example, pick orders and create sales. For now, all new users have the sales type.

Internals
---------

When Item Hut starts up, the system checks for a "super admin" role in the database. If this role does not exist, the system will redirect to /initialize and have you create a new super admin.

If you forget the password for the super admin, you can delete the super admin from the databse, while keeping all of your data intact. This is why we suggest not using the super admin for anything in Item Hut. Password retrieval is not available in Item Hut at this time.

