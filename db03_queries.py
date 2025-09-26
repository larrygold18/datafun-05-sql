from pathlib import Path
import sqlite3

ROOT = Path(__file__).parent
DB = ROOT / "data" / "league.sqlite3"

def run_query(path: Path):
    with sqlite3.connect(DB) as conn:
        sql = path.read_text(encoding="utf-8")
        cur = conn.execute(sql)
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()
        print(f"\n--- {path.name} ---")
        print(" | ".join(cols))
        print("-" * (len(" | ".join(cols))))
        for r in rows:
            print(" | ".join(str(x) for x in r))

def main():
    for q in sorted((ROOT / "sql_queries").glob("*.sql")):
        run_query(q)

if __name__ == "__main__":
    main()

