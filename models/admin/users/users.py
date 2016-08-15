# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def insert_new_user(username, password, real_name,  utype, urole):
    dbconn.cur.execute(
        """
        select user_name
        from users.users
        where user_name = %(username)s;
        """, {"username": username})
    a = dbconn.cur.fetchall()
    if a:
        return True

    dbconn.cur.execute(
        """
        begin;
        insert into users.users (user_name, password, person_name,
                user_type, user_role)
        values (trim(%(user_name)s), %(password)s, 
        trim(%(person_name)s), trim(%(user_type)s), 
        trim(%(user_role)s));
        commit
        """, {"user_name": username,
              "password" :password,
              "person_name": real_name,
              "user_type": utype,
              "user_role": urole})

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
        where user_name = %(user_id)s;
        """, {"user_id" : uid})
    a = dbconn.cur.fetchall()
    return a

def update_user(original_username, username, real_name, utype,
                urole):
    if original_username != username:
        dbconn.cur.execute(
            """
            select user_name
            from users.users
            where user_name = %(username)s;
            """, {"username": username})
        a = dbconn.cur.fetchall()
        if a:
            return True

    if utype == "":
        utype = None

    dbconn.cur.execute(
        """
        begin;
        select users.update_user(%(original_username)s, 
        %(username)s, %(real_name)s, %(user_type)s, %(user_role)s);
        commit;
        """, {"original_username": original_username,
              "username": username,
              "real_name": real_name,
              "user_type": utype,
              "user_role": urole})

def update_user_password(uid, pwd):
    dbconn.cur.execute(
        """
        begin;
        update users.users
        set password = %(pwd)s
        where user_name = %(uid)s;
        commit;
        """, {"pwd": pwd,
              "uid": uid})
