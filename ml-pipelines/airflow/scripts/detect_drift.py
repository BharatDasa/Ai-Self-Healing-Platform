import pandas as pd
import os

from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

INPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/feature_data.csv"
)

REPORT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/reports/drift_report.txt"
)

# =====================================================
# DRIFT DETECTION
# =====================================================

def main():

    try:

        print("🚀 Starting drift detection")

        # =============================================
        # VALIDATE INPUT
        # =============================================

        if not os.path.exists(INPUT):

            print(
                "❌ feature_data.csv not found"
            )

            os._exit(1)

        # =============================================
        # LOAD DATA
        # =============================================

        df = pd.read_csv(INPUT)

        # =============================================
        # EMPTY DATASET SAFETY
        # =============================================

        if df.empty:

            print(
                "⚠ Empty feature dataset"
            )

            os._exit(0)

        # =============================================
        # REQUIRED COLUMNS
        # =============================================

        required_columns = [

            "amount_scaled",
            "risk_score"
        ]

        missing = [

            col for col in required_columns

            if col not in df.columns
        ]

        if missing:

            print(
                f"❌ Missing columns: {missing}"
            )

            os._exit(1)

        # =============================================
        # CLEAN DATA
        # =============================================

        df["amount_scaled"] = pd.to_numeric(
            df["amount_scaled"],
            errors="coerce"
        )

        df["risk_score"] = pd.to_numeric(
            df["risk_score"],
            errors="coerce"
        )

        df = df.dropna()

        # =============================================
        # DRIFT LOGIC
        # =============================================

        mean_amount = round(

            df["amount_scaled"].mean(),

            4
        )

        mean_risk = round(

            df["risk_score"].mean(),

            4
        )

        drift_detected = (

            mean_amount > 0.75 or

            mean_risk > 0.80
        )

        status = (

            "DRIFT DETECTED"

            if drift_detected

            else "HEALTHY"
        )

        # =============================================
        # REPORT
        # =============================================

        report = f"""
AI MODEL DRIFT REPORT
=====================

Generated: {datetime.now()}

Dataset Size: {len(df)}

Mean Amount Score: {mean_amount}

Mean Risk Score: {mean_risk}

Status: {status}
"""

        with open(REPORT, "w") as f:

            f.write(report)

        # =============================================
        # FINAL OUTPUT
        # =============================================

        print(report)

        print(
            "✅ Drift analysis completed"
        )

    except Exception as e:

        print(
            f"❌ Drift detection failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
