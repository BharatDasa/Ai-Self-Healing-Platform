import pandas as pd
import psycopg2
import os

# =====================================================
# CONFIG
# =====================================================

OUTPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/scaling_history.csv"
)

POSTGRES_CONFIG = {

    "host": "postgres.databases.svc.cluster.local",

    "database": "ai_analytics",

    "user": "psqlAdmin",

    "password": "Admin123"
}

QUERY = """

    SELECT
        service_name,
        action,
        replicas,
        model_score,
        event_rate,
        created_at

    FROM scaling_history

    ORDER BY created_at DESC

"""

# =====================================================
# SCALING ANALYTICS EXPORT
# =====================================================

def main():

    conn = None

    try:

        print("🚀 Starting scaling analytics export")

        # =============================================
        # CONNECT TO POSTGRES
        # =============================================

        conn = psycopg2.connect(
            **POSTGRES_CONFIG
        )

        print("✅ Connected to PostgreSQL")

        # =============================================
        # LOAD SCALING DATA
        # =============================================

        df = pd.read_sql(
            QUERY,
            conn
        )

        # =============================================
        # EMPTY DATASET SAFETY
        # =============================================

        if df.empty:

            print("⚠ No scaling history found")

            empty_df = pd.DataFrame(columns=[

                "service_name",
                "action",
                "replicas",
                "model_score",
                "event_rate",
                "created_at"
            ])

            empty_df.to_csv(
                OUTPUT,
                index=False
            )

            print(
                "✅ Empty scaling dataset exported"
            )

            return

        # =============================================
        # DATA CLEANING
        # =============================================

        numeric_columns = [

            "replicas",
            "model_score",
            "event_rate"
        ]

        for column in numeric_columns:

            df[column] = pd.to_numeric(

                df[column],

                errors="coerce"
            )

        df = df.dropna()

        # =============================================
        # DUPLICATE CLEANUP
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
        # EXPORT ANALYTICS
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
            f"📦 Exported rows: {len(df)}"
        )

        print(
            f"📈 Average replicas: "
            f"{round(df['replicas'].mean(), 2)}"
        )

        print(
            f"🧠 Average AI score: "
            f"{round(df['model_score'].mean(), 4)}"
        )

        print(
            f"📊 Average event rate: "
            f"{round(df['event_rate'].mean(), 2)}"
        )

        print("✅ Scaling analytics exported")

    except Exception as e:

        print(
            f"❌ Scaling analytics export failed: {e}"
        )

        raise

    finally:

        if conn:

            conn.close()


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
