import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# =====================================================
# CONFIG
# =====================================================

INPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/feature_data.csv"
)

MODEL = (
    "/opt/airflow/dags/ml-pipelines/"
    "models/fraud_model.pkl"
)

FEATURE_COLUMNS = [

    "amount_scaled",

    "risk_score"
]

TARGET_COLUMN = "fraud_prediction"

# =====================================================
# FRAUD MODEL TRAINING
# =====================================================

def main():

    try:

        print("🚀 Starting fraud model training")

        # =============================================
        # VALIDATE INPUT FILE
        # =============================================

        if not os.path.exists(INPUT):

            print(
                "❌ feature_data.csv not found"
            )

            os._exit(1)

        # =============================================
        # LOAD DATASET
        # =============================================

        df = pd.read_csv(INPUT)

        # =============================================
        # EMPTY DATASET SAFETY
        # =============================================

        if df.empty:

            print(
                "⚠ Empty feature dataset"
            )

            return

        # =============================================
        # VALIDATE REQUIRED COLUMNS
        # =============================================

        required_columns = (

            FEATURE_COLUMNS +

            [TARGET_COLUMN]
        )

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
        # CLEAN NUMERIC DATA
        # =============================================

        numeric_columns = [

            "amount_scaled",
            "risk_score",
            "fraud_prediction"
        ]

        for column in numeric_columns:

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
        # FINAL EMPTY CHECK
        # =============================================

        if df.empty:

            print(
                "⚠ Dataset empty after cleanup"
            )

            return

        # =============================================
        # CLASS VALIDATION
        # =============================================

        unique_classes = (
            df[TARGET_COLUMN].nunique()
        )

        if unique_classes < 2:

            print(
                "⚠ Training skipped — "
                "only one fraud class detected"
            )

            return

        # =============================================
        # MINIMUM DATASET SAFETY
        # =============================================

        if len(df) < 20:

            print(
                "⚠ Not enough fraud samples "
                "for reliable ML training"
            )

            return

        # =============================================
        # BUILD FEATURES
        # =============================================

        X = df[FEATURE_COLUMNS]

        y = df[TARGET_COLUMN]

        # =============================================
        # SPLIT DATASET
        # =============================================

        X_train, X_test, y_train, y_test = (

            train_test_split(

                X,
                y,

                test_size=0.2,

                random_state=42,

                stratify=y
            )
        )

        # =============================================
        # TRAIN MODEL
        # =============================================

        model = RandomForestClassifier(

            n_estimators=100,

            random_state=42
        )

        model.fit(
            X_train,
            y_train
        )

        # =============================================
        # VALIDATE MODEL
        # =============================================

        predictions = model.predict(
            X_test
        )

        accuracy = accuracy_score(

            y_test,

            predictions
        )

        # =============================================
        # SAVE MODEL
        # =============================================

        joblib.dump(
            model,
            MODEL
        )

        # =============================================
        # FINAL OUTPUT
        # =============================================

        print(
            f"📊 Training rows: {len(df)}"
        )

        print(
            f"🎯 Model accuracy: "
            f"{round(accuracy, 4)}"
        )

        print(
            f"📈 Fraud ratio: "
            f"{round(df['fraud_prediction'].mean(), 4)}"
        )

        print(
            f"💰 Avg risk score: "
            f"{round(df['risk_score'].mean(), 4)}"
        )

        print(
            f"💾 Model saved: {MODEL}"
        )

        print(
            "✅ Fraud ML model trained"
        )

    except Exception as e:

        print(
            f"❌ Fraud model training failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
