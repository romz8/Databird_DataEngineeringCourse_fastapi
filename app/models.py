from pydantic import BaseModel, Field

class Book(BaseModel):
    book_id: int
    title: str
    author: str
    genre: str
    published_year: int = Field(..., ge=1000, le=2023)  # Limiter les années possibles
