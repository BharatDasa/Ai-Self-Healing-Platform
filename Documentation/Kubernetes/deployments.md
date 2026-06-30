# Deployments

## Application Deployments

### Self-Healing Engine

```bash
kubectl get deploy self-healing -n ai-platform
```

### Transaction Simulator

```bash
kubectl get deploy transaction-simulator -n ai-platform
```

### Airflow Components

```bash
kubectl get deploy -n airflow
```

### Grafana

```bash
kubectl get deploy grafana -n monitoring
```

---

## Verify

```bash
kubectl get deployments -A
```

---

## Benefits

- Replica management
- Rolling updates
- Self-healing