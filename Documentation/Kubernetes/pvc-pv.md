# Persistent Volumes and PVCs

## Storage Backend

NFS Shared Storage

---

## Consumers

### Airflow

- DAGs
- Models
- Reports

### MongoDB

- Fraud analytics

### PostgreSQL

- Metadata

### Kafka

- Event retention

### Prometheus

- Metrics

### Loki

- Logs

### Tempo

- Traces

---

## Verify PVCs

```bash
kubectl get pvc -A
```

---

## Verify PVs

```bash
kubectl get pv
```

---

## Benefits

- Shared storage
- Data persistence
- Durable workloads