import requests

#-------------
#td_order_send
#-------------


def sendTrade(stock_to_buy, access_token):
  header = {'Authorization': "Bearer {}".format(access_token),
            "Content-Type":"application/json"}
  endpoint = r"https://api.tdameritrade.com/v1/accounts//orders"
  
  payload = {"orderType": "MARKET",
             "session": "NORMAL",
             "duration": "DAY",
             "orderStrategyType": "SINGLE",
             "orderLegCollection": [{"instruction": "BUY","quantity": 1,"instrument":{"symbol": stock_to_buy,"assetType": "EQUITY"}}]}
  
  content = requests.post(url = endpoint,json = payload, headers = header)
  code = content.status_code
  print(code)
  return code