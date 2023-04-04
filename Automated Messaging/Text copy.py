import os, time, random
from pynput import keyboard
from pynput.keyboard import Key,Controller
from py_imessage import imessage
from py_imessage import db_conn

# Opens messaging application 
os.system("open -a Messages")

time.sleep(2)
Preset_messages= ["Good morning parents", "Good morning btother", "how has everything been"
  "hi cousins", "wha's up man, how's your week been", "what's up brodie, how u doing", "NEOMIE",]

quote = Preset_messages[random.randint(0,len(Preset_messages)-1)]

# Connecting to iMessage
# connect = imessage.Connection()

# The phone number or email of the recipient
to = '8047210181'

# keyboard = Controller()
# keyboard.type(quote)
# time.sleep(1)

# The message you want to send
message = ""
# time.sleep(1)

# Send the message using iMessage

imessage.send(to,message)
keyboard = Controller()
keyboard.type("yo")
time.sleep(1)
keyboard.press(Key.enter)

# keyboard.press(Key.enter)
# connect.send_message(quote, to)
