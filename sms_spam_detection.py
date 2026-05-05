import streamlit as st
from PIL import Image
import easyocr
import numpy as np
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("Sms_spam_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("📷 Image to Text + 📧 Spam Detector")

# ---------------- OCR SECTION ----------------
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

extracted_text = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)

    reader = easyocr.Reader(['en'])

    with st.spinner("Reading text..."):
        results = reader.readtext(img_array)

    extracted_text = " ".join([res[1] for res in results])

    st.subheader("📄 Extracted Text")
    st.text_area("Result", extracted_text, height=200)

# ---------------- SPAM DETECTION ----------------
st.subheader("📧 Spam Detection")

user_input = st.text_area(
    "Enter Email/Text to Check",
    value=extracted_text,
    height=150
)

if st.button("Check Spam"):
    if user_input.strip() != "":
        vectorized_input = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_input)[0]
        
        if prediction == "spam":
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is NOT Spam")
    else:
        st.warning("Please enter some text first.")