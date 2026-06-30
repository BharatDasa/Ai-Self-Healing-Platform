# Restart Engine

## Purpose

Recover workloads during extreme anomaly pressure.

---

## Threshold

RESTART_LOAD = 50

---

## Flow

Current Load ≥ 50

↓

Decision = RESTART

↓

Argo Rollout Restart

↓

Pods recreated

↓

Recovery completed

---

## Verify

```bash
kubectl argo rollouts restart fraud-detection -n ai-platform
```

---

## Metrics

restart_actions_total