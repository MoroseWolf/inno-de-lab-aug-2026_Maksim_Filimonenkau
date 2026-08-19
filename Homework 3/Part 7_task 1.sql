SELECT
    concat(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM
    customers AS c
JOIN orders AS o
ON
    c.customer_id = o.customer_id
WHERE
    c.customer_id IN (
    SELECT
        s.customer
    FROM
        shippings AS s
    WHERE
        status = 'Delivered')
GROUP BY
    full_name,
    c.country
HAVING
    COUNT(o.order_id) >= 2
