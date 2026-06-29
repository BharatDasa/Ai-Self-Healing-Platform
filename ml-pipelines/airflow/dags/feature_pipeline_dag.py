from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import (
    datetime,
    timedelta
)

# =====================================================
# DEFAULT CONFIG
# =====================================================

default_args = {

    "owner": "platform-engineering",

    "depends_on_past": False,

    "email_on_failure": False,

    "email_on_retry": False,

    "retries": 2,

    "retry_delay": timedelta(minutes=2)
}

# =====================================================
# DAG
# =====================================================

with DAG(

    dag_id="feature_pipeline",

    default_args=default_args,

    start_date=datetime(2025, 1, 1),

    schedule_interval="*/30 * * * *",

    catchup=False,

    tags=[
        "mlops",
        "features",
        "preprocessing"
    ],

    max_active_runs=1,

    dagrun_timeout=timedelta(minutes=15)

) as dag:

    feature_engineering = BashOperator(

        task_id="feature_engineering",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/feature_engineering.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )
