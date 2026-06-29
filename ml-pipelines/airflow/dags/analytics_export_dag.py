from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "platform-engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="analytics_export_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["analytics"]
) as dag:

    task = BashOperator(
        task_id="export_analytics",
        bash_command="python /opt/airflow/dags/ml-pipelines/scripts/export_analytics.py"
    )
