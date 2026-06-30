# ServiceMonitor

## Overview

ServiceMonitor resources enable Prometheus Operator to discover application metrics automatically.

---

# Flow

Applications
      ↓
Service
      ↓
ServiceMonitor
      ↓
Prometheus Operator
      ↓
Prometheus
      ↓
Grafana

---

# Monitored Components

## Fraud Detection

Metrics Port:

8001

Metrics:

- fraud_model_score
- kafka_events_total
- fraud_predictions_total

---

## Self-Healing Engine

Metrics Port:

8000

Metrics:

- ai_event_rate
- ai_model_score
- ai_target_replicas
- scaling_actions_total
- restart_actions_total

---

## Kafka Exporter

Metrics:

- broker health
- consumer lag
- throughput

---

## MongoDB Exporter

Metrics:

- connections
- memory
- operations

---

## PostgreSQL Exporter

Metrics:

- transactions
- query latency
- connections

---

# Verify

kubectl get servicemonitor -A

kubectl describe servicemonitor

---

# Example

apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor

---

# Benefits

- automatic discovery
- no manual scrape configs
- Prometheus integration
- centralized monitoring