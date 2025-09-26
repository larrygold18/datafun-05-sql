from pathlib import Path
import sqlite3

ROOT = Path(__file__).parent
DB = ROOT / "data" / "league.sqlite3"

def run_script(conn, path: Path):
    sql = path.read_text(encoding="utf-8")
    print(f"-- running {path.name}")
    try:
        conn.executescript(sql)
    except sqlite3.Error as e:
        print(f"!! sqlite error in {path.name}: {e}")
        print("SQL was:\n", sql)
        raise

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        before = conn.total_changes
        run_script(conn, ROOT / "sql_features" / "update_records.sql")
        mid = conn.total_changes
        run_script(conn, ROOT / "sql_features" / "delete_records.sql")
        after = conn.total_changes

        conn.commit()

    print(f"Updated rows: {mid - before} | Deleted rows: {after - mid}")

if __name__ == "__main__":
    main()
