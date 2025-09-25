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
