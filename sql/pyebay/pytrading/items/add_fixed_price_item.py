#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

## A full explanation of AddFixedPriceItem can be found here: http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/AddFixedPriceItem.html#AddFixedPriceItem

from ebaysdk.trading import Connection
import sys
sys.path.append("/itemhut/pyebay/common/")
from common import Universal

from pprint import pprint

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')


##Should be your listing_sku, not to be confused with the real product sku:


def application_data(sku):
    appData = {}
    if len(sku) <= 32:
        appData.setdefault('ApplicationData', sku)
    return appData

def auto_pay(tf):
    ap = {}
    if tf in [True, False]:
        ap.setdefault('AutoPay', tf)
    return ap
        
def best_offer_enabled(tf):
    bod = {}
    if tf in [True, False]:
        bod.setdefault('BestOfferDetails', 
                       {}).setdefault('BestOfferEnabled', tf)
    return bod

# dd = application_data('mySku')
# ee = auto_pay(True)
# ff = best_offer_enabled(True)

# print(dd)
# print(ee)
# print(ff)

def linked_paypal(tf):
    brd = {}
    if tf in [True, False]:
        brd.setdefault('BuyerRequirementDetails', 
                       {}).setdefault('LinkedPayPalAccount', tf)
    return brd

## period is represented as Days_30, Days_180, etc
# def max_buyer_violations_count(cnt = None, period = None):
#     mmbpv = {}
#     if cnt is not None:
#         mbpv.setdefault('MaximumBuyerPolicyViolations', 
#                         {}).setdefault('Count' , cnt)

# def max_buyer_violations_period(period),
#     mbpv.setdefault('MaximumBuyerPolicyViolations'].setdefault('Period' , period)


def maximum_item_count(cnt):
    mir = {}
    mir.setdefault('MaximumItemRequirements', 
                   {}).setdefault('MaximumItemCount' , cnt)
    return mir

# def minimum_feedback_score(cnt):
#     brd = {}
#     if cnt in [-1, -2, -3],
#         brd.setdefault('BuyerRequirementDetails', 
#                        {}).setdefault('MinimumFeedbackScore', cnt)
#     return self

# def musi_count(cnt),
#     musi.setdefault('MaximumUnpaidItemStrikesInfo'].setdefault('Count' , cnt)
#     query.setdefault('BuyerRequirementDetails'].setdefault(musi)

# def musi_period(period),
#     musi.setdefault('MaximumUnpaidItemStrikesInfo'].setdefault('Period' , period)
#     query.setdefault('BuyerRequirementDetails'].setdefault(musi)

# ## blocks bidders who reside in the ship-to exclusion list. For some reason, this defaults to false in the API. Here I default it to true
# def ship_to_reg_country(tf = True),
#     if tf in .setdefault(True, False],
#         query.setdefault('BuyerRequirementDetails'].setdefault('ShipToRegistrationCountry' , tf)

# def vu_minimum_feedback_score(cnt),
#     vur.setdefault('VerifiedUserRequirements'].setdefault('MinimumFeedbackScore' , cnt)
#     query.setdefault('BuyerRequirementDetails'].setdefault(vur)

# def vu_verified_user(tf),
#     if tf in .setdefault(True, False],
#         vur.setdefault('VerifiedUserRequirements'].setdefault('VerifiedUser' , tf)
#         query.setdefault('BuyerRequirementDetails'].setdefault(vur)

#     ## Thre is a field called ZeroFeedbackScore that is only available in China. I'm going to skip this one for now

def cat_based_att_prefill(tf):
    cbar = {}
    if tf in [True, False]:
        cbar.setdefault('CategoryBasedAttributesPrefill',  tf)
    return cbar

def cat_map_allowed(tf):
    cma = {}
    if tf in [True, False]:
        cma.setdefault('CategoryMappingAllowed', tf)
    return cma

def charity(c_id, c_num, donation_percent):
    char = {}
    char.setdefault('Charity', {})
    char['Charity'].setdefault('CharityID' , c_id)
    char['Charity'].setdefault('CharityNumber', c_num)
    char['Charity'].setdefault('DonationPercent', donation_percent)
    return char

def condition_description(desc):
    cd = {}
    cd.setdefault('ConditionDescription', desc)
    return cd

