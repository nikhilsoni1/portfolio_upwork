{{ config(
    materialized='table'
) }}

WITH rfm_base AS (
    SELECT
        customer_id,
        MAX(invoice_datetime) AS last_purchase_date,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(quantity * unit_price) AS monetary
    FROM {{ ref('cleaned_online_retail2') }}
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
),
date_reference AS (
    SELECT MAX(invoice_datetime) AS max_date FROM {{ ref('cleaned_online_retail2') }}
),
rfm_computation AS (
    SELECT
        r.customer_id,
        DATE_PART('day', d.max_date - r.last_purchase_date) AS recency,
        r.frequency,
        r.monetary,
        NTILE(5) OVER (ORDER BY DATE_PART('day', d.max_date - r.last_purchase_date) ASC) AS recency_score,
        NTILE(5) OVER (ORDER BY r.frequency DESC) AS frequency_score,
        NTILE(5) OVER (ORDER BY r.monetary DESC) AS monetary_score
    FROM rfm_base r
    JOIN date_reference d ON 1=1
)
SELECT 
    customer_id,
    recency_score,
    frequency_score,
    monetary_score,
    CASE 
        -- Champions: Highest priority (0)
        WHEN recency_score = 5 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'champions'
        -- Loyal Customers: Priority (1)
        WHEN recency_score >= 3 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'loyal_customers'
        -- Potential Loyalists: Priority (2)
        WHEN recency_score = 5 AND frequency_score >= 3 THEN 'potential_loyalists'
        -- At Risk: Priority (3)
        WHEN recency_score <= 2 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'at_risk'
        -- Lost Customers: Priority (4)
        WHEN recency_score = 1 AND frequency_score = 1 AND monetary_score = 1 THEN 'lost_customers'
        -- Other categories (Priority 5, can be further refined)
        ELSE 'others'
    END AS rfm_segment,
    CASE 
        WHEN recency_score = 5 AND frequency_score >= 4 AND monetary_score >= 4 THEN 0  -- Champions
        WHEN recency_score >= 3 AND frequency_score >= 4 AND monetary_score >= 4 THEN 1  -- Loyal Customers
        WHEN recency_score = 5 AND frequency_score >= 3 THEN 2  -- Potential Loyalists
        WHEN recency_score <= 2 AND frequency_score >= 4 AND monetary_score >= 4 THEN 3  -- At Risk
        WHEN recency_score = 1 AND frequency_score = 1 AND monetary_score = 1 THEN 4  -- Lost Customers
        ELSE 5  -- Others
    END AS rfm_segment_priority
FROM rfm_computation
