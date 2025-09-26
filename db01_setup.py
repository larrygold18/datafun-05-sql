from pathlib import Path
import sqlite3

ROOT = Path(__file__).parent
DB = ROOT / "data" / "league.sqlite3"

def run_sql_file(conn, path: Path):
    with open(path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    print("START db01_setup.py")  # <-- add this
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        for sql_path in [
            ROOT / "sql_create" / "01_drop_tables.sql",
            ROOT / "sql_create" / "02_create_tables.sql",
            ROOT / "sql_create" / "03_insert_records.sql",
        ]:
            print(f"Running: {sql_path}", flush=True)  # <-- and this
            run_sql_file(conn, sql_path)
        conn.commit()
    print(f"Database ready at {DB}")
    
if __name__ == "__main__":
    main()
