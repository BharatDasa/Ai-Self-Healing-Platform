# Prometheus

Prometheus provides metrics collection and AI metric ingestion.

## Responsibilities

* scrape Kubernetes metrics
* scrape application metrics
* collect AI metrics
* evaluate alert rules

## AI Metrics

* ai_event_rate
* ai_model_score
* ai_target_replicas
* scaling_actions_total
* restart_actions_total

## Verify

```bash
kubectl get pods -n monitoring

kubectl port-forward svc/prometheus-operated 9090
```

Open:

```text
http://localhost:9090
```

## Queries

```promql
ai_target_replicas

ai_model_score

rate(kafka_events_total[5m])
```

Prometheus acts as the central metric engine of the platform.
