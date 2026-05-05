# 📷 Image to Text + 📧 SMS Spam Detection App

This project is a web application built using **Streamlit** that performs:

* 📷 Image to Text (OCR)
* 📧 SMS/Email Spam Detection

It allows users to upload an image, extract text from it, and then check whether the extracted (or manually entered) text is spam or not.

---

## 🚀 Features

* Upload image (`.png`, `.jpg`, `.jpeg`)
* Extract text using OCR (EasyOCR)
* Automatically use extracted text for spam detection
* Manual text input option
* Classifies message as:

  * 🚨 Spam
  * ✅ Not Spam

---

## 🧠 How it works

1. Image is uploaded by the user
2. OCR extracts text using EasyOCR
3. Text is transformed using TF-IDF Vectorizer
4. Pre-trained ML model predicts spam or not

---

## 📂 Project Structure

```
├── sms_spam.py
├── requirements.txt
├── Sms_spam_detection_model.pkl
├── tfidf_vectorizer.pkl
└── README.md
```

---


## 📊 Dataset Information

This model is trained on an SMS Spam dataset.

👉 You can either:

* Use your own dataset
* Or view/download a public dataset like the **SMS Spam Collection Dataset**

The dataset typically contains:

* `label` → spam / ham
* `message` → actual text

---

## ✍️ Usage Instructions

* Upload an image to extract text
* OR manually enter text in the input box
* Click **"Check Spam"**
* View the result instantly

---

## ⚠️ Notes

* Make sure model files are present:

  * `Sms_spam_detection_model.pkl`
  * `tfidf_vectorizer.pkl`
* EasyOCR may take a few seconds to load initially
* Internet connection may be required for first-time OCR model download

---

## 🛠️ Tech Stack

* Streamlit
* EasyOCR
* Scikit-learn
* NumPy
* PyTorch

---

## 🙌 Future Improvements

* Support multiple languages in OCR
* Add confidence score for predictions
* Improve UI/UX
* Add real-time API support

---

## 📜 License

This project is for educational purposes.

---

## 👤 Author

Harsh

---
