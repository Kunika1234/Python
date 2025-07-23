import streamlit as st
from twilio.rest import Client

# Streamlit page setup
st.set_page_config(page_title="📞 Twilio Call App", layout="centered")
st.title("📞 Twilio Voice Call Trigger")
st.write("Enter a number below and click the button to make a test call.")

to_number = st.text_input("📱 Enter the recipient phone number (with country code)", "+91XXXXXXXXXX")

account_sid = 'xxxxxxxxxxxxx'
auth_token =  'xxxxxxxxxxxxx'
from_number = 'xxxxxxxxxxxxx'  

if st.button("📞 Make the Call"):
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml='<Response><Say>Hello! This is a test call from Python using Twilio.</Say></Response>'
        )
        st.success(f"✅ Call initiated! Call SID: {call.sid}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
