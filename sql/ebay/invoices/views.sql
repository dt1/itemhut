create view ebay_invoices.credit_final_value as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'CreditFinalValue';

create view ebay_invoices.fee_insertion as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'FeeInsertion';

create view ebay_invoices.subscription_ebay_stores as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'SubscriptioneBayStores';

create view ebay_invoices.sales_reports_plus_fee as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'SalesReportsPlusFee';

create view ebay_invoices.subscription_sm_basic as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'SubscriptionSMBasic';

create view ebay_invoices.subtitle_fee as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'SubtitleFee';

create view ebay_invoices.custom_code as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'CustomCode';

create view ebay_invoices.fee_final_value as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'FeeFinalValue';

create view ebay_invoices.fee_picture_pack as
select * 
from ebay_invoices.invoices
where account_details_entry_type = 'FeePicturePack';
