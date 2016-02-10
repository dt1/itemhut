# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection
import sys
sys.path.append("/itemhut/pyebay/common/")
import common

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')

def comment_text(txt):
    ct = {}
    ct.setdefault('CommentText', txt)
    return ct

def comment_type(t):
    ct = {}
    if t in ['Negative', 'Neutral', 'Positive']:
        ct.setdefault('CommentType', t)
    return ct

def item_id(i_id):
    ii = {}
    ii.setdefault('ItemID', i_id)
    return ii

def order_line_item_id(o_id):
    olid = {}
    olid.setdefault('OrderLineItemID', o_id)
    return olid

def seller_item_rating_detail_array(rating, rating_detail):
    sirda = {}
    sirda.setdefault('SellerItemRatingDetailArray', {})
    sirda['SellerItemRatingDetailArray'].setdefault('ItemRatingDetails', {})
    if rating in [1, 2, 3, 4, 5]:
        sirda['SellerItemRatingDetailArray']['ItemRatingDetails'].setdefault('Rating', rating)
    
    if rating_detail in ['Communication', 'ItemAsDescribed', 'ShippingAndHandlingCharges', 'ShippingTime']:
        sirda['SellerItemRatingDetailArray']['ItemRatingDetails'].setdefault('RatingDetail', rating_detail)
    return sirda

def target_user(user_id):
    tu = {}
    tu.setdefault('TargetUser', user_id)
    return tu

def transaction_id(t_id):
    ti = {}
    ti.setdefault('TransactionID', t_id)
    return ti

QUERY = {}

def create_map(*args):
    for i in args:
        QUERY.update(i)

ctxt = comment_text('Great Buyer!')
ctype = comment_type('Positive')
ii = item_id(123)
olid = order_line_item_id(123)
sirda = seller_item_rating_detail_array(1, 'ItemAsDescribed')
tu = target_user('dude1')
ti = transaction_id(123)

create_map(ctxt, ctype, ii, olid, sirda, tu, ti)

print(QUERY)
    
