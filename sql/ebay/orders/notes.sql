--creating function
--varchar
select v#>'{OrderArray, Order}'->1#>>'{SellerEmail}'
from ebay_orders.json_insert;

--varchar
select v#>'{OrderArray, Order}'->1#>>'{IntegratedMerchantCreditCardEnabled}'
from ebay_orders.json_insert;

-- TransactionArray (do not put into database):

select v#>'{OrderArray, Order}'->1#>>'{TransactionArray}'
from ebay_orders.json_insert;

select v#>'{OrderArray, Order, 0}'
from ebay_orders.json_insert;

select json_array_length(v#>'{OrderArray, Order}')
from ebay_orders.json_insert;

-- transaction id:
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, TransactionID}'
from ebay_orders.json_insert;


-- Payment Hold Status
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Status, PaymentHoldStatus}'
from ebay_orders.json_insert;



-- shipping currency 
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualShippingCost, _currencyID}'
from ebay_orders.json_insert;

-- shipping cost to buyer 
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualShippingCost, value}'
from ebay_orders.json_insert;


-- handling currency
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualHandlingCost, _currencyID}'
from ebay_orders.json_insert;

-- handling value
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ActualHandlingCost, value}'
from ebay_orders.json_insert;

-- Shipping Carrier
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ShippingDetails, ShipmentTrackingDetails, ShippingCarrierUsed}'
from ebay_orders.json_insert;

-- Shipping Tracking
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ShippingDetails, ShipmentTrackingDetails, ShipmentTrackingNumber}'
from ebay_orders.json_insert;

-- Transaction Currency
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, TransactionPrice, _currencyID}'
from ebay_orders.json_insert;


-- Transaction Price
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, TransactionPrice, value}'
from ebay_orders.json_insert;

-- transaction site id 
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, TransactionSiteID}'
from ebay_orders.json_insert;

-- Total Taxes Currency
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TotalTaxAmount, _currencyID}'
from ebay_orders.json_insert;

-- Total Taxes Amount
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TotalTaxAmount, value}'
from ebay_orders.json_insert;

-- Sales (?) Tax Currency Type
-- varchar
select v#>'{OrderArray, Order}'->1#>'{TransactionArray, Transaction, Taxes, TaxDetails}'->1#>>'{TaxAmount, _currencyID}'
from ebay_orders.json_insert;

-- Sales (?) Tax Currency Amount
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 1, TaxAmount, value}'
from ebay_orders.json_insert;

-- Handling Tax Currency Type
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 0, TaxOnHandlingAmount, _currencyID}'
from ebay_orders.json_insert;

-- Handling Tax Currency Amount
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 0, TaxOnHandlingAmount, value}'
from ebay_orders.json_insert;

-- Sales (?) Tax Imposition
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails'->(1)->>'{Imposition}'
from ebay_orders.json_insert;

-- Shipping Tax Currency Type
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 0, TaxOnShippingAmount, _currencyID}'
from ebay_orders.json_insert;

-- Shipping Tax Currency Amount
-- numeric
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 0, TaxOnShippingAmount, value}'
from ebay_orders.json_insert;

-- Sales (?) Tax Description
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Taxes, TaxDetails, 1, TaxDescription}'
from ebay_orders.json_insert;


------------------------------


-- Transaction QTY
-- int
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, QuantityPurchased}'
from ebay_orders.json_insert;






-- Item Details

-- Buyer Email
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, Buyer, Email}'
from ebay_orders.json_insert;

-- Transaction ID
-- bigint
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, TransactionID}'
from ebay_orders.json_insert;

-- Order Line Item ID
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, OrderLineItemID}'
from ebay_orders.json_insert;



-- Selling Manager Sales Record
-- int
select v#>'{OrderArray, Order}'->1#>>'{TransactionArray, Transaction, ShippingDetails, SellingManagerSalesRecordNumber}'
from ebay_orders.json_insert;

-- Created Time
-- timestamp
select v#>'{OrderArray, Order}'->1#>>>'{CreatedTime}'
from ebay_orders.json_insert;

-- Currency ID
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{Total, _currencyID}'
from ebay_orders.json_insert;


-- Checkout Status
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{CheckoutStatus, Status}'
from ebay_orders.json_insert;

-- Payment Method
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{CheckoutStatus, PaymentMethod}'
from ebay_orders.json_insert;

-- Last Modified Time (for listing?)
-- timestamp
select v#>'{OrderArray, Order}'->1#>>'{CheckoutStatus, LastModifiedTime}'
from ebay_orders.json_insert;

-- eBay Payment Status
-- varchar
select v#>'{OrderArray, Order}'->1#>>'{CheckoutStatus, eBayPaymentStatus}'
from ebay_orders.json_insert;

-- Checkout Status
-- boolean
select v#>'{OrderArray, Order}'->1#>>'{CheckoutStatus, IntegratedMerchantCreditCardEnabled}'
from ebay_orders.json_insert;

-- Checkout Status
-- boolean
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, GetItFast}'
from ebay_orders.json_insert;

-- Selling Manager Sales Record
-- int
select v#>'{OrderArray, Order}'->1#>>'{ShippingDetails, SellingManagerSalesRecordNumber}'
from ebay_orders.json_insert;




-- Sales Tax Percent
-- numeric
select v#>'OrderArray}'
from ebay_orders.json_insert;

