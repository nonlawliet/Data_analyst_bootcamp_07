# Create table
CREATE TABLE menu (
  menu_id INT,
  menu_name TEXT,
  menu_price REAL );

CREATE TABLE employee (
  employee_id INT,
  employee_name TEXT,
  employee_salary REAL );

CREATE TABLE customer (
  customer_id INT,
  customer_name TEXT,
  customer_gender TEXT ); 
  
CREATE TABLE bill (
  bill_id INT,
  bill_date TEXT,
  bill_menu_id INT,
  bill_customer_id INT,
  bill_employee_id INT);

# Insert data
INSERT INTO menu VALUES
  (1, 'Pizza', 50),
  (2, 'Hotdog', 20),
  (3, 'Cake', 70),
  (4, 'Somtum', 30);

INSERT INTO employee VALUES
  (1, 'Alice', 15000),
  (2, 'Bob', 13000),
  (3, 'Carole', 14000);

INSERT INTO customer VALUES
  (1, 'Daniel', 'M'),
  (2, 'Eve', 'F'),
  (3, 'John', 'M'),
  (4, 'Tom', 'F');

INSERT INTO bill VALUES
  (1, '2023-01-01', 2, 1, 2),
  (2, '2023-01-01', 3, 2, 1),
  (3, '2023-01-01', 1, 3, 3),
  (4, '2023-01-02', 1, 1, 1),
  (5, '2023-01-03', 4, 2, 1),
  (6, '2023-01-04', 1, 4, 2),
  (7, '2023-01-05', 2, 2, 3),
  (8, '2023-01-05', 3, 2, 3),
  (9, '2023-01-06', 1, 2, 2),
  (10, '2023-01-07', 4, 3, 2);

# Analysis part
## Summary total revenue group by menu
SELECT m.menu_name, SUM(m.menu_price)
FROM bill AS b
LEFT JOIN menu AS m
ON b.bill_menu_id = m.menu_id
GROUP BY m.menu_name
ORDER BY SUM(m.menu_price) DESC;

## Summary total revenue per day
SELECT b.bill_date, SUM(m.menu_price)
FROM bill AS b
LEFT JOIN menu AS m
ON b.bill_menu_id = m.menu_id
GROUP BY b.bill_date
ORDER BY b.bill_date;

## Who has min salary, how much did they sell
SELECT e.employee_name, SUM(m.menu_price)
FROM bill AS b
JOIN employee AS e
ON b.bill_employee_id = e.employee_id
JOIN menu AS m
ON b.bill_menu_id = m.menu_id
WHERE e.employee_salary = (SELECT MIN(employee_salary) FROM employee);

## Count transaction group by gender
SELECT c.customer_gender, COUNT(*) FROM bill AS b
JOIN customer AS c
ON b.bill_customer_id = c.customer_id
WHERE b.bill_date BETWEEN '2023-01-01' AND '2023-01-03'
GROUP BY c.customer_gender;
