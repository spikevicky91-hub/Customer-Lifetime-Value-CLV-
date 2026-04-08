
SELECT 
    AVG(lifetime_value) AS avg_revenue_per_user
FROM {{ ref('fct_clv') }}
