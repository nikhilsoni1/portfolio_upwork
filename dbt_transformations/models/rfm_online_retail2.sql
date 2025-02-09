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
    monetary_score
FROM rfm_computation
