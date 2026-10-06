from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from database import get_connection, init_db

# Product (object) gemaakt om te versturen
class Product(BaseModel):
    naam: str
    aantal: int = 1 # hele getallen, als niks is aangegeven dan 1.
    houdbaar_tot: date | None = None 

app = FastAPI()
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hallo/{naam}")
def hallo(naam: str):
    return {"bericht": f"Hallo {naam}!"}

@app.post("/producten")
def set_products(product: Product):
    houdbaar = product.houdbaar_tot.isoformat() if product.houdbaar_tot else None

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO producten (naam, aantal, houdbaar_tot) VALUES (?, ?, ?)", 
            (product.naam, product.aantal, houdbaar)
        )

    return {"bericht": f"{product.naam} toegevoegd", "id": cursor.lastrowid}

@app.get("/producten")
def get_products():

    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM producten ORDER BY houdbaar_tot ASC NULLS LAST"
        )
        rows = cursor.fetchall()

    return [dict(row) for row in rows]

