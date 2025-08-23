from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Scribsy Backend is running"}

#cek di browser: http://127.0.0.1:8000
