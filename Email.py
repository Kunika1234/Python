import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="📧 Gmail Email Sender", layout="centered")
st.title("📧 Send Email via Gmail (Python + Streamlit)")

# Input fields
sender_email = st.text_input("Your Gmail address", placeholder="you@gmail.com")
app_password = st.text_input("Your Gmail App Password", type="password")
receiver_email = st.text_input("Recipient's Email", placeholder="recipient@example.com")
subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

if st.button("Send Email"):
    if not all([sender_email, app_password, receiver_email, subject, body]):
        st.warning("Please fill in all fields.")
    else:
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, app_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")