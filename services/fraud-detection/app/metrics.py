from prometheus_client import (
    Counter,
    Gauge,
    start_http_server
)

# =====================================================
# 🔥 BUSINESS METRICS
# =====================================================

fraud_predictions_total = Counter(
    "fraud_predictions_total",
    "Total fraud predictions"
)

fraud_detected_total = Counter(
    "fraud_detected_total",
    "Total fraud detected"
)

fraud_safe_total = Counter(
    "fraud_safe_total",
    "Total safe transactions"
)

# =====================================================
# 🔥 ML METRICS
# =====================================================

fraud_model_score = Gauge(
    "fraud_model_score",
    "Fraud model probability score"
)

fraud_transaction_amount = Gauge(
    "fraud_transaction_amount",
    "Latest transaction amount"
)

# =====================================================
# 🔥 STREAMING METRICS
# =====================================================

kafka_events_total = Counter(
    "kafka_events_total",
    "Kafka fraud events consumed"
)

mongodb_writes_total = Counter(
    "mongodb_writes_total",
    "MongoDB writes completed"
)

# =====================================================
# 🔥 START SERVER
# =====================================================

def start_metrics_server():

    print(
        "📡 Starting fraud-detection metrics on :8001",
        flush=True
    )

    start_http_server(8001)
