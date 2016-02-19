from ebaysdk.trading import Connection
import sys
sys.path.append("/itemhut/pyebay/common/")
from common import *

from pprint import pprint

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')

def verifyAddItem():
    """http://www.utilities-online.info/xmltojson/#.UXli2it4avc
    """

    myitem = {
            "Item": {
                "Title": "Harry Potter and the Philosopher's Stone",
                "Description": "This is the first book in the Harry Potter series. In excellent condition!",
                "PrimaryCategory": {"CategoryID": "377"},
                "StartPrice": "10000.0",
                "CategoryMappingAllowed": "true",
                "Country": "US",
                "ConditionID": "3000",
                "Currency": "USD",
                "DispatchTimeMax": "3",
                "ListingDuration": "Days_7",
                "ListingType": "Chinese",
                "PaymentMethods": "PayPal",
                "PayPalEmailAddress": "dbtoomey@gmail.com",
                "PictureDetails": {"PictureURL": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Item.png"},
                "PostalCode": "95125",
                "Quantity": "1",
                "ReturnPolicy": {
                    "ReturnsAcceptedOption": "ReturnsAccepted",
                    "RefundOption": "MoneyBack",
                    "ReturnsWithinOption": "Days_30",
                    "Description": "If you are not satisfied, return the book for refund.",
                    "ShippingCostPaidByOption": "Buyer"
                },
                "ShippingDetails": {
                    "ShippingType": "Flat",
                    "ShippingServiceOptions": {
                        "ShippingServicePriority": "1",
                        "ShippingService": "USPSMedia",
                        "ShippingServiceCost": "2.50"
                    }
                },
                "Site": "US"
            }
        }

    api.execute('AddItem', myitem)
    print(api.response_json())

verifyAddItem()
