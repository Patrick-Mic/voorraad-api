from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

# Product (object) gemaakt om te versturen
class Product(BaseModel):
    naam: str
    aantal: int = 1 # hele getallen, als niks is aangegeven dan 1.
    houdbaar_tot: date | None = None 

app = FastAPI()
voorraad: list[Product] = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hallo/{naam}")
def hallo(naam: str):
    return {"bericht": f"Hallo {naam}!"}

@app.post("/producten")
def voeg_toe(product: Product):
    voorraad.append(product)
    return {"bericht": f"{product.naam} toegevoegd", "totaal": len(voorraad)}

@app.get("/producten")
def get_products():
    return voorraad

