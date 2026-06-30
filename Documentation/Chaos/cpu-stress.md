# CPU Stress Test

## Purpose

Validate autoscaling and anomaly detection.

---

## Scenario

Artificial CPU load is injected into workloads.

---

## Stress Test

```bash
kubectl exec -it POD_NAME -- stress --cpu 2 --timeout 120
```

---

## Expected Results

CPU utilization increases.

Prometheus records higher metrics.

AI self-healing engine evaluates pressure.

KEDA performs scaling operations.

---

## Validation

```bash
kubectl top pods -n ai-platform
```

---

## Observe

Grafana:

- CPU usage
- Replica count
- AI metrics

---

## Success Criteria

- CPU metrics increase
- Scaling recommendation generated
- Workload remains healthy