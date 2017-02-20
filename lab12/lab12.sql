.read data.sql

-- Q2
CREATE TABLE obedience as
  SELECT seven, denero from students;


-- Q3
CREATE TABLE blue_dog as
  -- REPLACE THIS LINE
  SELECT color, pet from students where color = "blue" and pet = "dog";


-- Q4
CREATE TABLE smallest_int as
  -- REPLACE THIS LINE
  SELECT time, smallest from students where smallest > 6 order by smallest limit 20;


-- Q5
CREATE TABLE sevens as
  -- REPLACE THIS LINE
  SELECT a.seven from students as a, checkboxes as b where a.number = 7 and b.'7' = "True" and a.time = b.time;


-- Q6
CREATE TABLE matchmaker as
  -- REPLACE THIS LINE
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b
  where a.pet = b.pet and a.song = b.song and a.time <> b.time order by a.time;
