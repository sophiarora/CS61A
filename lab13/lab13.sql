.read data.sql

-- Q1
CREATE TABLE flight_costs as
  with
    flight(num, pre, cur) as (
      select 1, 20, 30 union
      select 2, 30, 40 union
      select num+1, cur, (pre+cur)/2+5*((num+2)%7) from flight where num < 25
    )
  SELECT num, pre from flight;

-- Q2
CREATE TABLE schedule as
  with
    flight_find(mediate, ending, num, cost) as (
      select departure||", "||arrival, arrival, 1, price from flights
      where departure = "SFO" union
      select mediate||", "||arrival, arrival, num + 1, cost+price from flights, flight_find
      where departure = ending and num < 2
    )
  SELECT mediate, cost from flight_find where ending = "PDX" order by cost;


-- Q3
CREATE TABLE shopping_cart as
  with
    choose_food(food_list, food_price, left) as (
      select item, price, 60 - price from supermarket where price <= 60 union
      select food_list||", "||item, price, left - price from choose_food, supermarket
      where left-price >= 0 and price >= food_price order by left-price, price
    )
  SELECT food_list, left from choose_food where left >= 0 order by left, food_list;


-- Q4
CREATE TABLE number_of_options as
  -- REPLACE THIS LINE
  SELECT count(distinct meat) from main_course ;


-- Q5
CREATE TABLE calories as

  SELECT count(a.meat||", "||a.side||", "||b.pie) from main_course as a,
  pies as b where a.calories+b.calories < 2500;


-- Q6
CREATE TABLE healthiest_meats as
  -- REPLACE THIS LINE
  SELECT a.meat, min(a.calories+b.calories) from main_course as a,
  pies as b group by a.meat having max(a.calories + b.calories) < 3000;


-- Q7
CREATE TABLE average_prices as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q8
CREATE TABLE lowest_prices as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q9
CREATE TABLE shopping_list as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q10
CREATE TABLE total_bandwidth as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';
