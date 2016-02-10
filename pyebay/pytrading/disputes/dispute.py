#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection
import sys
sys.path.append("/itemhut/pyebay/common/")
sys.path.append("/itemhut/pydb/")
import common
import conn
from psycopg2.extras import Json
import simplejson

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')

def dispute_reason(reason):
    dr = {}
    if reason in ['BuyerHasNotPaid', 'TransactionMutuallyCanceled']:
        dr.setdefault('DisputeReason', reason)
    return dr

# def dispute_explanation(explanation):
#     if (explanation in ['BuyerHasNotResponded', 
#                        'BuyerNoLongerRegistered', 
#                        'BuyerNotClearedToPay', 
#                        'BuyerRefusedToPay', 
#                        'ShippingAddressNotConfirmed', 
#                        'OtherExplanation', 
#                        'BuyerNotPaid', 
#                        'BuyerPaymentNotReceivedOrCleared', 
#                        'SellerDoesntShipToCountry', 
#                        'ShipCountryNotSupported'] and 
#         setdefault('DisputeReason'] == 'BuyerHasNotPaid'):
#         setdefault('DisputeExplanation'] = explanation

#     elif (explanation in ['BuyerNoLongerWantsItem', 
#                          'BuyerPurchasingMistake', 
#                          'ShippingAddressNotConfirmed', 
#                          'BuyerReturnedItemForRefund', 
#                          'UnableToResolveTerms', 
#                          'OtherExplanation'] and 
#           setdefault('DisputeReason',= 'TransactionMutuallyCanceled'):
#         setdefault('DisputeExplanation', explanation

#     else:
#         del setdefault('DisputeReason']


def item_id(item_id):
    ii = {}
    ii.setdefault('ItemID', item_id)
    return ii

def order_line_item_id(olid):
    olii = {}
    olii.setdefault('OrderLineItemID', olid)
    return olii

def transaction_id(trans_id):
    ti = {}
    ti.setdefault('TransactionID', trans_id)
    return ti

def error_language(lang):
    el = {}
    el.setdefault('ErrorLanguage', lang)
    return el

def message_id(m_id):
    mi = {}
    mi.setdefault('MessageID', m_id)
    return mi

def version(version):
    v = {}
    v.setdefault('Version', version)
    return v

def warning_level(wl):
    wl = {}
    wl.setdefault('WarningLevel', wl)
    return wl
        
QUERY = {}

def create_map(*args):
    for i in args:
        QUERY.update(i)

dr = dispute_reason('BuyerHasNotPaid')
##dispute_explanation('BuyerHasNotResponded')
ii = item_id('iid')
olid = order_line_item_id('olid')
ti = transaction_id('trans')
el = error_language('lang')
mi = message_id('mid')
v = version('one')
wl = warning_level('level')

create_map(dr, ii, olid, ti, el, mi, v, wl)

# api.execute('AddDisputeRequest', query)

print(QUERY)
