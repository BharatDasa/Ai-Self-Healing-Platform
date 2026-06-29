import os
import subprocess
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

BASE = "/opt/airflow/dags/ml-pipelines"

SCRIPTS = f"{BASE}/scripts"

MODELS = f"{BASE}/models"

WORKFLOW = [

    "preprocess.py",

    "feature_engineering.py",

    "train_fraud_model.py",

    "scaling_analysis.py",

    "train_scaling_model.py"
]

# =====================================================
# RETRAINING WORKFLOW
# =====================================================

def main():

    try:

        print(
            "\n"
            "================================================="
        )

        print(
            "🚀 STARTING FULL MODEL RETRAINING PIPELINE"
        )

        print(
            "=================================================\n"
        )

        # =============================================
        # EXECUTE WORKFLOW
        # =============================================

        for script in WORKFLOW:

            script_path = (
                f"{SCRIPTS}/{script}"
            )

            print(
                f"⚙ Running: {script}"
            )

            result = subprocess.run(

                ["python", script_path],

                capture_output=True,

                text=True
            )

            print(result.stdout)

            if result.returncode != 0:

                print(result.stderr)

                raise Exception(
                    f"{script} failed"
                )

            print(
                f"✅ Completed: {script}\n"
            )

        # =============================================
        # MODEL VALIDATION
        # =============================================

        fraud_model = (
            f"{MODELS}/fraud_model.pkl"
        )

        scaling_model = (
            f"{MODELS}/scaling_model.pkl"
        )

        if os.path.exists(fraud_model):

            print(
                "✅ Fraud model validated"
            )

        else:

            raise Exception(
                "fraud_model.pkl missing"
            )

        if os.path.exists(scaling_model):

            print(
                "✅ Scaling model validated"
            )

        else:

            raise Exception(
                "scaling_model.pkl missing"
            )

        # =============================================
        # FINAL OUTPUT
        # =============================================

        print(
            "\n================================================="
        )

        print(
            "🧠 RETRAINING PIPELINE COMPLETED"
        )

        print(
            f"🕒 Completed at: {datetime.now()}"
        )

        print(
            "=================================================\n"
        )

    except Exception as e:

        print(
            f"❌ Retraining workflow failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