def condition_id(id):
    cid = {}
    cid.setdefault('ConditionID', id)
    return cid

# ## for the database, get country list here, http,//developer.ebay.com/DevZone/XML/docs/Reference/ebay/extra/AddFxdPrcItmRqst.Itm.Cntry.html
def country(country):
    ctry = {}
    ctry.setdefault('Country', country)
    return ctry

# ## Not all countries are available, http,//developer.ebay.com/DevZone/guides/ebayfeatures/Development/Feature-MultipleSiteListing.html
def cross_border_trade(country):
    cbt = {}
    if country in ['US', 'Canada', 'UK', 'Ireland']:
        cbt.setdefault('CrossBorderTrade', country)
    return cbt

def currency(currency = 'USD'):
    ccy = {}
    if currency in ['AUD', 'CAD', 'CHF', 'CNY', 'EUR', 'GBP', 'HKD', 
                    'INR', 'MYR', 'PHP', 'PLN', 'SEK', 'GSD', 'TWD', 
                    'USD']:
        ccy.setdefault('ConditionID', currency)
    return ccy

def description(desc):
    desc = {}
    desc.setdefault('Description', desc)
    return desc

def disable_buyer_requirements(tf):
    dbr = {}
    if tf in [True, False]:
        dbr.setdefault('DisableBuyerRequirements', tf)
    return dbr

def made_for_otlet_comparison_price(price):
    mfocr = {}
    mfocr.setdefault('MadeForOutletComparisonPrice', price)
    return mfocr

def minimum_advertised_price(price):
    mmap = {}
    mmap.setdefault('MinimumAdvertisedPrice', price)
    return mmap

def minimum_advertised_price_exposure(opt):
    mmape = {}
    if opt in ['DuringCheckout', 'None', 'PreCheckout']:
        mmap.setdefault('ConditionID', opt)
    return mmape

def original_retail_price(price):
    orp = {}
    orp.setdefault('OriginalRetailPrice', price)
    return orp

def sold_off_ebay(tf):
    sofe = {}
    if tf in [True, False]:
        sob.setdefault('SoldOffeBay', tf)
    return sob

def sold_on_ebay(tf):
    sone = {}
    if tf in [True, False]:
        sone.setdefault('SoldOneBay', tf)
    return sone

# ## Maximum time for packagind and sending to carrier
def dispatch_time_max(days):
    dtm = {}
    dtm.setdefault('DispatchTimeMax', days)
    return dtm

def ebay_now_eligible(tf):
    ene = {}
    if tf in [True, False]:
        ene.setdefault('eBayNowEligible', tf)
    return ene

def get_it_fast(tf):
    gifa = {}
    if tf in [True, False]:
        gifa.setdefault('GetItFast', tf)
    return gifa

# ## Not Available in the US,
def gift_icon(n):
    gi = {}
    gi.setdefault('GiftIcon', n)
    return gi

def gift_services(n):
    gs = {}
    gs.setdefault('GiftServices', n)
    return gs

def hit_counter(style):
    hc = {}
    if style in ['BasicStyle', 'GreenLED', 'Hidden', 'HiddenStyle', 
                'HonestyStyle', 'NoHitCounter', 'RetroStyle']:
        hc.setdefault('HitCounter', style)
    return hc

def include_recommendations(tf):
    ir = {}
    if tf in [True, False]:
        ir.setdefault('IncludeRecommendations', tf)
    return ir

def inventory_tracking_method(method):
    itm = {}
    if method in ['ItemID', 'SKU']:
        itm.setdefault('InventoryTrackingMethod', method)
    return itm

# ## sounds like a lot of stuff, will do later,
# def item_compatibility_list(icl),
#     pass

# def name_value_list_name(name):
#     nvname.setdefault('Name'] = name
#     nvlist.setdefault('NameValueList'].setdefault(nvname)
#     itspec.setdefault('ItemSpecifics'].setdefault(nvlist)
#     query.setdefault(itspec)

# def name_value_list_value(val),
#     nvvalue.setdefault('Value'] = val
#     nvlist.setdefault('NameValueList'].setdefault(nvvalue)
#     itspec.setdefault('ItemSpecifics'].setdefault(nvlist)
#     query.setdefault(itspec)

