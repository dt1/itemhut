#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection
import sys
sys.path.append("/omark/pyebay/common/")
sys.path.append("/omark/pydb/")
import dbconn

api = Connection(config_file = '/omark/pyebay/ebay.yaml')

def get_categories (detail_level = 'ReturnAll'):
    api.execute('GetCategories', {'DetailLevel' : detail_level})
    zz = api.response_json()
    dbconn.cur.execute("""INSERT INTO ebcats.json_insert_categories (v)
                          VALUES ($${0}$$);""".format(zz))


    
def get_category_features(detail_level = 'ReturnAll',
                          view_all_nodes = 'True'):
    api.execute('GetCategoryFeatures' , {'DetailLevel': detail_level,
                                      'ViewAllNodes' : view_all_nodes})
    zz = api.response_json()
    dbconn.cur.execute("""INSERT INTO 
                          ebcats.json_insert_category_features (v)
                          VALUES ($${0}$$);""".format(zz))
# print (zz)

get_category_features()

dbconn.conn.commit()
dbconn.cur.close()

print("success")
