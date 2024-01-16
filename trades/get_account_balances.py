import requests

#--------------------
#get_account_balances
#--------------------

def getAccountBalances(access_token):
  header = {'Authorization': "Bearer {}".format(access_token),
            "Content-Type":"application/json"}
  endpoint = r"https://api.tdameritrade.com/v1/accounts/"
  

  
  content = requests.get(url = endpoint, headers = header)
  
  decoded_content = content.json()
  print("------------------------")
  print("Here is the account information")
  print("------------------------")
  print(decoded_content)
  print("------------------------")
  print("")
  print("------------------------")
  cash = decoded_content['securitiesAccount']['currentBalances']['cashBalance']
  print(cash)
  return cash
  
