# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from ebaysdk.trading import Connection

api = Connection(config_file = '/itemhut/pyebay/ebay.yaml')

class Universal(object):
    def get_pagination(self, entries_per_page, page_number = 1):
        self.query['Pagination'] = {}
        self.query['Pagination'].update({'PageNumber' : page_number})
        self.query['Pagination'].update({'EntriesPerPage' : entries_per_page})
        return self

    def sorting_order(self, sort_order):
        if sort_order in ['Ascending', 'Descending']:
            self.query['SortingOrder'] = sort_order
        return self


class StandardInputFields(Universal):
    def detail_level(self): ## ToDo DetailLevel
        pass

    def error_language(self): ## ToDo ErrorLanguage
        pass

    def message_id(self): ## ToDo MessageID
        pass

    def output_selector(self): ## ToDo OutputSelector
        pass

    def version(self): ## ToDo Version
        pass

    def warning_level(self): ## ToDo WarningLevel
        pass
    

class CommentQuery(StandardInputFields):
    def comment_type(self, t):
        if t in ['Negative', 'Neutral', 'Positive', 'Withdrawn']:
            self.query['CommentType'] = t
        return self

    def feedback_id(self, f_id):
        self.query['FeedbackID'] = f_id
    return self

    def feedback_type(self, f_type):
        if f_type in ['FeedbackLeft', 
                      'FeedbackReceived', 
                      'FeedbackReceivedAsBuyer', 
                      'FeedbackReceivedAsSeller']:
            self.query['FeedbackType'] = f_type
        return self

    def item_id(self, item_id): 
        if len(item_id) <= 19:
            self.query['ItemId'] = item_id
    return self

    def order_line_item_id(self, oli_id):
        if len(oli_id) <= 100:
            self.query['OrderLineItemID'] = oli_id
        return self

    def transaction_id(self, t_id):
        if len(t_id):
            self.query['TransactionID'] = t_id
        return self

    def user_id(self, user_id):
        self.query['UserID'] = user_id
    return self

