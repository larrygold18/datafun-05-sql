# datafun-05-sql

A Python + SQLite project to load CSVs, build a relational database, and run sample queries.  
Meets the course requirements: scripts (not notebooks), virtual environment, dependencies, GitHub workflow, and professional documentation.

---

## Goals & Learning Outcomes

- Build and manipulate a SQLite database using Python (`sqlite3`)  
- Load CSV data with `pandas` into database tables  
- Write and run SQL queries (joins, filters) from a script  
- Practice using a virtual environment and `requirements.txt`  
- Document setup, commands, and results for reproducibility  
- Practice repeatable workflow with GitHub (`git add → commit → push`)  

---

## Project Files

- `.gitignore` — ignores `.venv/`, `*.sqlite`, and other non-source files  
- `requirements.txt` — specifies dependencies (`pandas`)  
- `main.py` — Python script to create DB, load CSVs, and run queries  
- `authors.csv` & `books.csv` — sample data files  
- `example.sqlite` — generated SQLite database (ignored by Git)  
- `README.md` — documentation of project setup, workflow, and results  

## Setup Instructions (Windows / PowerShell)

```powershell
# Clone the repo
git clone https://github.com/larrygold18/datafun-05-sql.git
cd datafun-05-sql

# Create and activate a virtual environment
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# If activation fails, run this once:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
---
```

## How to Run

```powershell
python main.py
```
## Git Workflow Used
```powershell
git add -A
git commit -m "Add scaffold: .gitignore, requirements.txt, main.py"
git push

git add authors.csv books.csv
git commit -m "Add sample data CSVs"
git push

git add -A
git commit -m "First run: build SQLite DB, load CSVs, run join query"
git push

git add README.md
git commit -m "Update README with setup commands, workflow, and sample output"
git push
```

## Sample Output
```
              title                 author_name
0  Pride and Prejudice             Jane Austen
1                Emma             Jane Austen
2  Adventures of Huckleberry Finn   Mark Twain
3     Things Fall Apart             Chinua Achebe
4     Kafka on the Shore            Haruki Murakami
```
## Database Schema
```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,      -- GUID as TEXT
    first     TEXT NOT NULL,
    last      TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    book_id         TEXT PRIMARY KEY,    -- GUID as TEXT
    title           TEXT NOT NULL,
    year_published  INTEGER,
    author_id       TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

```
