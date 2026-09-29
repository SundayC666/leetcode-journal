-- Write your query below
SELECT t1.customer_id, t1.customer_name FROM customers t1 
LEFT JOIN orders t2 ON t1.customer_id = t2.customer_id 
GROUP BY t1.customer_id, t1.customer_name
HAVING SUM(CASE WHEN t2.product_name = 'A' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN t2.product_name = 'B' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN t2.product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY customer_name