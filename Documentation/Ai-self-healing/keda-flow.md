# KEDA Autoscaling Flow

## Architecture

Fraud Events

↓

Self-Healing Engine

↓

ai_target_replicas

↓

Prometheus

↓

KEDA ScaledObject

↓

Generated HPA

↓

Argo Rollout

↓

Fraud Detection Pods

---

## Metric

ai_target_replicas

---

## Scale Range

Minimum replicas

1

Maximum replicas

5

---

## Verify

```bash
kubectl get scaledobject -A

kubectl get hpa -A
```

---

## Benefits

- event-driven scaling
- AI-assisted autoscaling