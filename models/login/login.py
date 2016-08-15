# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

def select_user_count():
    dbconn.cur.execute(
        """
        select count(*)
        from users.users;
        """)
    a = dbconn.cur.fetchall()
    if a[0][0] > 0:
        return True
    else:
        return False

def select_user_password_role(username):
    dbconn.cur.execute(
        """
        select password, user_role
        from users.users
        where user_name = %s;
        """, [username])
    a = dbconn.cur.fetchall()
    return a
