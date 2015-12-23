#!/usr/bin/python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def get_pagination(entries_per_page, page_number):
    pag = {}
    pag.setdefault('Pagination', {})
    pag['Pagination'].setdefault('PageNumber', page_number)
    pag['Pagination'].setdefault('EntriesPerPage', entries_per_page)
    return pag

def sorting_order(sort_order):
    sorder = {}
    if sort_order in ['Ascending', 'Descending']:
        sorder.setdefault('SortingOrder', sort_order)
    return sorder

# def order_id_array(self): ## ToDo OrderIDArray
#     pass 

def by_status(order_status):
    ostatus = {}
    if order_status in ['Active', 'Completed', 'Cancelled', 'Inactive']:
        ostatus.setdefault('Order_status', order_status)
    return ostatus

# def detail_level(self): ## ToDo DetailLevel
#     pass

# def error_language(self): ## ToDo ErrorLanguage
#     pass

# def message_id(self): ## ToDo MessageID
#     pass

# def output_selector(self): ## ToDo OutputSelector
#     pass

# def version(self): ## ToDo Version
#     pass

# def warning_level(self): ## ToDo WarningLevel
#     pass
