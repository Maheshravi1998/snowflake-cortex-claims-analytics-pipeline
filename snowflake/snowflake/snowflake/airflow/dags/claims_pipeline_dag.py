from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="claims_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["snowflake", "dbt", "claims", "cortex-ai"],
) as dag:

    upload_to_s3 = BashOperator(
        task_id="upload_claims_file_to_s3",
        bash_command="python python_ingestion/upload_to_s3.py"
    )

    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd dbt && dbt run"
    )

    run_dbt_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command="cd dbt && dbt test"
    )

    run_cortex_sentiment = BashOperator(
        task_id="run_cortex_sentiment_sql",
        bash_command="echo 'Run Snowflake Cortex sentiment SQL'"
    )

    upload_to_s3 >> run_dbt_models >> run_dbt_tests >> run_cortex_sentiment
