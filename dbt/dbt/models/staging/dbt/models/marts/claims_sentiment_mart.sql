SELECT
    claim_id,
    policy_id,
    customer_id,
    claim_date,
    claim_type,
    claim_amount,
    claim_note,
    state,
    SNOWFLAKE.CORTEX.SENTIMENT(claim_note) AS sentiment_score,
    CASE
        WHEN SNOWFLAKE.CORTEX.SENTIMENT(claim_note) > 0.3 THEN 'Positive'
        WHEN SNOWFLAKE.CORTEX.SENTIMENT(claim_note) < -0.3 THEN 'Negative'
        ELSE 'Neutral'
    END AS sentiment_category
FROM {{ ref('stg_claims') }}
