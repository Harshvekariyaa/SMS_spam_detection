# Image OCR Tool

This project provides two ways to extract text from images using OCR (Optical Character Recognition):

1. A desktop GUI script (`image_ocr.py`)
2. A web app using Streamlit (`streamlit_ocr.py`)

## Prerequisites

- Python 3.x
- Tesseract OCR engine installed on your system.

### Installing Tesseract

- On Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
- On macOS: `brew install tesseract`
- On Linux: `sudo apt-get install tesseract-ocr`

## Installation

1. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Desktop GUI Version

Run the script:
```
python image_ocr.py
```

A file dialog will open. Select an image file (PNG, JPG, JPEG, BMP, TIFF, GIF). The extracted text will be displayed in a message box.

### Web App Version

Run the Streamlit app:
```
streamlit run streamlit_ocr.py
```

Open the provided URL in your browser. Upload an image file, and the extracted text will be displayed automatically.

## Troubleshooting

- If no text is extracted, ensure the image has clear, readable text.
- Make sure Tesseract is properly installed and in your PATH.