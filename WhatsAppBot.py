import pywhatkit as kit
import pyautogui
import time

# Replace with your contact's phone number (with country code)
phone_number = "+91XXXXXXXXXX"

# Your message
message = "Hello! This is a message sent by my Python WhatsApp bot. 😊"

# Send message at a scheduled time (HH, MM in 24-hour format)
hour = 15  # 3 PM
minute = 30

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)

# Wait for the message box to open (give some buffer time)
time.sleep(15)

# Optional: press "Enter" if not auto-sent
pyautogui.press("enter")

print("✅ Message sent successfully!")
