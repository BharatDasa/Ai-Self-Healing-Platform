# Pod Restart Runbook

## Purpose

Recover unhealthy workloads.

---

## Identify Pods

```bash
kubectl get pods -n ai-platform
```

---

## Restart Deployment

```bash
kubectl rollout restart deploy self-healing -n ai-platform

kubectl rollout restart deploy transaction-simulator -n ai-platform
```

---

## Restart Rollout

```bash
kubectl argo rollouts restart fraud-detection -n ai-platform
```

---

## Verify

```bash
kubectl get pods -n ai-platform
```

---

## Monitor

- Grafana
- Prometheus
- Loki
- Tempo

---

## Success Criteria

- Pods Running
- No CrashLoopBackOff
- Metrics Available