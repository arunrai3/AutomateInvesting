import yfinance as yf

#-------------------
#get_current_price
#-------------------

def getCurrentPrice(stock_to_buy):

  ticker = yf.Ticker(stock_to_buy)
  
  current_price = ticker.history(period="1d")["Close"].iloc[0]
  
  print(f"The current price of " + stock_to_buy + " is " + str(current_price))
  return current_price  