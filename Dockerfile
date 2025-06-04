# Étape 1 : image de base avec Python
FROM python:3.11-slim

# Étape 2 : définit le dossier de travail
WORKDIR /app

# Étape 3 : copie les fichiers
COPY . .

# Étape 4 : installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : commande à exécuter au démarrage du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]