# Scaling Failure Runbook

## Symptoms

- No new replicas
- High CPU
- Traffic backlog

---

## Verify KEDA

```bash
kubectl get scaledobject -A
```

---

## Verify HPA

```bash
kubectl get hpa -A
```

---

## Verify Prometheus Metric

```promql
max(ai_target_replicas)
```

---

## Verify Self-Healing Logs

```bash
kubectl logs deploy/self-healing -n ai-platform
```

---

## Verify Rollout

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## Recovery

Restart self-healing engine.

```bash
kubectl rollout restart deploy self-healing -n ai-platform
```

---

## Success Criteria

- Metric exported
- KEDA detects metric
- Replica count increases