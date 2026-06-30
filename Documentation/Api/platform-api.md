# Platform API

## Overview

Provides platform metadata and component information.

---

# Endpoint

```http
GET /platform
```

---

# Response

```json
{
  "storage": "mongodb",
  "streaming": "kafka",
  "service_mesh": "istio",
  "monitoring": "prometheus",
  "runtime": "kubernetes",
  "pipeline": "airflow"
}
```

---

# Platform Components

## Storage

- MongoDB
- PostgreSQL
- NFS

---

## Streaming

- Kafka

---

## Service Mesh

- Istio
- Envoy Sidecars

---

## Observability

- Prometheus
- Grafana
- Loki
- Tempo
- OpenTelemetry
- Alertmanager

---

## MLOps

- Airflow
- Feature Engineering
- Model Training
- Drift Detection

---

## Autoscaling

- KEDA
- HPA

---

## Progressive Delivery

- Argo Rollouts

---

## Verify

```bash
curl http://localhost:8000/platform
```

---

# Architecture

```text
Fraud Detection Service
        ↓
MongoDB
        ↓
Kafka
        ↓
Prometheus
        ↓
Istio
        ↓
Kubernetes
        ↓
Airflow
```