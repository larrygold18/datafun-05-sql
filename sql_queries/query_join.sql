SELECT
  t.city || ' ' || t.name            AS team,
  p.first_name || ' ' || p.last_name AS player,
  p.position,
  p.age,
  p.salary_millions
FROM players p
JOIN teams t ON t.id = p.team_id
ORDER BY team, player;
