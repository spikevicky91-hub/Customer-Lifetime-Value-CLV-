
SELECT 
    customer_id,
    SUM(revenue) AS lifetime_value,
    COUNT(*) AS transactions
FROM {{ ref('stg_clv') }}
GROUP BY customer_id
