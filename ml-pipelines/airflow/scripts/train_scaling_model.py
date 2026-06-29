import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# =====================================================
# CONFIG
# =====================================================

INPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/scaling_history.csv"
)

MODEL = (
    "/opt/airflow/dags/ml-pipelines/"
    "models/scaling_model.pkl"
)

FEATURE_COLUMNS = [

    "event_rate",

    "model_score"
]

TARGET_COLUMN = "replicas"

# =====================================================
# SCALING MODEL TRAINING
# =====================================================

def main():

    try:

        print("🚀 Starting scaling model training")

        # =============================================
        # VALIDATE INPUT
        # =============================================

        if not os.path.exists(INPUT):

            print(
                "❌ scaling_history.csv not found"
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
                "⚠ Empty scaling dataset"
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

            "event_rate",
            "model_score",
            "replicas"
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
                "service_name",
                "created_at"
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
        # MINIMUM DATASET SAFETY
        # =============================================

        if len(df) < 10:

            print(
                "⚠ Not enough scaling samples "
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

                random_state=42
            )
        )

        # =============================================
        # TRAIN MODEL
        # =============================================

        model = RandomForestRegressor(

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

        mae = mean_absolute_error(

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
            f"📉 Mean Absolute Error: "
            f"{round(mae, 4)}"
        )

        print(
            f"📈 Average replicas: "
            f"{round(df['replicas'].mean(), 2)}"
        )

        print(
            f"🧠 Average event rate: "
            f"{round(df['event_rate'].mean(), 2)}"
        )

        print(
            f"🎯 Average AI score: "
            f"{round(df['model_score'].mean(), 4)}"
        )

        print(
            f"💾 Model saved: {MODEL}"
        )

        print(
            "✅ Scaling ML model trained"
        )

    except Exception as e:

        print(
            f"❌ Scaling model training failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
