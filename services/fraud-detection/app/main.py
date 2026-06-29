from flask import Flask
from threading import Thread

from kafka_consumer import start

from metrics import start_metrics_server

app = Flask(__name__)

# ======================================================
# 🔥 PLATFORM INFO
# ======================================================

SERVICE_NAME = "fraud-detection"

VERSION = "5.0-enterprise"

ENVIRONMENT = "production"

AI_ENGINE = "random-forest-classifier"


# ======================================================
# 🔥 HTTP ROUTES
# ======================================================

@app.route("/")
def home():

    return {

        "service": SERVICE_NAME,

        "status": "running",

        "version": VERSION,

        "environment": ENVIRONMENT,

        "database": "mongodb",

        "streaming": "kafka",

        "mesh": "istio",

        "observability": "prometheus",

        "ai_engine": AI_ENGINE
    }


# ======================================================
# HEALTH CHECK
# ======================================================

@app.route("/health")
def health():

    return {

        "status": "healthy",

        "service": SERVICE_NAME
    }


# ======================================================
# AI ENGINE STATUS
# ======================================================

@app.route("/fraud-check")
def fraud_check():

    return {

        "message": "fraud engine active",

        "ml_inference": "enabled",

        "model": AI_ENGINE
    }


# ======================================================
# PLATFORM INFO
# ======================================================

@app.route("/platform")
def platform():

    return {

        "storage": "mongodb",

        "streaming": "kafka",

        "service_mesh": "istio",

        "monitoring": "prometheus",

        "runtime": "kubernetes",

        "pipeline": "airflow"
    }


# ======================================================
# START KAFKA CONSUMER
# ======================================================

def start_kafka():

    print(
        "📡 Starting Kafka consumer thread...",
        flush=True
    )

    start()


# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    print(
        "\n"
        "=====================================================\n"
        "🚀 AI FRAUD DETECTION SERVICE STARTED\n"
        "=====================================================\n"
        f"📦 Service      : {SERVICE_NAME}\n"
        f"🧠 Version      : {VERSION}\n"
        f"🤖 AI Engine    : {AI_ENGINE}\n"
        f"🌍 Environment  : {ENVIRONMENT}\n"
        f"🍃 Database     : MongoDB\n"
        f"📡 Streaming    : Kafka\n"
        f"📈 Monitoring   : Prometheus\n"
        f"🛰️ Mesh         : Istio\n"
        "=====================================================\n",
        flush=True
    )

    # ==================================================
    # START PROMETHEUS METRICS
    # ==================================================

    start_metrics_server()

    # ==================================================
    # START KAFKA THREAD
    # ==================================================

    kafka_thread = Thread(
        target=start_kafka,
        daemon=True
    )

    kafka_thread.start()

    # ==================================================
    # START FLASK APP
    # ==================================================

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=False,
        threaded=True,
        use_reloader=False
    )
