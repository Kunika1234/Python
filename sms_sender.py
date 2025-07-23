import streamlit as st
from twilio.rest import Client

# Twilio credentials (replace with your actual values or use environment variables)
ACCOUNT_SID = 'xxxxxxxxxxxxxxxxxxxx'
AUTH_TOKEN = 'xxxxxxxxxxxxxxxxxxxx'
TWILIO_PHONE = 'xxxxxxxxxx'  

client = Client(ACCOUNT_SID, AUTH_TOKEN)

st.title("📲 SMS Sender via Streamlit")

# Input fields
to_number = st.text_input("Recipient Phone Number (with country code)", "+91")
message_body = st.text_area("Message", "Type your message here...")

if st.button("Send SMS"):
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=to_number
        )
        st.success(f"✅ Message sent! SID: {message.sid}")
    except Exception as e:
        st.error(f"❌ Failed to send message: {e}")