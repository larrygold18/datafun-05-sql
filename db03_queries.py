# db03_queries.py
from pathlib import Path
import sqlite3, csv

ROOT = Path(__file__).parent
DB = ROOT / "data" / "league.sqlite3"
OUT_DIR = ROOT / "docs" / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def run_query(path: Path) -> None:
    with sqlite3.connect(DB) as conn:
        sql = path.read_text(encoding="utf-8")
        cur = conn.execute(sql)

        # headers
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()

        # pretty print widths
        widths = [max(len(str(x)) for x in [c, *[r[i] for r in rows]] or [0]) for i, c in enumerate(cols)]

        print(f"\n--- {path.name} ---")
        print(" | ".join(str(c).ljust(widths[i]) for i, c in enumerate(cols)))
        print("-" * (sum(widths) + 3 * (len(cols) - 1)))
        for r in rows:
            print(" | ".join(str(r[i]).ljust(widths[i]) for i in range(len(cols))))

        # save CSV too
        csv_path = OUT_DIR / f"out_{path.stem}.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(cols)
            w.writerows(rows)
        print(f"Saved: {csv_path}")

def main():
    qdir = ROOT / "sql_queries"
    qs = sorted(qdir.glob("*.sql"))
    print(f"Found {len(qs)} SQL file(s) in {qdir}")
    for q in qs:
        run_query(q)

if __name__ == "__main__":
    main()
