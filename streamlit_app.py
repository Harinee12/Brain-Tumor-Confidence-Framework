import streamlit as st
from PIL import Image

st.title("Brain Tumor Classification")

st.write("Upload an MRI image to classify the tumor.")

uploaded_file = st.file_uploader("Choose MRI Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Prediction will appear here.")
