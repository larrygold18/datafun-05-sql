ALTER TABLE books ADD COLUMN is_favorite INTEGER NOT NULL DEFAULT 0;

-- Example updates
UPDATE books SET is_favorite = 1 WHERE title = 'To Kill a Mockingbird';
UPDATE books SET is_favorite = 1 WHERE title LIKE 'Harry Potter%';
