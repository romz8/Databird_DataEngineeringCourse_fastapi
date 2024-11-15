from fastapi import FastAPI
from app.routes.books_routes import router as books_router

# Créer une instance de l'application FastAPI
app = FastAPI()

# Inclure les routes pour les livres
app.include_router(books_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Bookstore!"}
