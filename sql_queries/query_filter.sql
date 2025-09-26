SELECT first_name, last_name, position, age, salary_millions
FROM players
WHERE age >= 30
  AND salary_millions > 8
ORDER BY salary_millions DESC;
