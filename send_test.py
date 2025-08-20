# send_test.py
import os
from twilio.rest import Client
TWILIO_ACCOUNT_SID = os.getenv("account_sid")
TWILIO_AUTH_TOKEN = os.getenv("auth_token")

# Replace with your Twilio Account SID and Auth Token
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello Noah! 🚀 This is your first WhatsApp message from Twilio Sandbox.",
    from_="whatsapp:+14155238886",   # Twilio sandbox number
    to="whatsapp:+254719531290"      # Your number in E.164 format
)

print("Message SID:", message.sid)