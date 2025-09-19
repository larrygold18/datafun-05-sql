# datafun-05-sql

A clean, script-first starter for **Project 5 (CC5.1)** that integrates **Python + SQLite**. You’ll practice the **repeatable workflow** (GitHub first, virtual environment, requirements, scripts), create a relational schema, load CSV data with `pandas`, and run SQL queries (joins, filters, aggregates). Optionally compare with **DuckDB**.

---

## Table of Contents
- [datafun-05-sql](#datafun-05-sql)
  - [Table of Contents](#table-of-contents)
  - [Goals \& Learning Outcomes](#goals--learning-outcomes)
  - [Tech Stack](#tech-stack)
  - [Repository Structure](#repository-structure)
  - [Prerequisites](#prerequisites)
  - [Setup (Windows, PowerShell)](#setup-windows-powershell)
  - [Repeatable Workflow](#repeatable-workflow)
  - [How to Run](#how-to-run)
  - [Database Schema](#database-schema)
  - [Sample Data](#sample-data)
  - [Example SQL Queries](#example-sql-queries)
  - [Extend the Project](#extend-the-project)
  - [Optional: DuckDB Comparison](#optional-duckdb-comparison)
  - [Troubleshooting](#troubleshooting)
  - [Notes for the Grader](#notes-for-the-grader)
  - [Acknowledgments](#acknowledgments)

---

## Goals & Learning Outcomes

- Create and manipulate a **SQLite** database from Python (via the Standard Library `sqlite3`).
- Understand file-based relational databases and how to organize **schema** and **queries**.
- Practice reading CSV files into **pandas** DataFrames and writing them into tables.
- Use a **virtual environment** and **requirements.txt** for a repeatable, professional workflow.
- Document your work thoroughly in **Markdown**.

---

## Tech Stack

- **Python 3.10+**
- **SQLite** (file-based DB; created as `example.sqlite`)
- **pandas** for CSV I/O
- (Optional) **DuckDB** for comparison

---

## Repository Structure

```
datafun-05-sql/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ data/
│  ├─ authors.csv
│  └─ books.csv
├─ src/
│  ├─ main.py          # Entry point: build DB, run sample queries
│  ├─ db_utils.py      # Helpers: connect, init schema, upserts, read_sql_as_df
│  ├─ schema.sql       # DDL for authors, books
│  └─ queries.sql      # Example queries (counts, join, filters)
└─ tests/
   └─ test_smoke.py    # Imports check
```

---

## Prerequisites

- **Git** installed and configured
- **Python 3.10+** available on your PATH (`py --version`)
- A **GitHub** account

---

## Setup (Windows, PowerShell)

1. **Create the GitHub repo first** named `datafun-05-sql` and **check “Add a README”**.
2. **Clone** the repo locally and open the folder in VS Code.

```powershell
git clone https://github.com/<your-username>/datafun-05-sql.git
cd datafun-05-sql
```

3. **Create & activate a virtual environment**:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. **Install dependencies**:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. **First commit** (scaffold + environment files tracked appropriately):

```powershell
git add .
git commit -m "Project scaffold: src, data, tests, requirements, gitignore"
git push
```

---

## Repeatable Workflow

```powershell
git pull
# make your edits
git status
git add -A
git commit -m "Describe your change (what & why)"
git push
```

- Keep `.venv/` and `*.sqlite` **out of version control** via `.gitignore`.
- Commit early and often with meaningful messages.

---

## How to Run

From the project root:

```powershell
python -m src.main
```

You should see:
- Row counts for authors and books
- A join of authors → books
- Parameterized example: books after a given year
- A new `example.sqlite` created in the project root (ignored by Git)

---

## Database Schema

`src/schema.sql` contains two tables:

```sql
CREATE TABLE IF NOT EXISTS authors (
    author_id      INTEGER PRIMARY KEY,
    author_name    TEXT NOT NULL,
    country        TEXT
);

CREATE TABLE IF NOT EXISTS books (
    book_id        INTEGER PRIMARY KEY,
    title          TEXT NOT NULL,
    author_id      INTEGER NOT NULL,
    year_published INTEGER,
    genre          TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```

---

## Sample Data

Two small CSVs live in `data/`:
- `authors.csv` (id, name, country)
- `books.csv` (id, title, author_id, year, genre)

You can expand these to test joins, filters, and aggregates.

---

## Example SQL Queries

- **Counts** for quick sanity checks

```sql
SELECT (SELECT COUNT(*) FROM authors) AS author_count,
       (SELECT COUNT(*) FROM books)   AS book_count;
```

- **Join** authors to books

```sql
SELECT b.book_id, b.title, a.author_name, a.country, b.year_published, b.genre
FROM books AS b
JOIN authors AS a ON a.author_id = b.author_id
ORDER BY a.author_name, b.year_published;
```

- **Parameterized** (from Python) — books after year X

```sql
SELECT * FROM books
WHERE year_published >= ?
ORDER BY year_published;
```

---

## Extend the Project

- Add more tables (e.g., `publishers`, `sales`, `reviews`)
- Add **indexes** for performance and test query plans
- Split SQL files into folders: `sql_create/`, `sql_features/`, `sql_queries/`
- Add scripts like `db01_setup.py` (build DB), `db02_features.py` (updates/deletes),
  `db03_queries.py` (aggregations, group by, joins)
- Add **unit tests** for critical logic
- Visualize results with `matplotlib` (optional)

---

## Optional: DuckDB Comparison

1. Uncomment `duckdb` in `requirements.txt` and reinstall:
   ```
   duckdb>=1.1
   ```
   ```powershell
   pip install -r requirements.txt
   ```
2. Create `src/duck_demo.py`:
   ```python
   import duckdb
   print(duckdb.sql("select 42 as answer").df())
   ```
3. Run:
   ```powershell
   python -m src.duck_demo
   ```
4. Note differences in ergonomics/perf in your README.

---

## Troubleshooting

- **Module not found** when running `python -m src.main` → ensure you’re in the project root and `src/` exists.
- **No venv prompt** → re-run activation: `.\.venv\Scripts\Activate.ps1`.
- **Permission error on activation** → set execution policy once (as Admin):  
  `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Pip install fails** → upgrade pip: `python -m pip install --upgrade pip`.

---

## Notes for the Grader

- Repo named **exactly** `datafun-05-sql` and created with a README.
- Uses **scripts** (not notebooks) for this module.
- `.venv/` and `*.sqlite` are ignored.
- README documents exact commands, observations, and results.
- (Optional) Includes a DuckDB demo & brief comparison.

---

## Acknowledgments

- Course guidance and recommended workflow from **Dr. Denise Case**.
- SQLite & pandas docs for API references.