def pro_stores_store_name(sname):
    pssn = {}
    pssn.setdefault('ProStoresStoreName', sname)
    return pssn

def seller_third_party_username(pname):
    stpu = {}
    stpu.setdefault('SellerThirdPartyUsername', pname)
    return stpu

def listing_designer(l_id, psize, t_id):
    ld = {}
    ld.setdefault('ListingDesigner', {})
    ld.['ListingDesigner'].setdefault('LayoutId', l_id)
    ld.['ListingDesigner'].setdefault('OptimalPictureSize', psize)
    ld.setdefault('ThemeId', t_id)
    return ld

def listing_details(boaap, lld, mbop):
    ld = {}
    ld.setdefault('ListingDetails', {})
    ld.setdefault('BestOfferAutoAcceptPrice', boaap)
    ld.setdefault('LocalListingDistance', lld)
    ld.setdefault('MinimumBestOfferPrice', mbop)
    return ld

def listing_duration(dur):
    ld = {}
    ld.setdefault('ListingDuration', dur)
    return ld

def listing_enhancement(enhancment):
    le = {}
    if enhancement in ['BasicUpgradePackBundle', ' BoldTitle', ' Border', 
                       ' CustomCode', ' Featured', 'Highlight', 
                       'HomePageFeatured', 'ProPackBundle', 
                       'ProPackPlusBundle', 'ValuePackBundle']:
        le.setdefault('ListingEnhancement', enhancement)
    return le

def listing_type(ltype):
    lt = {}
    if ltype in ['FixedPriceItem']:
        lt.setdefault('ListingType', ltype)
    return lt

## probably better to just use Postal Code
def location(n):
    loc = {}
    loc.setdefault('Location', n)
    return loc

def out_of_stock_control(tf):
    oosc = {}
    if tf in [True, False]:
        oosc.setdefault('OutOfStockControl', tf)
    return tf

## Lots of complicated rules here: http://developer.ebay.com/DevZone/XML/docs/Reference/ebay/extra/AddFxdPrcItmRqst.Itm.PymntMthds.html

def payment_methods(method):
    pm = {}
    if metod in ['AmEx', 'CashInPerson', 'CashOnPickup', 'CCAccepted', 
                 'COD', 'CODPrePayDelivery', 'CreditCard', 'CustomCode', 
                 'Diners', 'DirectDebit', 'Discover', 'VisaMC'
                 'IntegratedMerchantCreditCard', 'LoanCheck', 'MOCC', 
                 'Moneybookers', 'MoneyXferAccepted', 'None', 'Other'
                 'MoneyXferAcceptedInCheckout', 'Paymate',
                 'OtherOnlinePayments', 'PaisaPayAccepted', 'PaisaPayEscrow', 
                 'PaisaPayEscrowEMI', 'PaymentSeeDescription', 
                 'PayOnPickup', 'PayPal', 'PersonalCheck', 'ProPay', 
                 'StandardPayment']:
        pm.setdefault('PaymentMethods', method)
    return pm

def paypal_email_address(addr):
    pea = {}
    pea.setdefault('PayPalEmailAddress', pea)
    return pea

def pickup_in_store_details(tf):
    pisd = {}
    pisd.setdefault('PickupInStoreDetails', {})
    if tf in [True, False]:
        pisd['PickupInStoreDetails'].setdefault('EligibleForPickupInStore', tf)
    return pea

## duration is Days_7, LifeTime, Days_20, etc.
def picture_details(duration, gtype, g_url, p_display, p_source, p_url):
    pd = {}
    pd.setdefault('PictureDetails', {})
    pd['PictureDetails'].setdefault('GalleryDuration', duration)

    if gtype in ['Featured', 'Gallery', 'None', 'Plus']:
        pd['PictureDetails'].setdefault('GalleryType', gtype)

    
    pd['PictureDetails'].setdefault('GalleryURL', g_url)

    if p_display in ['None', 'PicturePack', 
                     'SuperSize', 'SuperSizePictureShow']:
        pd['PictureDetails'].setdefault('PhotoDisplay', p_display)

    if p_source in ['EPS', 'Vendor']:
        pd['PictureDetails'].setdefault('PictureSource', p_source)
    
    pd['PictureDetails'].setdefault('PictureURL', p_url)    
    return pd

