# Voorraad API

Backend for **Voorraad**, a personal grocery inventory app I'm building to track what's in my kitchen, when products expire, and (eventually) turn photos of receipts into structured data automatically.

This repository contains the REST API. It runs in Docker on my self-hosted home server (Ubuntu Server, accessible via Tailscale).

## Features (so far)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check (used for uptime monitoring) |
| `GET` | `/producten` | List all products in stock |
| `POST` | `/producten` | Add a product (name, quantity, expiry date) with automatic input validation |

Interactive API docs are generated automatically at `/docs`.

## Tech stack

- **Python 3.12**
- **FastAPI**: web framework for building the API
- **Pydantic**: data models and input validation
- **Uvicorn**: ASGI server that runs the app
- **Git & GitHub**: version control

## Run locally

```bash
# 1. Clone the repository
git clone git@github.com:Patrick_Mic/voorraad-api.git
cd voorraad-api

# 2. Create and activate a virtual environment, install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Start the development server
fastapi dev main.py
```

Then open http://127.0.0.1:8000/docs

## Roadmap

- [x] Basic API with health check and product endpoints
- [ ] Persistent storage with SQLite
- [ ] Containerize with Docker and deploy to home server
- [ ] Receipt photo → product data via the Claude API
- [ ] Expiry notifications
- [ ] Recipe suggestions based on current stock
- [ ] Power BI dashboard on purchase and consumption data