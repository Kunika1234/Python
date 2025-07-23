import streamlit as st
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get credentials from environment
account_sid = os.getenv("xxxxxxxxxxxxxxxxxxxxxx")
auth_token = os.getenv("xxxxxxxxxxxxxxxxxxxxxxx")
twilio_whatsapp_number = os.getenv("xxxxxxxxxx")

# Debug print to verify loading
st.write("Loaded SID:", account_sid)
st.write("Loaded Token:", auth_token[:4] + "..." if auth_token else "Not loaded")
st.write("Loaded FROM number:", twilio_whatsapp_number)

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Streamlit UI
st.title("📲 Send WhatsApp Message using Twilio")

to_number = st.text_input("Recipient WhatsApp Number (with country code)", placeholder="+91xxxxxxxxxx")
message_body = st.text_area("Enter your message")

if st.button("Send WhatsApp Message"):
    if to_number and message_body:
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_whatsapp_number,
                to="whatsapp:" + to_number
            )
            st.success(f"✅ Message sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Failed to send: {e}")
    else:
        st.warning("⚠️ Please enter both recipient number and message.")
