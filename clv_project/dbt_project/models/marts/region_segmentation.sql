
SELECT 
    region,
    SUM(revenue) AS total_revenue,
    COUNT(DISTINCT customer_id) AS customers
FROM {{ ref('stg_clv') }}
GROUP BY region
