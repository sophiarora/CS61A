.read lab12.sql

-- Q7
CREATE TABLE smallest_int_count as
  -- REPLACE THIS LINE
  SELECT smallest, count(*) from students where smallest >= 1 group by smallest;
