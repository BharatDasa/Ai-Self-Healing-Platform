from prometheus_client import (
    Counter,
    Gauge,
    start_http_server
)

# =====================================================
# AI METRICS
# =====================================================

ai_event_rate = Gauge(
    "ai_event_rate",
    "Events processed in active window"
)

ai_model_score = Gauge(
    "ai_model_score",
    "Scaling ML confidence score"
)

ai_target_replicas = Gauge(
    "ai_target_replicas",
    "Predicted replicas from ML model"
)

# =====================================================
# ACTION METRICS
# =====================================================

scaling_actions_total = Counter(
    "scaling_actions_total",
    "Total scaling actions"
)

restart_actions_total = Counter(
    "restart_actions_total",
    "Total rollout restart actions"
)

# =====================================================
# KAFKA METRICS
# =====================================================

kafka_alerts_total = Counter(
    "kafka_alerts_total",
    "Kafka fraud alerts received"
)

kafka_errors_total = Counter(
    "kafka_errors_total",
    "Kafka processing errors"
)

# =====================================================
# DATABASE METRICS
# =====================================================

postgres_writes_total = Counter(
    "postgres_writes_total",
    "PostgreSQL analytics writes"
)

# =====================================================
# START SERVER
# =====================================================

def start_metrics_server():

    print(
        "📡 Starting Prometheus metrics on :8000",
        flush=True
    )

    start_http_server(8000)
