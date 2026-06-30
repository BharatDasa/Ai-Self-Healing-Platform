# Fraud Detection API

## Overview

The Fraud Detection Service provides REST APIs for platform information and AI fraud inference.

---

# Base URL

```text
http://fraud-detection.ai-platform.svc.cluster.local:8000
```

---

# Available Endpoints

| Endpoint | Method | Purpose |
|------------|--------|----------|
| / | GET | Platform information |
| /health | GET | Health check |
| /fraud-check | GET | AI engine status |
| /platform | GET | Platform metadata |

---

# Root Endpoint

## Request

```http
GET /
```

---

## Response

```json
{
  "service": "fraud-detection",
  "status": "running",
  "version": "5.0-enterprise",
  "environment": "production",
  "database": "mongodb",
  "streaming": "kafka",
  "mesh": "istio",
  "observability": "prometheus",
  "ai_engine": "random-forest-classifier"
}
```

---

# Fraud Engine Endpoint

## Request

```http
GET /fraud-check
```

---

## Response

```json
{
  "message": "fraud engine active",
  "ml_inference": "enabled",
  "model": "random-forest-classifier"
}
```

---

# Platform Components

- Flask
- Kafka
- MongoDB
- Prometheus
- Istio
- Kubernetes

---

# Verify

```bash
curl http://localhost:8000/
```