def postal_code(p_code):
    pc = {}
    pc.setdefault('PostalCode', p_code)
    return pc

## Vaidation Check is much too large to put here, though I may
## include it in the database soon: 
## http://listings.ebay.com/_W0QQloctZShowCatIdsQQsacatZQ2d1QQsalocationZatsQQsocmdZListingCategoryList
def primary_category(p_id):
    pc = {}
    pc.setdefault('PrimaryCategory', {})
    pc['PrimaryCategory'].setdefault('CategoryID', p_id)
    return pc

def private_listing(tf):
    pl = {}
    if tf in [True, False]:
        pl.setdefault('PrivateListing', tf)
    return pl

def private_notes(notes):
    pn = {}
    pn.setdefault('PrivateNotes', notes)
    return pn

def product_listing_details(brand, mpn, ean, gtin, ):
    pld = {}
    pld.setdefault('ProductListingDetails', {})
    pld['ProductListingDetails']
    return pld
    
    
    


# dd = Query()
# dd.application_data('my sku')
# dd.auto_pay(True)
# dd.best_offer_enabled(False)
# dd.linked_paypal(True)
# dd.linked_paypal(True)
# dd.max_buyer_violations_count(3)
# dd.max_buyer_violations_period(45)
# dd.maximum_item_count(5)
# dd.minimum_feedback_score(-2)
# dd.musi_count(9)
# dd.musi_period('Days_40')
# dd.ship_to_reg_country()
# dd.vu_minimum_feedback_score(4)
# dd.vu_verified_user(True)
# dd.cat_based_att_prefill(True)
# dd.cat_map_allowed(False)
# dd.charity_id(123)
# dd.charity_number(50)
# dd.charity_donation_percent(50)
# dd.condition_description('new?')
# dd.condition_id(123)
# dd.country('USA')
# dd.condition_id(123)
# dd.cross_border_trade('USD')
# dd.currency('USD')
# dd.description('words and words')
# dd.disable_buyer_requirements(True)
# dd.made_for_otlet_comparison_price(5.95)
# dd.minimum_advertised_price(.99)
# dd.minimum_advertised_price_exposure(9.99)
# dd.original_retail_price(100)
# dd.sold_off_ebay(True)
# dd.sold_on_ebay(False)
# dd.dispatch_time_max(4)
# dd.ebay_now_eligible(False)
# dd.get_it_fast(False)
# dd.hit_counter('BasicStyle')
# dd.include_recommendations(False)
# dd.inventory_tracking_method('ItemID')

# ## doesn't work like it's supposed to,
# dd.name_value_list_name('names name names')
# dd.name_value_list_value('values value vslues')
# dd.name_value_list_name('more names')
# dd.name_value_list_value('more values')


# pprint(dd.item)



# 'Item', 'ApplicationData', 'my sku',
#           'AutoPay', True,
#           'BestOfferDetails', 'BestOfferEnabled', False,
#           'BuyerRequirementDetails', 'LinkedPayPalAccount', True,
#                                       'MaximumBuyerPolicyViolations', 'Count', 3,
#                                                                        'Period', 45,
#                                       'MaximumItemRequirements', 'MaximumItemCount', 5,
#                                       'MaximumUnpaidItemStrikesInfo', 'Count', 9,
#                                                                        'Period', 'Days_40',
#                                       'MinimumFeedbackScore', -2,
#                                       'ShipToRegistrationCountry', True,
#                                       'VerifiedUserRequirements', 'MinimumFeedbackScore', 4,
#                                                                    'VerifiedUser', True,
#           'CategoryBasedAttributesPrefill', True,
#           'CategoryMappingAllowed', False,
#           'ConditionDescription', 'new?',
#           'ConditionID', 'USD',
#           'Country', 'USA',
#           'Description', 'words and words',
#           'DisableBuyerRequirements', True,
#           'DispatchTimeMax', 4,
#           'GetItFast', False,
#           'HitCounter', 'BasicStyle',
#           'IncludeRecommendations', False,
#           'InventoryTrackingMethod', 'ItemID',
#           'ItemSpecifics', 'NameValueList', 'Name', 'more names',
#                                               'Value', 'more values',
#           'eBayNowEligible', False

# Compilation finished at Wed Jul 16 22,24,56
