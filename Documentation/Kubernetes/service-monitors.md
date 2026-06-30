# ServiceMonitor

## Purpose

Prometheus Operator uses ServiceMonitors to discover targets.

---

## Targets

### Fraud Detection

Metrics Port

8001

### Self-Healing Engine

Metrics Port

8000

### Kafka

Exporter metrics

### Istio

Mesh telemetry

---

## Verify

```bash
kubectl get servicemonitor -A
```

---

## Benefits

- Automatic scraping
- Dynamic discovery