# Word ↔ PDF Converter (Flask)

A simple web application built with **Flask** that allows users to:
- Convert **Word (DOCX) → PDF**
- Convert **PDF → Word (DOCX)**

Deployed using **Render (Free Tier)**.

---

## 🚀 Features
- Upload a Word document and download it as PDF  
- Upload a PDF file and download it as Word (DOCX)  
- Clean and responsive UI (Bootstrap 5)  
- Lightweight Flask backend with `python-docx`, `reportlab`, and `pypandoc`

---

## 🛠 Tech Stack
- **Backend**: Flask (Python)  
- **Frontend**: HTML + Bootstrap 5  
- **Libraries**:  
  - `python-docx` – Word handling  
  - `reportlab` – PDF generation  
  - `pypandoc` – Format conversion  
  - `gunicorn` – Production server  

---

## 📦 Installation (Local Development)
1. Clone this repository:
   ```bash
   git clone https://github.com/lenra777/wordtopdfconverter.git
   cd word-pdf-converter

2. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

3. Install dependencies:
    pip install -r requirements.txt

4. Run the Flask app:
    python app.py

5. App will run at:
    http://127.0.0.1:5000