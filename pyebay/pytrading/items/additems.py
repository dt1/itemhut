# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# To start, I am going to use json to interact with PostgreSQL. I do plan to add in python dict and xml interop.

##For an overview of the eBay AddItems API: http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddItem.html#AddItem. The items that are specific to half.com are not included. Examples include: ListingType

from ebaysdk.trading import Connection

api = Connection(config_file = '/omark/pyebay/ebay.yaml')

