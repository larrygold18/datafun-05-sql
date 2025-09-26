-- Give a 5% raise to players older than 27
UPDATE players
SET salary_millions = ROUND(salary_millions * 1.05, 2)
WHERE age > 27;

