import pandas as pd
import psycopg2
import os

# =====================================================
# CONFIG
# =====================================================

OUTPUT = (
    "/opt/airflow/dags/ml-pipelines/"
    "analytics/exports/anomaly_history.csv"
)

POSTGRES_CONFIG = {
    "host": "postgres.databases.svc.cluster.local",
    "database": "ai_analytics",
    "user": "psqlAdmin",
    "password": "Admin123"
}

QUERY = "SELECT * FROM restart_history"

# =====================================================
# EXPORT ANALYTICS
# =====================================================

def main():

    try:

        print("🚀 Starting analytics export")

        conn = psycopg2.connect(
            **POSTGRES_CONFIG
        )

        df = pd.read_sql(
            QUERY,
            conn
        )

        # =============================================
        # EMPTY DATASET SAFETY
        # =============================================

        if df.empty:

            print(
                "⚠ No restart history found"
            )

            os._exit(0)

        # =============================================
        # EXPORT CSV
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
            "✅ Analytics exported"
        )

        # =============================================
        # CLEANUP
        # =============================================

        conn.close()

    except Exception as e:

        print(
            f"❌ Analytics export failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
