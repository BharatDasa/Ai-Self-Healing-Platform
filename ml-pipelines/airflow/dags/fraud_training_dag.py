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

    dag_id="fraud_training_pipeline",

    default_args=default_args,

    start_date=datetime(2025, 1, 1),

    schedule_interval="@daily",

    catchup=False,

    tags=[
        "mlops",
        "fraud",
        "training",
        "ai"
    ],

    max_active_runs=1,

    dagrun_timeout=timedelta(minutes=30)

) as dag:

    # =================================================
    # PREPROCESS FRAUD EVENTS
    # =================================================

    preprocess_data = BashOperator(

        task_id="preprocess_data",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/preprocess.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )

    # =================================================
    # FEATURE ENGINEERING
    # =================================================

    feature_engineering = BashOperator(

        task_id="feature_engineering",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/feature_engineering.py"
        ),

        execution_timeout=timedelta(minutes=5)
    )

    # =================================================
    # TRAIN FRAUD MODEL
    # =================================================

    train_fraud_model = BashOperator(

        task_id="train_fraud_model",

        bash_command=(
            "python "
            "/opt/airflow/dags/ml-pipelines/"
            "scripts/train_fraud_model.py"
        ),

        execution_timeout=timedelta(minutes=10)
    )

    # =================================================
    # PIPELINE FLOW
    # =================================================

    preprocess_data >> feature_engineering >> train_fraud_model
