# AI Metrics

## Exported Metrics

### ai_event_rate

Current events inside sliding window.

Example:

7

---

### ai_model_score

AI confidence score.

Example:

0.92

---

### ai_target_replicas

Recommended replicas.

Example:

3

---

### scaling_actions_total

Number of scale actions.

---

### restart_actions_total

Restart operations count.

---

### kafka_alerts_total

Kafka fraud alerts processed.

---

## Verify Metrics

```bash
kubectl port-forward svc/self-healing 8000:8000 -n ai-platform

curl localhost:8000/metrics
```

---

## Used By

- Prometheus
- Grafana
- KEDA
- Alertmanager