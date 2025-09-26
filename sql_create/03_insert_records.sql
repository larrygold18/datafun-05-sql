-- TEAMS (10+)
INSERT INTO teams (id, name, city, founded_year) VALUES
 ('t1','Lions','Dallas',1980),
 ('t2','Falcons','Atlanta',1975),
 ('t3','Sharks','San Jose',1991),
 ('t4','Bulls','Chicago',1966),
 ('t5','Tigers','Detroit',1934),
 ('t6','Kings','Sacramento',1985),
 ('t7','Wolves','Minneapolis',1989),
 ('t8','Storm','Seattle',2000),
 ('t9','Raptors','Toronto',1995),
 ('t10','Knights','Orlando',1989);

-- PLAYERS (10+; all team_id values must exist in teams.id)
INSERT INTO players (id, team_id, first_name, last_name, position, age, salary_millions) VALUES
 ('p1','t1','Alex','Carter','Forward',29,12.5),
 ('p2','t1','Jordan','Miles','Guard',24,8.2),
 ('p3','t1','Riley','Nguyen','Center',31,10.1),
 ('p4','t2','Sam','Lopez','Forward',27,7.5),
 ('p5','t2','Chris','Osei','Guard',26,6.1),
 ('p6','t2','Devon','Price','Center',30,9.8),
 ('p7','t3','Kai','Ishikawa','Forward',25,5.2),
 ('p8','t3','Maya','Chen','Guard',23,4.7),
 ('p9','t3','Leo','Martins','Center',28,7.9),
 ('p10','t4','Ava','Brooks','Forward',30,11.0),
 ('p11','t5','Nina','Thomas','Guard',22,4.1),
 ('p12','t6','Omar','Singh','Center',27,6.8),
 ('p13','t7','Ella','Park','Forward',26,6.2),
 ('p14','t8','Zane','Garcia','Guard',29,8.7),
 ('p15','t9','Ivy','Lin','Center',24,5.3),
 ('p16','t10','Amir','Diaz','Forward',28,7.1),
 ('p17','t10','Lia','Baker','Guard',25,5.9),
 ('p18','t9','Noah','Wright','Forward',27,6.6),
 ('p19','t8','Sofia','Reed','Center',31,9.2),
 ('p20','t7','Ethan','Hale','Guard',23,4.9);
