# Snowflake Cortex AI Claims Analytics Pipeline

This project demonstrates an end-to-end insurance claims analytics pipeline using Python, AWS S3, Snowpipe, Snowflake, dbt, Airflow, Cortex AI, Snowflake ML, and Streamlit.

## Architecture

Python → AWS S3 → Snowpipe → Snowflake → dbt → Airflow → Cortex AI → Streamlit

## Use Case

Insurance companies process large volumes of claims, customer notes, and policy information. Manual review of this data can be slow and inconsistent.

This project shows how claims notes can be analyzed using Snowflake Cortex AI sentiment analysis and how renewal risk can be predicted using Snowflake ML.

## Features

- Python-based data ingestion
- AWS S3 raw data landing zone
- Snowpipe auto-ingestion into Snowflake
- Snowflake raw, staging, and mart schemas
- dbt transformations
- Airflow orchestration
- Cortex AI sentiment analysis on claim notes
- Streamlit dashboard for analytics

## Data

This project uses synthetic insurance claims data. No real customer data or company data is used.

## Pipeline Flow

1. Python uploads claims data to AWS S3.
2. Snowpipe loads files from S3 into Snowflake.
3. dbt transforms raw claims data into analytics-ready models.
4. Cortex AI calculates sentiment from claim notes.
5. Snowflake ML can be used to classify renewal risk.
6. Streamlit displays claim trends and risk insights.

## Disclaimer

This is a portfolio project built with synthetic data. It does not contain proprietary company code, customer data, or confidential business logic.
