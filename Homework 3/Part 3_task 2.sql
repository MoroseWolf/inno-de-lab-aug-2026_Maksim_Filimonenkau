SELECT 
    item,
    COUNT(item),
    trunc(AVG(amount), 2) AS avg_amount
FROM 
    orders
GROUP BY 
    item