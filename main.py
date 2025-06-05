from fastapi import FastAPI
import os

app = FastAPI()

# Serve le dossier static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Accès direct à main.html via /
@app.get("/")
def read_root():
    return {"message": "Hello from Railway"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
