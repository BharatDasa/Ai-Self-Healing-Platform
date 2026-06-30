# Loki

Loki provides centralized logging.

## Sources

* Fraud Detection
* Self-Healing Engine
* Kafka
* Airflow
* Istio
* Prometheus
* Grafana

## Collection

```text
Pods
 ↓
Promtail
 ↓
Loki
 ↓
Grafana Explore
```

## Verify

```bash
kubectl get pods -n monitoring
```

## Log Search

Example:

```text
{namespace="ai-platform"}

{app="fraud"}

{app="self-healing"}
```

Loki stores platform logs efficiently.
