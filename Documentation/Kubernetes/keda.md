# KEDA Autoscaling

## Overview

KEDA scales fraud-detection Rollouts using Prometheus metrics.

---

## Metric

ai_target_replicas

---

## Scale Range

Minimum replicas:

1

Maximum replicas:

5

---

## Verify

```bash
kubectl get scaledobject -A

kubectl describe scaledobject fraud-prometheus-keda -n ai-platform
```

---

## Scaling Flow

Self-Healing Engine

↓

Prometheus Metric

↓

KEDA

↓

HPA

↓

Argo Rollout

↓

Pods

---

## Benefits

- Event-driven scaling
- AI-assisted autoscaling