import pyautogui
import os, time, random
import requests
# from bs4 import Beautifulsoup
# import pandas as pd 
# import urllib.reququest

# list to store the scrapped data 
authors = []
quoates = []
url = ""

# Opens messaging application and clicks new message 
# i tried simulating many ways but it was not good, this is not the best but works the best right now

def new_message():#only way i could really open new message everytime with no error
    os.system("open -a Messages")
    time.sleep(1)
    pyautogui.rightClick(x=145, y=7)
    time.sleep(.5)
    pyautogui.rightClick(x=145, y=139)
new_message()
# Simulate pressing the Command + N keys to create a new message
# pyautogui.hotkey('command', 'n') # a method i tried but does not always work
# time.sleep(0.5) 

# The message you want to send
mess = "what's up "


Preset_messages= ["Good morning parents", "Good morning btother", "how has everything been"
  "hi cousins", "wha's up man, how's your week been", "what's up brodie, how u doing", "NEOMIE",]




quote = Preset_messages[random.randint(0,len(Preset_messages)-1)] #randomizes the messages

# The recipient's phone number or email address
recipient = '2025566065' 

# Type the recipient's phone number or email address
pyautogui.typewrite(recipient)
time.sleep(0.5)

# Press the Enter key to confirm the recipient
pyautogui.press('enter')
time.sleep(1)

# Press the Tab key to navigate to the message input field
pyautogui.press('tab')      
time.sleep(1)

# Type the message
pyautogui.typewrite(mess)
time.sleep(0.5)

# Press the Enter key to send the message
pyautogui.press('enter')
