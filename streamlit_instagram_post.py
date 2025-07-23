import streamlit as st
from instagrapi import Client
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="Instagram Auto Poster", page_icon="📸")

st.title("📸 Instagram Auto Poster")

# Step 1: Get user credentials
username = st.text_input("Instagram Username")
password = st.text_input("Instagram Password", type="password")

# Step 2: Upload photo and caption
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
caption = st.text_area("Enter a caption for your post")

# Step 3: Post to Instagram
if st.button("Post to Instagram"):
    if not all([username, password, uploaded_file, caption]):
        st.error("❗Please fill in all fields.")
    else:
        with st.spinner("Logging in and uploading your photo..."):
            try:
                cl = Client()
                cl.login(username, password)

                with NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                    tmp.write(uploaded_file.getvalue())
                    temp_path = tmp.name

                cl.photo_upload(path=temp_path, caption=caption)
                st.success("✅ Post uploaded successfully!")

            except Exception as e:
                st.error(f"🚫 Failed to upload: {e}")
