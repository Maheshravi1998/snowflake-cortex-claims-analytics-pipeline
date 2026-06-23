CREATE OR REPLACE TABLE INSURANCE_ANALYTICS_DB.MARTS.RENEWAL_RISK_FEATURES AS
SELECT
    customer_id,
    policy_id,
    COUNT(claim_id) AS total_claims,
    SUM(claim_amount) AS total_claim_amount,
    AVG(claim_amount) AS avg_claim_amount,
    AVG(sentiment_score) AS avg_sentiment_score,
    CASE
        WHEN AVG(sentiment_score) < -0.3 OR SUM(claim_amount) > 5000 THEN 'High Risk'
        WHEN AVG(sentiment_score) BETWEEN -0.3 AND 0.3 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS renewal_risk_category
FROM INSURANCE_ANALYTICS_DB.MARTS.CLAIMS_SENTIMENT
GROUP BY customer_id, policy_id;
