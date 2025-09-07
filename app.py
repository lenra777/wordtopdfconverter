from flask import Flask, render_template, request, send_file
import pypandoc, os, uuid
from pdf2docx import Converter

app = Flask(__name__)

UPLOAD_FOLDER = "generated_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# DOCX to PDF
def docx_to_pdf(docx_file, pdf_file):
    pypandoc.convert_file(docx_file, "pdf", outputfile=pdf_file, extra_args=["--standalone"])
    return pdf_file

# PDF to DOCX
def pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    return docx_file

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    pdf_file = converted_docx = None

    if request.method == "POST":
        # Word to PDF
        if "word_file" in request.files:
            uploaded = request.files["word_file"]
            if uploaded.filename.endswith(".docx"):
                unique_id = str(uuid.uuid4())
                docx_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.docx")
                pdf_file = os.path.join(UPLOAD_FOLDER, f"{unique_id}.pdf")
                uploaded.save(docx_path)

                docx_to_pdf(docx_path, pdf_file)

        # PDF to Word
        elif "pdf_file" in request.files:
            uploaded = request.files["pdf_file"]
            if uploaded.filename.endswith(".pdf"):
                unique_id = str(uuid.uuid4())
                pdf_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.pdf")
                converted_docx = os.path.join(UPLOAD_FOLDER, f"{unique_id}.docx")
                uploaded.save(pdf_path)

                pdf_to_docx(pdf_path, converted_docx)

        return render_template("index.html", pdf_file=pdf_file, converted_docx=converted_docx)

    return render_template("index.html", pdf_file=None, converted_docx=None)

@app.route("/download/<path:filename>")
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#if __name__ == "__main__":
    #app.run(debug=True)
