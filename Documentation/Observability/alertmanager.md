# Alertmanager

## Overview

Alertmanager provides alert routing and notification management.

---

# Alert Flow

```text
Prometheus Rules
       ↓
Alertmanager
       ↓
Slack Webhook
       ↓
Operations Team
```

---

# Alert Scenarios

## Kubernetes

* Pod Crash
* Restart Loop
* High CPU
* High Memory

## Kafka

* Broker Down
* Consumer Lag

## AI Platform

* Scaling Failure
* Restart Failure
* AI Metric Anomaly

## Argo Rollouts

* Rollout Failure

---

# Verify

```bash
kubectl get pods -n monitoring
```

---

# Alert Features

* grouping
* deduplication
* routing
* severity management

---

# Slack Integration

```text
Alertmanager
       ↓
Slack Webhook
       ↓
Real-Time Notifications
```

---

# Benefits

* incident response
* proactive monitoring
* operational awareness
