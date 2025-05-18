from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve le dossier static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Accès direct à main.html via /
@app.get("/")
def root():
    return FileResponse("static/main.html")
