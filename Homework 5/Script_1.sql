-- Сколько денег приносит сервис в каждом месяце?

-- Выручка по месяцам
WITH monthly_revenue AS (
SELECT
	d.year,
	d.month,
	SUM(f.amount) AS revenue
FROM
	fact_subscription_events f
JOIN dim_date d
        ON
	f.event_date_key = d.date_key
WHERE
	f.event_type = 'PAYMENT_SUCCESS'
	AND f.is_successful = TRUE
GROUP BY
	d.year,
	d.month
)


SELECT
	YEAR,
	MONTH,
	revenue
FROM
	monthly_revenue
ORDER BY
	YEAR,
	MONTH;