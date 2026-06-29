from pymongo import MongoClient
import psycopg2

# =====================================================
# CONFIG
# =====================================================

MONGO_URI = (
    "mongodb://mongodbAdmin:Admin123@"
    "mongodb.databases.svc.cluster.local:27017/"
)

POSTGRES_CONFIG = {
    "host": "postgres.databases.svc.cluster.local",
    "database": "ai_analytics",
    "user": "psqlAdmin",
    "password": "Admin123"
}

# =====================================================
# CLEANUP JOB
# =====================================================

def main():

    try:

        print("🚀 Starting cleanup workflow")

        # =============================================
        # MONGODB CLEANUP
        # =============================================

        mongo = MongoClient(MONGO_URI)

        db = mongo["fraud_detection"]

        fraud_deleted = (
            db.fraud_events.delete_many({})
        )

        prediction_deleted = (
            db.predictions.delete_many({})
        )

        print(
            f"🧹 Mongo fraud_events deleted: "
            f"{fraud_deleted.deleted_count}"
        )

        print(
            f"🧹 Mongo predictions deleted: "
            f"{prediction_deleted.deleted_count}"
        )

        # =============================================
        # POSTGRES CLEANUP
        # =============================================

        conn = psycopg2.connect(
            **POSTGRES_CONFIG
        )

        cur = conn.cursor()

        cur.execute(
            "DELETE FROM scaling_history"
        )

        scaling_deleted = cur.rowcount

        cur.execute(
            "DELETE FROM restart_history"
        )

        restart_deleted = cur.rowcount

        conn.commit()

        print(
            f"🧹 PostgreSQL scaling_history deleted: "
            f"{scaling_deleted}"
        )

        print(
            f"🧹 PostgreSQL restart_history deleted: "
            f"{restart_deleted}"
        )

        # =============================================
        # CLOSE CONNECTIONS
        # =============================================

        cur.close()

        conn.close()

        mongo.close()

        # =============================================
        # SUCCESS
        # =============================================

        print(
            "✅ Old platform data cleaned successfully"
        )

    except Exception as e:

        print(
            f"❌ Cleanup pipeline failed: {e}"
        )

        raise


# =====================================================
# ENTRYPOINT
# =====================================================

if __name__ == "__main__":

    main()
