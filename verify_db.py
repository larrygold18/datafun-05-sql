import sqlite3
c = sqlite3.connect("data/league.sqlite3")
print("tables:", c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print("teams:",   c.execute("SELECT COUNT(*) FROM teams").fetchone()[0])
print("players:", c.execute("SELECT COUNT(*) FROM players").fetchone()[0])
