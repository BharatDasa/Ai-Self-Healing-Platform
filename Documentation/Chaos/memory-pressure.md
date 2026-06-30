# Memory Pressure Test

## Purpose

Validate workload stability under memory stress.

---

## Scenario

Pods experience excessive memory consumption.

---

## Stress Command

```bash
stress --vm 1 --vm-bytes 500M --timeout 120
```

---

## Expected Behavior

Memory usage increases.

Prometheus metrics rise.

Alertmanager may trigger notifications.

Grafana visualizes pressure.

---

## Validation

```bash
kubectl top pods -n ai-platform
```

---

## Observe

Grafana dashboards:

- Memory utilization
- Pod restarts
- Replica changes

---

## Success Criteria

- Metrics collected
- Alerts generated
- Platform remains operational