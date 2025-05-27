import pywhatkit

# Replace with the recipient's phone number and your message
phone_number = "+94762219150"  # Use country code, e.g., +94 for Sri Lanka
message = "Hello from Python!"

# Send message instantly (opens WhatsApp Web, you must scan QR code once)
pywhatkit.sendwhatmsg_instantly(phone_number, message)