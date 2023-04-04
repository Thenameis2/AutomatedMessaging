import pyautogui
import os, time, random

# Opens messaging application 
os.system("open -a Messages")
time.sleep(2)

# The message you want to send
Preset_messages= ["Good morning parents", "Good morning btother", "how has everything been"
  "hi cousins", "wha's up man, how's your week been", "what's up brodie, how u doing", "NEOMIE",]

quote = Preset_messages[random.randint(0,len(Preset_messages)-1)] #randomizes the messages

# The recipient's phone number or email address
recipient = '2025566065' 


# Activate the Messages app window
# pyautogui.hotkey('command', 'tab')
# time.sleep(0.5)

# # Click on the new message button
# new_message_x, new_message_y = pyautogui.locateCenterOnScreen('new.png')
# pyautogui.click(new_message_x, new_message_y)
 # Click the "New Message" button
# new_message_x, new_message_y = pyautogui.locateCenterOnScreen('new.png')
# pyautogui.click(new_message_x, new_message_y)

# new_message_region = pyautogui.locateOnScreen('new.png')
# new_message_x, new_message_y = pyautogui.center(new_message_region)
# pyautogui.click(new_message_x, new_message_y)

# Take a screenshot of the Messages app window
messages_window = pyautogui.screenshot()

# Locate the "New Message" button in the screenshot
new_message_button = pyautogui.locateOnScreen('new.png', grayscale=True)

# Calculate the center point of the "New Message" button
new_message_x, new_message_y = pyautogui.center(new_message_button)

# Click the "New Message" button
pyautogui.click(new_message_x, new_message_y)
# Simulate pressing the Command + N keys to create a new message
pyautogui.hotkey('command', 'n')
time.sleep(0.5) 

# Type the recipient's phone number or email address
pyautogui.typewrite(recipient)
time.sleep(0.5)

# Press the Enter key to confirm the recipient
pyautogui.press('enter')
time.sleep(0.5)

# Click on the message input field
# message_input_x, message_input_y = pyautogui.locateCenterOnScreen(' input.png')
# pyautogui.click(message_input_x, message_input_y)
# Press the Tab key to navigate to the message input field
pyautogui.press('tab')      
time.sleep(0.5)

# Type the message
pyautogui.typewrite(quote)
time.sleep(0.5)

# Press the Enter key to send the message
pyautogui.press('enter')
