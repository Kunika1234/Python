import streamlit as st
import pywhatkit as kit
import datetime

st.set_page_config(page_title="WhatsApp Message Sender", layout="centered")

st.title("📲 Send WhatsApp Message Automatically")

phone_no = st.text_input("Enter phone number (with country code)", "+91")
message = st.text_area("Enter the message to send")
delay_minutes = st.slider("Send message after how many minutes?", 1, 10, 1)

if st.button("Send Message"):
    if phone_no and message:
        now = datetime.datetime.now()
        send_hour = now.hour
        send_minute = now.minute + delay_minutes

        try:
            kit.sendwhatmsg(
                phone_no=phone_no,
                message=message,
                time_hour=send_hour,
                time_min=send_minute,
                wait_time=15,
                tab_close=True,
                close_time=5
            )
            st.success(f"Message will be sent at {send_hour}:{send_minute}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both phone number and message.")