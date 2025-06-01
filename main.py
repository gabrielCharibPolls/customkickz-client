from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

app = FastAPI()

# Monte un dossier "static" pour servir les images, CSS, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates si tu veux utiliser Jinja (optionnel)
templates = Jinja2Templates(directory="static")

# Route racine qui renvoie ta page HTML (ici on utilise un template Jinja, tu peux aussi envoyer un fichier statique)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# Traitement du formulaire POST pour la réservation
@app.post("/submit")
async def submit_form(
    nom: str = Form(...),
    email: str = Form(...),
    date: str = Form(...),
    message: str = Form(""),
    photo: UploadFile = File(...)
):
    
    print(f"Nom: {nom}, Email: {email}, Date: {date}, Message: {message}, Photo: {photo.filename}")

    # Sauvegarde fichier uploadé dans dossier "uploads"
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, photo.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(photo.file, buffer)

    # Ici, tu peux ajouter la logique d'enregistrement en base, envoi email, etc.
    # Pour l'exemple, on redirige vers la page d'accueil après soumission
    return RedirectResponse(url="/", status_code=303)
