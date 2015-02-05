# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection
import sys
sys.path.append("/omark/pyebay/common/")
import common

api = Connection(config_file = '/omark/pyebay/ebay.yaml')

def comment_type(t):
    ct = {}
    if t in ['Negative', 'Neutral', 'Positive', 'Withdrawn']:
        ct.setdefault('CommentType', t)
    return ct

def feedback_id(f_id):
    fi = {}
    fi.setdefault('FeedbackID', f_id)
    return fi

def feedback_type(f_type):
    ft = {}
    if f_type in ['FeedbackLeft', 
                  'FeedbackReceived', 
                  'FeedbackReceivedAsBuyer', 
                  'FeedbackReceivedAsSeller']:
        ft.setdefault('FeedbackType', f_type)
    return ft

def item_id(item_id): 
    ii = {}
    if len(item_id) <= 19:
        ii.setdefault('ItemId', item_id)
    return ii

def order_line_item_id(oli_id):
    olid = {}
    if len(oli_id) <= 100:
        olid.setdefault('OrderLineItemID', oli_id)
    return olid

def transaction_id(t_id):
    ti = {}
    if len(t_id):
        ti.setdefault('TransactionID', t_id)
    return ti

def user_id(user_id):
    ui = {}
    ui.setdefault('UserID', user_id)
    return ui

QUERY = {}

def create_map(*args):
    for i in args:
        QUERY.update(i)

ct = comment_type('Negative')
ft = feedback_type('FeedbackLeft')

create_map(ct, ft)

zz = api.execute('GetFeedback', QUERY).response_json()
print(zz)
