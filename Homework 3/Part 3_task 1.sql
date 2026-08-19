SELECT 
    country,
    count(country)
FROM 
    customers
GROUP BY 
    country 