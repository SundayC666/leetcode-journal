-- Write your query below
SELECT employee_id,
CASE 
    WHEN (employee_id %2 = 0) IS FALSE AND name NOT LIKE ('M%') THEN employees.salary
ELSE 0
END AS bonus
FROM employees
ORDER BY employee_id ASC