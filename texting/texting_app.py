from twilio.rest import Client

def sendingUpdateText(status, stock):
  
  account_sid = 'ACd05c964d75780ec64d289903c68e197a'
  auth_token = '125c3730fd4fffbcc2d11738145f4f69'
  
  client = Client(account_sid, auth_token)
  
  message = client.messages.create(
      body="Purchased Stock: " + stock + "\nStatus Code: " + str(status),
      from_='+18556122462',  # Your Twilio phone number
      to='+15307134629'      # Recipient's phone number
  )
  
  print(f"Message sent with SID: {message.sid}")