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

    dag_id="scaling_training_pipeline",

    default_args=default_args,

    start_date=datetime(2025, 1, 1),

    schedule_interval="@daily",

    catchup=False,

    tags=[
        "mlops",
        "autoscaling",
        "keda",
        "ai"
    ],

    max_active_runs=1,

    dagrun_timeout=timedelta(minutes=30)

) as dag:

    # =================================================
    # EXPORT SCALING ANALYTICS
    # =================================================

    scaling_analysis = BashOperator(

        task_id="scaling_analysis",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/scaling_analysis.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )

    # =================================================
    # TRAIN SCALING MODEL
    # =================================================

    train_scaling_model = BashOperator(

        task_id="train_scaling_model",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/train_scaling_model.py"
        ),

        execution_timeout=timedelta(minutes=10)
    )

    # =================================================
    # PIPELINE FLOW
    # =================================================

    scaling_analysis >> train_scaling_model
