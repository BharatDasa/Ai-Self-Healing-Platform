import psycopg2

from psycopg2 import OperationalError

from metrics import postgres_writes_total

# ======================================================
# POSTGRES CONFIG
# ======================================================

POSTGRES_HOST = "postgres.databases.svc.cluster.local"

POSTGRES_DATABASE = "ai_analytics"

POSTGRES_USER = "psqlAdmin"

POSTGRES_PASSWORD = "Admin123"

# ======================================================
# GLOBAL CONNECTION
# ======================================================

conn = None

# ======================================================
# CONNECT TO POSTGRES
# ======================================================

def connect_postgres():

    global conn

    try:

        conn = psycopg2.connect(

            host=POSTGRES_HOST,

            database=POSTGRES_DATABASE,

            user=POSTGRES_USER,

            password=POSTGRES_PASSWORD
        )

        conn.autocommit = True

        print(
            "✅ Connected to PostgreSQL",
            flush=True
        )

    except OperationalError as e:

        print(
            f"❌ PostgreSQL connection failed: {e}",
            flush=True
        )

        raise

# ======================================================
# INITIAL CONNECTION
# ======================================================

connect_postgres()

# ======================================================
# HEALTH CHECK
# ======================================================

def ensure_connection():

    global conn

    try:

        conn.cursor().execute("SELECT 1")

    except Exception:

        print(
            "⚠ PostgreSQL connection lost "
            "→ reconnecting",
            flush=True
        )

        connect_postgres()

# ======================================================
# STORE SCALING EVENT
# ======================================================

def save_scaling_event(
    service_name,
    action,
    replicas,
    score,
    event_rate
):

    cur = None

    try:

        ensure_connection()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO scaling_history (
                service_name,
                action,
                replicas,
                model_score,
                event_rate
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                service_name,
                action,
                replicas,
                score,
                event_rate
            )
        )

        postgres_writes_total.inc()

        print(
            f"📈 Scaling event stored "
            f"({action})",
            flush=True
        )

    except Exception as e:

        print(
            f"❌ Failed to store scaling event: {e}",
            flush=True
        )

    finally:

        if cur:

            cur.close()

# ======================================================
# STORE RESTART EVENT
# ======================================================

def save_restart_event(
    service_name,
    reason,
    score
):

    cur = None

    try:

        ensure_connection()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO restart_history (
                service_name,
                reason,
                model_score
            )
            VALUES (%s, %s, %s)
            """,
            (
                service_name,
                reason,
                score
            )
        )

        postgres_writes_total.inc()

        print(
            "🔄 Restart event stored",
            flush=True
        )

    except Exception as e:

        print(
            f"❌ Failed to store restart event: {e}",
            flush=True
        )

    finally:

        if cur:

            cur.close()
