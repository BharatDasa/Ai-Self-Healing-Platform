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

    "retries": 1,

    "retry_delay": timedelta(minutes=2)
}

# =====================================================
# DAG
# =====================================================

with DAG(

    dag_id="cleanup_pipeline",

    default_args=default_args,

    start_date=datetime(2025, 1, 1),

    schedule_interval=None,

    catchup=False,

    tags=[
        "maintenance",
        "cleanup",
        "manual"
    ],

    max_active_runs=1,

    dagrun_timeout=timedelta(minutes=15)

) as dag:

    cleanup_old_data = BashOperator(

        task_id="cleanup_old_data",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/cleanup_old_data.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )
