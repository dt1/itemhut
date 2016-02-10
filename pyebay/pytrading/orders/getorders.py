#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

##For an overview of the eBay GetOrders API: http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/GetOrders.html. The items that are specific to half.com are not included. Examples include: ListingType

## I am assuming that the user wants the final value on by default.

## Undecided about OrderIDArray. For now, this is not included.

## OrderRole appears to assume you are also buying. Since this program is stricly for selling, I am not including bought items.

from ebaysdk.trading import Connection
import sys
sys.path.append("/itemhut/pyebay/common/")
sys.path.append("/itemhut/pydb/")
import common
import dbconn

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')

def creation_time(from_date, to_date):
    ct = {}
    ct.setdefault('CreateTimeFrom', from_date)
    ct.setdefault('CreateTimeTo', to_date)
    return ct
        
def include_final_value(tf):
    ifv = {}
    if tf in [True, False]:
        ifv.setdefault('IncludeFinalValue', tf)
    return ifv
        
def modified_between_dates(from_date, to_date):
    mbd = {}
    mbd.setdefault('ModTimeFrom', from_date)
    mbd.setdefault('ModTimeTo', to_date)
    return mbd

def number_of_days(days):
    nod = {}
    if days <= 30:
        nod.setdefault('NumberOfDays', days)
    return nod

QUERY = {}

def create_map(*args):
    for i in args:
        QUERY.update(i)
    
nod = number_of_days(30)
## mbd = modified_between_dates('then', 'now')
ifv = include_final_value(True)
# gp = common.get_pagination(10, 1)
# sorder = common.sorting_order('Ascending')
# bs = common.by_status('Active')

create_map(nod, ifv)

def get_orders(query):
    api.execute('GetOrders', query)
    zz = api.response_json()

    dbconn.cur.execute("""INSERT INTO ebords.json_insert (v)
                          VALUES ($${0}$$);""".format(zz))


get_orders(QUERY)

print(QUERY)

dbconn.conn.commit()
dbconn.cur.close()

print("success")


# print(zz)
