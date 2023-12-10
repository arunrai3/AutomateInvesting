#-------------
#main.py
#-------------

import time
from datetime import datetime as datetime2
import datetime
import pytz
import check_market_status
from handling_tokens import access_token
from trades import logic_for_trading
from texting import texting_app

wait_until_tomorrow = "N"
stocks_to_buy = ["TSLA", "AAPL", "AMZN", "GOOG", "META", "MSFT", "SPY"]

#change this number to what stock you want to start on
current_stock_index = 0

while True:

    pacific = pytz.timezone('US/Pacific')    
    current_time_pacific = datetime2.now(pacific)
    military_time = current_time_pacific.strftime('%H:%M')    
    print("Current Pacific Time (Military Format):", military_time)

    status = check_market_status.getIfMakretOpen()
    
    

    if status != "error" and military_time == '08:30' and wait_until_tomorrow == "N":
       wait_until_tomorrow = "Y"       
       
       
       refresh_token = access_token.get_refresh_token_text_file()
       access_token = access_token.getting_access_token_every_30(refresh_token)
       
       stock_to_buy = stocks_to_buy[current_stock_index]
       statuscode = logic_for_trading.handleTradeLogic(stock_to_buy, access_token)
       current_stock_index = (current_stock_index + 1) % len(stocks_to_buy)
       
       

       #send the sms message
       texting_app.sendingUpdateText(statuscode, stock_to_buy)
       
    
    if military_time == "09:00" and wait_until_tomorrow == "Y":
      wait_until_tomorrow = "N"

    time.sleep(5)


