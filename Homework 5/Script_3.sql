-- Какие тарифы приносят больше всего денег?

SELECT
	plan_name,
	revenue
FROM
	(
	SELECT
		p.plan_name,
		SUM(f.amount) AS revenue
	FROM
		fact_subscription_events f
	JOIN dim_plan p
        ON
		f.plan_key = p.plan_key
	WHERE
		f.event_type = 'PAYMENT_SUCCESS'
		AND f.is_successful = TRUE
	GROUP BY
		p.plan_name
) AS plan_revenue
ORDER BY
	revenue DESC
LIMIT 3;

