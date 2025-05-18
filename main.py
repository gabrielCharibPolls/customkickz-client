from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/main.html")
def serve_main():
    return FileResponse("static/main.html")
