# StatefulSets

## Components

### Kafka

```bash
kubectl get sts kafka -n messaging
```

### PostgreSQL

```bash
kubectl get sts postgres -n airflow
```

### Prometheus

```bash
kubectl get sts prometheus -n monitoring
```

### Loki

```bash
kubectl get sts loki -n monitoring
```

### Tempo

```bash
kubectl get sts tempo -n monitoring
```

### MongoDB

```bash
kubectl get sts mongodb -n ai-platform
```

---

## Verify

```bash
kubectl get sts -A
```

---

## Benefits

- Stable identity
- Persistent storage
- Ordered startup