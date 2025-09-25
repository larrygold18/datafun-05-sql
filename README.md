# DataFun-05-SQL: Teams → Players

This project demonstrates using **Python + SQLite** to create and query a relational database.

## How to Run (Windows 11)

```powershell
# 1) Clone
git clone https://github.com/larrygold18/datafun-05-sql.git
cd datafun-05-sql

# 2) Create & activate venv
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install -r requirements.txt

# 4) Build DB
py db01_setup.py

# 5) Run features (update/delete)
py db02_features.py

# 6) Run queries
py db03_queries.py
