#td order sending
from splinter import Browser
import time
import urllib
import urllib.parse
import requests
import json
import dateutil.parser
from datetime import datetime, timedelta
from datetime import timedelta
from pytz import timezone
import os


import datetime


def unix_time_millis(dt):
  epoch = datetime.datetime.utcfromtimestamp(0)
  return (dt - epoch).total_seconds() * 1000.0 

#-----------------------------------------------------------------------------------
#still need to add the date part to this code for making sure refresh_token is valid
#-----------------------------------------------------------------------------------

    
def get_refresh_token_text_file():

    script_dir = os.path.dirname(os.path.abspath(__file__))    
    file_path = os.path.join(script_dir, 'refresh_token.txt')

    with open(file_path, "r") as f:
        refresh_token = f.read().strip()
    return refresh_token


    

def getting_access_token_every_30(refresh_token):
    url = r'https://api.tdameritrade.com/v1/oauth2/token'
    headers = {'Content-Type':"application/x-www-form-urlencoded"}
    payload = {'grant_type':'refresh_token',
               'refresh_token' : refresh_token,
               'client_id':""}

    authreply = requests.post(url, headers = headers, data = payload)

    decoded_content = authreply.json()
    access_token = decoded_content['access_token']
    print("")
    print("")
    print("HERE IS ACCESS TOKEN")
    print("")
    print(access_token)
    print("")
    print("")
    print("Sleeping for 5 seconds")
    print("")
    print("")
    current_time = datetime.datetime.now()
    print("Current time:", current_time)
    print("")
    print("")
    



    script_dir = os.path.dirname(os.path.abspath(__file__))    
    file_path = os.path.join(script_dir, 'access_token.txt')

    
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w") as f:
        f.write(access_token) 

    time.sleep(5)
    return access_token


def run_access_token_refresh(refresh_token):
    while True:
        getting_access_token_every_30(refresh_token)
        time.sleep(20 * 60) 

        