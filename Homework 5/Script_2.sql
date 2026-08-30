-- Сколько пользователей начали пробный период и сколько из них в итоге оплатили подписку?

WITH trial_users AS (
SELECT
	DISTINCT
        user_key
FROM
	fact_subscription_events
WHERE
	event_type = 'TRIAL_START'
),
paid_users AS (
SELECT
	DISTINCT
        user_key
FROM
	fact_subscription_events
WHERE
	event_type = 'PAYMENT_SUCCESS'
	AND is_successful = TRUE
)

SELECT
	COUNT(t.user_key) AS trial_users_count,
	COUNT(p.user_key) AS paid_from_trial_count,
	ROUND(
        100.0 * COUNT(p.user_key) / NULLIF(COUNT(t.user_key), 0),
        2
    ) AS conversion_rate
FROM
	trial_users t
LEFT JOIN paid_users p
    ON
	t.user_key = p.user_key;