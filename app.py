
import streamlit as st
from PIL import Image
import pandas as pd

# App branding
st.set_page_config(page_title="BannerGen WebApp", page_icon="🎨", layout="wide")

st.markdown(
    """
    <style>
    body {font-family: 'Lato', 'Roboto', sans-serif;}
    .main {background: linear-gradient(to bottom right, #1E3A8A, #F97316); color: white;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎨 Banner Generator")
st.caption("Create custom banners using your images & Excel content.")

# Login / Signup section with dummy inputs
with st.expander("👤 Login / Signup"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login / Signup"):
        st.success(f"Welcome, {email}!")

# Banner size selection
template_sizes = [
    "120x600", "160x600", "180x150", "200x100", "200x200", "240x400", "250x150",
    "250x250", "300x250", "300x600", "300x1050", "320x50", "320x100", "336x280",
    "468x60", "550x120", "600x120", "728x90", "850x225", "970x90", "970x250"
]

st.subheader("📐 Choose a Banner Size")

cols = st.columns(5)
selected_size = None
for i, size in enumerate(template_sizes):
    if cols[i % 5].button(size):
        selected_size = size
        st.session_state['selected_size'] = size

if 'selected_size' in st.session_state:
    st.success(f"Selected Banner Size: {st.session_state['selected_size']}")

# Image & Excel upload
st.subheader("📁 Upload Image and Excel")

image_file = st.file_uploader("Upload Banner Image", type=["png", "jpg", "jpeg"])
excel_file = st.file_uploader("Upload Excel (.xlsx)", type="xlsx")

# Preview
if image_file is not None:
    st.image(Image.open(image_file), caption="Uploaded Image", use_column_width=True)

# Generate banner button
if st.button("✨ Generate Banner"):
    if image_file and 'selected_size' in st.session_state:
        st.success(f"Banner generated with size {st.session_state['selected_size']}!")
    else:
        st.error("Please upload an image and select a banner size.")

# Footer
st.markdown("---")
st.caption("BannerGen WebApp © 2025 | Powered by Streamlit")
