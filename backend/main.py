from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path
from PyPDF2 import PdfReader

#nyalain venv: .\venv\Scripts\activate
#jalanin server: uvicorn main:app --reload
#cek di browser: http://127.0.0.1:8000
#upload: http://127.0.0.1:8000/docs

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Hello, Scribsy Backend is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # simpan file ke folder uploads
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ekstrak teks dari PDF
    reader = PdfReader(str(file_path))
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return {
        "filename": file.filename,
        "text_preview": text[:500] if text else "No text found in PDF"
    }