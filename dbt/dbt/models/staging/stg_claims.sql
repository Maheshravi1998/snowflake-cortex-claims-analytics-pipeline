SELECT
    claim_id,
    policy_id,
    customer_id,
    claim_date,
    claim_type,
    claim_amount,
    claim_note,
    state
FROM INSURANCE_ANALYTICS_DB.RAW.CLAIMS_RAW
WHERE claim_id IS NOT NULL
