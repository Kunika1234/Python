import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Create Your Own Digital Image", layout="centered")
st.title("🎨 Create Your Own Digital Image")

# --- Inputs ---
text = st.text_input("Enter Text for the Image", "Hello, World!")
font_size = st.slider("Font Size", 10, 100, 40)
bg_color = st.color_picker("Background Color", "#497B89")
text_color = st.color_picker("Text Color", "#FFFFFF")
img_width = st.slider("Image Width", 100, 800, 400)
img_height = st.slider("Image Height", 100, 400, 200)

# --- Image Creation ---
if st.button("Generate Image"):
    image = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(image)

    try:
        # Try to use a better font if available
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback if Arial not available
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    st.image(image, caption="Your Custom Image")

    # Download option
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button("Download Image", byte_im, "custom_image.png", "image/png")
