from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates  # ajouté

import shutil
import os

app = FastAPI()

# Monte un dossier "static" pour servir les images, CSS, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Correction ici : le dossier templates doit être "templates" et non "static"
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/submit")
async def submit_form(
    nom: str = Form(...),
    email: str = Form(...),
    date: str = Form(...),
    message: str = Form(""),
    photo: UploadFile = File(...)
):
    print(f"Nom: {nom}, Email: {email}, Date: {date}, Message: {message}, Photo: {photo.filename}")

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, photo.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(photo.file, buffer)

    return RedirectResponse(url="/", status_code=303)
