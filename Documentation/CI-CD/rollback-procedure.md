# Rollback Procedure

## Purpose

Recover from failed deployments.

---

## Verify Rollout

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## Rollback

```bash
kubectl argo rollouts undo fraud-detection -n ai-platform
```

---

## Restart Rollout

```bash
kubectl argo rollouts restart fraud-detection -n ai-platform
```

---

## Verify Pods

```bash
kubectl get pods -n ai-platform
```

---

## Observe

- Grafana
- Prometheus
- Loki
- Tempo

---

## Success Criteria

- Healthy pods
- Metrics available
- Traffic restored
- No errors