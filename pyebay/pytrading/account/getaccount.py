#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection
import sys
sys.path.append("/omark/pyebay/common/")
sys.path.append("/omark/pydb/")
import common
import dbconn

api = Connection(config_file = '/omark/pyebay/ebay.yaml')

def account_entry_sort_type (sort_type):
    st = {}
    if sort_type in ['AccountEntryCreatedTimeAscending',
                     'AccountEntryCreatedTimeDescending',
                     'AccountEntryFeeTypeAscending',
                     'AccountEntryFeeTypeDescending',
                     'AccountEntryItemNumberAscending',
                     'AccountEntryItemNumberDescending',
                     'None']:
        st.setdefault('AccountEntrySortType', sort_type)
        return st

def account_history_selection (selection):
    hs = {}
    if selection in ['BetweenSpecifiedDates',
                     'LastInvoice',
                     'SpecifiedInvoice']:
        hs.setdefault('AccountHistorySelection', selection)
    return hs

def begin_date (date):
    bd = {}
    bd.setdefault('BeginDate', date)
    return bd

def end_date (date):
    ed = {}
    ed.setdefault('EndDate', date)
    return ed

def currency (currency):
    c = {}
    if currency in ['ADP', 'AED', 'AFA', 'ALL', 'AMD', 'ANG', 'AOA',
                    'ARS', 'ATS', 'AUD', 'AWG', 'AZM', 'BAM', 'BBD',
                    'BDT', 'BGL', 'BGN', 'BHD', 'BIF', 'BMD', 'BND',
                    'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYR',
                    'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY',
                    'COP', 'CRC', 'CUP', 'CVE', 'CYP', 'CZK', 'DJF',
                    'DKK', 'DOP', 'DZD', 'ECS', 'ECV', 'EEK', 'EGP',
                    'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL',
                    'GHC', 'GIP', 'GMD', 'GNF', 'GTQ', 'GWP', 'GYD',
                    'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
                    'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY',
                    'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD',
                    'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL',
                    'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGF', 'MKD',
                    'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR',
                    'MWK', 'MXN', 'MXV', 'MYR', 'MZM', 'NAD', 'NGN',
                    'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN',
                    'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'ROL',
                    'RUB', 'RUR', 'RWF', 'SAR', 'SBD', 'SCR', 'SDD',
                    'SEK', 'SGD', 'SHP', 'SIT', 'SKK', 'SLL', 'SOS',
                    'SRG', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS',
                    'TMM', 'TND', 'TOP', 'TPE', 'TRL', 'TTD', 'TWD',
                    'TZS', 'UAH', 'UGX', 'USD', 'USN', 'USS', 'UYU',
                    'UZS', 'VEB', 'VND', 'VUV', 'WST', 'XAF', 'XCD',
                    'XOF', 'XPF', 'YER', 'YUM', 'ZAR', 'ZMK', 'ZWD']:
        c.setdefault('Currency', currency)
    return c

def exclude_balance (tf):
    eb = {}
    if tf in [True, False]:
        eb.setdefault('ExcludeBalance', tf)
    return eb

def exclude_summary (tf):
    es = {}
    if tf in [True, False]:
        es.setdefault('ExcludeSummary', tf)
    return tf

def include_conversion_rate (tf):
    icr = {}
    if tf in [True, False]:
        icr.setdefault('IncludeConversionRate', tf)
    return icr

def invoice_date (date):
    id = {}
    id.setdefault('InvoiceDate', date)
    return id

def item_id (id):
    ii = {}
    ii.setdefault('ItemID', id)
    return ii

### willl create separte paganation file
# def pagination (cnt):
#     ## defaults to 500 per page
#     p = {}
#     if 0 < cnt < 2000:
#         p.setdefault('Pagination', cnt)
#     return p

QUERY = {}


def create_map(*args):
    for i in args:
        QUERY.update(i)

# acs = account_history_selection ('SpecifiedInvoice')
# id = invoice_date('2014-09-01')
# create_map(acs,id)
        
def get_account (QUERY):
    zz = api.execute('GetAccount', QUERY)    
    zz = zz.json()
    dbconn.cur.execute("""INSERT INTO ebay_invoices.json_insert (v)
                          VALUES ($${0}$$);""".format(zz))

get_account(QUERY)

dbconn.conn.commit()
dbconn.cur.close()

print("success")
