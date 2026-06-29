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

    dag_id="retraining_pipeline",

    default_args=default_args,

    start_date=datetime(2025, 1, 1),

    schedule_interval="@weekly",

    catchup=False,

    tags=[
        "mlops",
        "retraining",
        "models",
        "ai"
    ],

    max_active_runs=1,

    dagrun_timeout=timedelta(minutes=15)

) as dag:

    # =================================================
    # MODEL RETRAINING VALIDATION
    # =================================================

    retrain_models = BashOperator(

        task_id="retrain_models",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/retrain_models.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )
