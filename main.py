import sqlite3
import pandas as pd
from pathlib import Path

# File paths
DATA_DIR = Path(__file__).parent
AUTHORS_CSV = DATA_DIR / "authors.csv"
BOOKS_CSV = DATA_DIR / "books.csv"
DB_PATH = DATA_DIR / "example.sqlite"

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")

    # Create tables
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL,
        country TEXT
    );
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        year_published INTEGER,
        genre TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
    """)

    # Load CSVs into tables
    pd.read_csv(AUTHORS_CSV).to_sql("authors", conn, if_exists="replace", index=False)
    pd.read_csv(BOOKS_CSV).to_sql("books", conn, if_exists="replace", index=False)

    # Simple query
    result = pd.read_sql_query("""
        SELECT b.title, a.author_name
        FROM books b
        JOIN authors a ON b.author_id = a.author_id;
    """, conn)
    print(result)

    conn.close()

if __name__ == "__main__":
    main()
