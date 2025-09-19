# datafun-05-sql

A simple Python + SQLite project to load CSVs, build a relational database, and run sample queries. Meets the course requirements: scripts (not notebooks), virtual environment, dependencies, and documentation of workflow.

---

## Goals & Learning Outcomes

- Build and manipulate a SQLite database using Python (`sqlite3`)  
- Load CSV data with `pandas` into database tables  
- Write and run SQL queries (joins, filters) from scripts  
- Practice using a virtual environment and `requirements.txt`  
- Document setup, commands, and results for reproducibility  

---

## Project Files

- `.gitignore` — ignores `*.sqlite`, `.venv`, etc.  
- `requirements.txt` — lists Python packages (`pandas`)  
- `main.py` — script that builds DB, loads CSVs, and runs queries  
- `authors.csv` & `books.csv` — sample data files  
- `example.sqlite` — generated database file (ignored by Git)  

---

## Setup Instructions (Windows / PowerShell)

```powershell
# Clone the repo
git clone https://github.com/larrygold18/datafun-05-sql.git
cd datafun-05-sql

# Create and activate a virtual environment
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# If you hit a policy error, run this once:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
