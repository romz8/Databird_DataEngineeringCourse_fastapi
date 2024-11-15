from fastapi import APIRouter, HTTPException
from app.db import load_books, save_books
from app.models import Book
import pandas as pd

# Créer un routeur pour les endpoints liés aux livres
router = APIRouter()

@router.get("/books")
def get_books(genre: str = None, author: str = None):
    """Récupère tous les livres ou filtre par genre/auteur."""
    books = load_books()
    if genre:
        books = books[books['genre'].str.lower() == genre.lower()]
    if author:
        books = books[books['author'].str.lower() == author.lower()]
    return books.to_dict(orient="records")

@router.get("/books/{book_id}")
def get_book(book_id: int):
    """Récupère un livre par son ID."""
    books = load_books()
    book = books[books['book_id'] == book_id].to_dict(orient="records")
    if not book:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return book[0]

@router.post("/books")
def add_book(book: Book):
    """Ajoute un nouveau livre."""
    books = load_books()
    if not books[books['book_id'] == book.book_id].empty:
        raise HTTPException(status_code=400, detail="Un livre avec cet ID existe déjà.")
    new_book = pd.DataFrame([book.dict()])
    books = pd.concat([books, new_book], ignore_index=True)
    save_books(books)
    return book
