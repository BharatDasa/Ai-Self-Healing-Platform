# Pod Delete Chaos Test

## Purpose

Validate Kubernetes self-healing capabilities and workload recovery.

---

## Scenario

A running pod is unexpectedly terminated.

The platform should automatically recover and restore desired state.

---

## Test Command

```bash
kubectl delete pod -n ai-platform -l app=fraud
```

---

## Expected Behavior

Argo Rollouts detects missing replicas.

Kubernetes schedules a new pod.

Service availability remains intact.

Traffic continues flowing through Istio.

---

## Validation

```bash
kubectl get pods -n ai-platform -w
```

---

## Verify

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## Observability

Monitor:

- Grafana dashboards
- Prometheus targets
- Tempo traces
- Loki logs

---

## Success Criteria

- New pod created
- No service outage
- Metrics continue flowing
- Platform stabilized