# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pydb.dbconn import cur, dcur

def select_user_count():
    a = dcur.execute(
        """
        select count(*)
        from users.users;
        """)
    a = dcur.fetchall()
    if a[0][0] > 0:
        return True
    else:
        return False

def select_user_password_role(username):
    a = dcur.execute(
        """
        select password, user_role
        from users.users
        where user_name = %(username)s;
        """, {"username": username})
    a = dcur.fetchall()
    return a

def insert_original_admin(uname, password):
    a = dcur.execute(
        """
        begin;
        insert into users.users (user_name, password, user_role)
        values (%s, %s, 'original admin');
        commit;
        """, [uname, password])
