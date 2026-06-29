import pandas as pd
import os

# =====================================================
# CONFIG
# =====================================================

INPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/fraud_history.csv"
)

OUTPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/feature_data.csv"
)

# =====================================================
# FEATURE ENGINEERING
# =====================================================

def main():

    try:

        print("🚀 Starting feature engineering")

        # =============================================
        # VALIDATE INPUT
        # =============================================

        if not os.path.exists(INPUT):

            print(
                "❌ fraud_history.csv not found"
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
                "⚠ Empty fraud history dataset"
            )

            empty_df = pd.DataFrame(columns=[

                "user_id",
                "amount",
                "location",
                "timestamp",
                "amount_scaled",
                "risk_score",
                "high_amount",
                "fraud_prediction",
                "fraud_probability"
            ])

            empty_df.to_csv(
                OUTPUT,
                index=False
            )

            print(
                "✅ Empty feature dataset exported"
            )

            os._exit(0)

        # =============================================
        # REQUIRED COLUMNS VALIDATION
        # =============================================

        required_columns = [

            "amount"
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

        df["amount"] = pd.to_numeric(
            df["amount"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["amount"]
        )

        # =============================================
        # FEATURE GENERATION
        # =============================================

        df["high_amount"] = (
            df["amount"] > 8000
        ).astype(int)

        # =============================================
        # AMOUNT SCALING
        # =============================================

        if "amount_scaled" not in df.columns:

            df["amount_scaled"] = (
                df["amount"] / 10000
            )

        else:

            df["amount_scaled"] = pd.to_numeric(
                df["amount_scaled"],
                errors="coerce"
            )

        # =============================================
        # RISK SCORE
        # =============================================

        if "risk_score" not in df.columns:

            df["risk_score"] = (

                df["amount_scaled"] * 0.7 +

                df["high_amount"] * 0.3
            )

        else:

            df["risk_score"] = pd.to_numeric(
                df["risk_score"],
                errors="coerce"
            )

        # =============================================
        # FRAUD LABEL PRESERVATION
        # =============================================

        if "fraud_prediction" not in df.columns:

            print(
                "⚠ fraud_prediction missing "
                "→ fallback to high_amount labels"
            )

            df["fraud_prediction"] = (
                df["high_amount"]
            )

        else:

            df["fraud_prediction"] = pd.to_numeric(
                df["fraud_prediction"],
                errors="coerce"
            )

        # =============================================
        # FRAUD PROBABILITY SAFETY
        # =============================================

        if "fraud_probability" in df.columns:

            df["fraud_probability"] = pd.to_numeric(
                df["fraud_probability"],
                errors="coerce"
            )

        # =============================================
        # REMOVE INVALID DATA
        # =============================================

        df = df.dropna()

        # =============================================
        # REMOVE DUPLICATES
        # =============================================

        duplicate_keys = [

            col for col in [
                "user_id",
                "timestamp"
            ]

            if col in df.columns
        ]

        if duplicate_keys:

            df = df.drop_duplicates(
                subset=duplicate_keys
            )

        # =============================================
        # FINAL EMPTY CHECK
        # =============================================

        if df.empty:

            print(
                "❌ Dataset became empty after cleaning"
            )

            os._exit(1)

        # =============================================
        # EXPORT FEATURES
        # =============================================

        df.to_csv(
            OUTPUT,
            index=False
        )

        # =============================================
        # FINAL OUTPUT
        # =============================================

        print(df.head())

        print(
            f"📦 Engineered rows: {len(df)}"
        )

        print(
            f"📊 Fraud ratio: "
            f"{round(df['fraud_prediction'].mean(), 4)}"
        )

        print(
            f"💰 Avg amount: "
            f"{round(df['amount'].mean(), 2)}"
        )

        print(
            f"⚠ Avg risk score: "
            f"{round(df['risk_score'].mean(), 4)}"
        )

        print(
            "✅ Feature engineering completed"
        )

    except Exception as e:

        print(
            f"❌ Feature engineering failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
