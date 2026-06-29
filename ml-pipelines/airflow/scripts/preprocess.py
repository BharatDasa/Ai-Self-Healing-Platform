import pandas as pd
from pymongo import MongoClient
import os

# =====================================================
# CONFIG
# =====================================================

MONGO_URI = (
    "mongodb://mongodbAdmin:Admin123@"
    "mongodb.databases.svc.cluster.local:27017/"
)

EXPORT_PATH = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/fraud_history.csv"
)

# =====================================================
# PREPROCESS WORKFLOW
# =====================================================

def main():

    try:

        print("🚀 Starting fraud preprocessing")

        # =============================================
        # CONNECT MONGODB
        # =============================================

        client = MongoClient(MONGO_URI)

        db = client["fraud_detection"]

        predictions = db["predictions"]

        # =============================================
        # LOAD PREDICTION DATA
        # =============================================

        data = list(

            predictions.find(
                {},
                {"_id": 0}
            )
        )

        # =============================================
        # EMPTY DATASET SAFETY
        # =============================================

        if not data:

            print(
                "⚠ No prediction data found"
            )

            os._exit(0)

        # =============================================
        # DATAFRAME
        # =============================================

        df = pd.DataFrame(data)

        # =============================================
        # REQUIRED COLUMNS
        # =============================================

        required_columns = [

            "amount",
            "risk_score",
            "fraud_prediction"
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

        numeric_columns = [

            "amount",
            "amount_scaled",
            "risk_score",
            "fraud_prediction",
            "fraud_probability"
        ]

        for column in numeric_columns:

            if column in df.columns:

                df[column] = pd.to_numeric(

                    df[column],

                    errors="coerce"
                )

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
        # EXPORT CSV
        # =============================================

        df.to_csv(
            EXPORT_PATH,
            index=False
        )

        # =============================================
        # FINAL OUTPUT
        # =============================================

        print(df.head())

        print(
            f"📦 Exported records: "
            f"{len(df)}"
        )

        print(
            f"📊 Fraud ratio: "
            f"{round(df['fraud_prediction'].mean(), 4)}"
        )

        print(
            f"⚠ Average risk score: "
            f"{round(df['risk_score'].mean(), 4)}"
        )

        print(
            "✅ Fraud preprocessing completed"
        )

        # =============================================
        # CLEANUP
        # =============================================

        client.close()

    except Exception as e:

        print(
            f"❌ Fraud preprocessing failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
