import csv, sqlite3
from pathlib import Path

DB = Path("example.sqlite")
DATA = Path("data")

def run_sql(conn, path):
    with open(path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    # start fresh each run
    DB.unlink(missing_ok=True)
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        # create tables
        run_sql(conn, "sql_create/01_create_tables.sql")

        # load authors from CSV
        with (DATA / "authors.csv").open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [(r["author_id"], r["first"], r["last"]) for r in reader]
        conn.executemany("INSERT INTO authors(author_id, first, last) VALUES (?,?,?)", rows)

        # load books from CSV
        with (DATA / "books.csv").open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [(r["book_id"], r["title"], int(r["year_published"]), r["author_id"]) for r in reader]
        conn.executemany("INSERT INTO books(book_id, title, year_published, author_id) VALUES (?,?,?,?)", rows)

        # alter table: add is_favorite if not already there
        cur = conn.execute("PRAGMA table_info(books)")
        cols = [row[1] for row in cur.fetchall()]
        if "is_favorite" not in cols:
            conn.executescript(Path("sql_alter/01_add_is_favorite.sql").read_text(encoding="utf-8"))

        # quick check
        for row in conn.execute("""
            SELECT b.title, b.year_published, a.first || ' ' || a.last AS author, b.is_favorite
            FROM books b JOIN authors a ON a.author_id=b.author_id
            ORDER BY b.year_published
        """):
            print(row)

if __name__ == "__main__":
    main()
