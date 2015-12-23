#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# A full explanation of the AddDisuputeResponse portion of the eBay API can be found here: http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddDisputeResponse.html#AddDisputeResponse

from ebaysdk.trading import Connection
import sys
sys.path.append("/omark/pyebay/common/")
from common import Universal

api = Connection(config_file = '/omark/pyebay/ebay.yaml')

class AddDisputeResponse(Universal):
    def dispute_activity(self, activity):
        if activity in ['CameToAgreementNeedFVFCredit',
                        'MutualAgreementOrNoBuyerResponse',
                        'SellerAddInformation',
                        'SellerComment',
                        'SellerCompletedTransaction',
                        'SellerEndCommunication',
                        'SellerOffersRefund',
                        'SellerPaymentNotReceived',
                        'SellerShippedItem']:
            self.query['DisputeActivity'] = activity
            
    def dispute_id(self, d_id):
        self.query['DisputeID'] = d_id
        
    def message_text(self, text):
        self.query['MessageText'] = text
        
    def tracking(self, tracking):
        self.query['ShipmentTrackNumber'] = tracking
        
    def shipping_carrier(self, carrier):
        self.query['ShippingCarrierUsed'] = carrier
        
    def shipping_time(self, time):
        self.query['ShippingTime'] = time
                    
class Query(AddDisputeResponse):
    def __init__(self, **kwargs):
        self.query = {}
        for k in kwargs:
            self.query = dict(zip(self.KEYS[k], value))

dd = Query()
dd.dispute_activity('SellerComment')
dd.dispute_id('123')
dd.message_text('text is here!')
dd.tracking('00000011111')
dd.shipping_carrier('UPS')
dd.shipping_time('noon')

print(dd.query)
