from twilio.rest import Client

def sendingUpdateText(status, stock):
  
  account_sid = ''
  auth_token = ''
  
  client = Client(account_sid, auth_token)
  
  message = client.messages.create(
      body="Purchased Stock: " + stock + "\nStatus Code: " + str(status),
      from_='+',  # Your Twilio phone number
      to='+'      # Recipient's phone number
  )
  
  print(f"Message sent with SID: {message.sid}")