# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def insert_new_user(username, password, real_name,  utype, urole):
    dbconn.cur.execute(
        """
        select user_name
        from users.users
        where user_name = %s;
        """, [username])
    a = dbconn.cur.fetchall()
    if a:
        return True

    dbconn.cur.execute(
        """
        begin;
        insert into users.users (user_name, password, person_name,
                user_type, user_role)
        values (trim(%s), %s, trim(%s), trim(%s), trim(%s));
        commit
        """, [username, password, real_name, utype, urole])

def select_valid_roles():
    dbconn.cur.execute(
        """
        select user_role
        from users.valid_user_roles
        where user_role <> 'original admin';
        """)
    a = dbconn.cur.fetchall()
    return a

def select_valid_usertypes():
    dbconn.cur.execute(
        """
        select user_type
        from users.valid_user_types;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_users():
    dbconn.cur.execute(
        """
        select user_name, person_name, user_type, user_role
        from users.users;
        """)
    a = dbconn.cur.fetchall()
    return a

def select_user_info(uid):
    dbconn.cur.execute(
        """
        select user_name, person_name, user_type, user_role
        from users.users
        where user_name = %s;
        """, [uid])
    a = dbconn.cur.fetchall()
    return a

def update_user(original_username, username, real_name, utype,
                urole):
    if original_username != username:
        dbconn.cur.execute(
            """
            select user_name
            from users.users
            where user_name = %s;
            """, [username])
        a = dbconn.cur.fetchall()
        if a:
            return True

    if utype == "":
        utype = None

    dbconn.cur.execute(
        """
        begin;
        select users.update_user(%s, %s, %s, %s, %s);
        commit;
        """, [original_username, username, real_name,
              utype, urole])

def update_user_password(uid, pwd):
    dbconn.cur.execute(
        """
        begin;
        update users.users
        set password = %s
        where user_name = %s;
        commit;
        """, [pwd, uid])
