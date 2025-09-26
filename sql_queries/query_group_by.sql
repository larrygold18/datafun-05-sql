SELECT
  t.name AS team,
  COUNT(p.id)                  AS players_on_team,
  ROUND(AVG(p.salary_millions), 2) AS avg_salary
FROM teams t
LEFT JOIN players p ON p.team_id = t.id
GROUP BY t.name
ORDER BY players_on_team DESC, team ASC;
