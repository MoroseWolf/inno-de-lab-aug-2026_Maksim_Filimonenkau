SELECT
    s.status , c.first_name, c.last_name 
FROM 
    shippings AS s
JOIN customers AS c 
ON
    c.customer_id = s.customer 