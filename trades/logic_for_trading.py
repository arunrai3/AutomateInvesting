from trades import td_order_send
from trades import get_account_balances
from trades import get_current_price

#-----------------
#logic for trading
#-----------------


def handleTradeLogic(stock_to_buy, access_token):
  account_balance = get_account_balances.getAccountBalances(access_token)
  stocks_to_buy_price = get_current_price.getCurrentPrice(stock_to_buy)
  
  if account_balance > stocks_to_buy_price:     
     statuscode = td_order_send.sendTrade(stock_to_buy,access_token)
     return statuscode
  else:
     return "Error: Not enough cash to buy Stock: " + stock_to_buy
