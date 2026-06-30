# AI Scaling Events

## Flow

Fraud Events

↓

Self-Healing Engine

↓

Pressure Score

↓

Decision Engine

↓

Prometheus Metrics

↓

KEDA

↓

Argo Rollouts

↓

Scale Pods

---

## Scaling Metric

ai_target_replicas

---

## Decisions

NORMAL

1 replica

---

ELEVATED

2 replicas

---

SCALE

3-5 replicas

---

## Example Logs

```text
📊 Pressure Score : 4

🤖 ML Decision : SCALE

📈 Suggested Scale : 4

📡 KEDA consuming AI metric

🛰️ Argo Rollouts scaling workload
```

---

## Verify

```bash
kubectl logs deploy/self-healing -n ai-platform

kubectl get hpa -A

kubectl get scaledobject -A
```

---

## Benefits

- AI-assisted autoscaling
- event-driven scaling
- autonomous infrastructure