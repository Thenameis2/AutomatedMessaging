import pyautogui
import os, time, random

os.system("open -a Messages")

Preset_messages= ["Good morning parents", "Good morning btother", "how has everything been"
  "hi cousins", "wha's up man, how's your week been", "what's up brodie, how u doing", "NEOMIE",]


quote = Preset_messages[random.randint(0,len(Preset_messages)-1)]

pyautogui.hotkey('command', 'n') # a method i tried but does not always work
# time.sleep(0.5) 