#-------------
#main.py
#-------------

import time
from datetime import datetime as datetime2
import datetime
import pytz
import check_market_status
from handling_tokens import refresh_token
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
       
       with open(r'Z:\automate_investing\handling_tokens\refresh_token_date.txt', 'r') as file:
           refresh_token_date = file.read()       
       refresh_token_date_object = datetime2.strptime(refresh_token_date, "%Y-%m-%d").date()

       today_date = datetime.date.today()
       ten_days_ago = today_date - datetime.timedelta(days=10)
       
       
       if ten_days_ago < refresh_token_date_object:
           print("Refresh token is valid. Now getting the Access token")
           refresh_token = access_token.get_refresh_token_text_file()
           access_token = access_token.getting_access_token_every_30(refresh_token)
           
       elif ten_days_ago >= refresh_token_date_object:
           print("Refresh token is invaid. Getting a new refresh token first")
           refresh_token.open_browser_and_get_tokens()
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


