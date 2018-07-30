from binance.client import Client
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
order = client.create_order(
     symbol='BNBBTC',
     side=Client.SIDE_BUY,
     type=Client.ORDER_TYPE_MARKET,
     quantity=100)


