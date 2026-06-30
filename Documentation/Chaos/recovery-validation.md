# Recovery Validation

## Purpose

Verify that the platform successfully recovers after chaos experiments.

---

## Validate Kubernetes

```bash
kubectl get pods -A
```

---

## Validate Argo Rollouts

```bash
kubectl get rollout -A
```

---

## Validate KEDA

```bash
kubectl get scaledobject -A
```

---

## Validate HPA

```bash
kubectl get hpa -A
```

---

## Validate Airflow

```bash
kubectl get pods -n airflow
```

---

## Validate Monitoring

```bash
kubectl get pods -n monitoring
```

---

## Validate Databases

```bash
kubectl get pods -n database
```

---

## Validate Kafka

```bash
kubectl get pods -n messaging
```

---

## Observability Components

Verify:

- Prometheus
- Grafana
- Loki
- Tempo
- OpenTelemetry
- Alertmanager

---

## Success Criteria

### Infrastructure

- Healthy pods

### Messaging

- Kafka operational

### AI Platform

- Fraud Detection healthy
- Self-Healing engine healthy

### Observability

- Metrics available
- Logs available
- Traces available

### Storage

- NFS volumes mounted

### Platform Status

Recovered and stable.