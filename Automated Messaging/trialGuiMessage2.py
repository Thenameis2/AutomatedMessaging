import pyautogui
import os, time, random

# Wait for the Messages app to open
os.system("open -a Messages")
time.sleep(2)

# Click the "New Message" button
new_message_x, new_message_y = pyautogui.locateCenterOnScreen('new.png')
pyautogui.click(new_message_x, new_message_y)

# Wait for the "To:" field to appear
time.sleep(2)

# Type the contact name
pyautogui.typewrite('Maya')
time.sleep(1)

# Press the down arrow key to select the contact from the list
pyautogui.press('down')
time.sleep(1)

# Press Enter to select the contact
pyautogui.press('enter')
time.sleep(1)

# Wait for the message input field to appear
time.sleep(2)

# Type the message
pyautogui.typewrite('hello, this is a test message')
time.sleep(1)

# Press the Enter key to send the message
pyautogui.press('enter')
