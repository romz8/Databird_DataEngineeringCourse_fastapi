import pandas as pd

def load_books():
    """Charge les livres depuis le fichier CSV."""
    file_path = "./data/books.csv"
    return pd.read_csv(file_path)

def save_books(books_df):
    """Enregistre les livres dans le fichier CSV."""
    file_path = "data/books.csv"
    books_df.to_csv(file_path, index=False)
