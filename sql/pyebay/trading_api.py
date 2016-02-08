from ebaysdk.trading import Connection as Trading

api = Trading(config_file='ebay.yaml')

# feedback = api.execute('GetFeedback', {'UserId': 'genuvape'}).response_json()
# print(feedback)

orders = api.execute('GetOrders', {'NumberOfDays': 30}).response_json()
print(orders)

