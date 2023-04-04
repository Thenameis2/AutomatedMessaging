# the objecive of this application  is to make an automated messaging app
# i have a tendency to foget to tect back
# people to text
# 1. Mother 
# 2. Father
# 3. brother 
# 4. cousins 
# 5. bestfrined 
# 6. group chats 
# 7. FRiends 
# The automated messgaes will happen once a week for parents and brother, once a day
# have an api of postive quotes and mesages and have it loop thorugh the api and send them

from twilio.rest import Client
import schedule
import random
import time

# 1. A collection of presest messages
Preset_messages= ["Good morning parents", "Good morning btother", "how has everything been",
 "hi cousins", "wha's up man, how's your week been", "what's up brodie, how u doing", "NEOMIE",]
Preset_messages = ["Hey vic"]
# 2. send message using api

def send_messages(quote):
    account = "AC15b8450d412b4a4128135b7edd65f86e"
    token = "0cd5daf62787c8164734accf3ebb5d7f"
    client = Client(account,token)
    quote = Preset_messages[random.randint(0,len(Preset_messages)-1)]
    client.messages.create(
        to="+12025566065",
        from_="+18449384377",
        body= quote
            
            )
# 3. scheduling messages using schedule library
schedule.every(1).minutes.do(send_messages,Preset_messages)

while True:
    schedule.run_pending()
    time.sleep(2)