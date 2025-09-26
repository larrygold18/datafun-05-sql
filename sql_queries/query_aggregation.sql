SELECT
  COUNT(*)                     AS player_count,
  ROUND(AVG(age), 2)           AS avg_age,
  ROUND(SUM(salary_millions), 2) AS total_salary
FROM players;
