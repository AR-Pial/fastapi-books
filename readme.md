# FastAPI Books API

A simple FastAPI project with books stored in a JSON/dictionary. No database for now.

## API Endpoints
- `GET /books` → List all books
- `GET /books/{id}` → Get book by ID

## Quick Start
```bash
git clone git@github.com/AR-Pial/fastapi-books.git
cd fastapi-books
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

uvicorn main:app --reload
