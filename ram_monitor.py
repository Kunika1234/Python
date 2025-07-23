import streamlit as st
import psutil
import time

st.set_page_config(page_title="RAM Usage Monitor", layout="centered")

st.title("💻 Real-Time RAM Usage Monitor")

placeholder = st.empty()

while True:
    mem = psutil.virtual_memory()

    with placeholder.container():
        st.metric("Total RAM", f"{mem.total / (1024 ** 3):.2f} GB")
        st.metric("Available RAM", f"{mem.available / (1024 ** 3):.2f} GB")
        st.metric("Used RAM", f"{mem.used / (1024 ** 3):.2f} GB")
        st.metric("RAM Usage", f"{mem.percent} %")

    time.sleep(1)  