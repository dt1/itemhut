#!/usr/bin/env python3

from pydb.dbconn import cur, dcur

dbconn.cur.execute(open("build_database/users/users.sql", "r").read())
dbconn.cur.execute(open("build_database/products/products.sql", "r").read())
dbconn.cur.execute(open("build_database/warehouse/warehouse.sql", "r").read())
dbconn.cur.execute(open("build_database/vendors/vendors.sql", "r").read())
dbconn.cur.execute(open("build_database/incoming/incoming.sql", "r").read())
dbconn.cur.execute(open("build_database/marketplaces/marketplace.sql", "r").read())
dbconn.cur.execute(open("build_database/customers/company.sql", "r").read())
dbconn.cur.execute(open("build_database/orders/orders.sql", "r").read())
dbconn.cur.execute(open("build_database/email/gmail.sql", "r").read())

dbconn.conn.commit()
