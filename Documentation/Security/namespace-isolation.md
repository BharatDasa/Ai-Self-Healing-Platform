# Namespace Isolation

## Overview

The platform separates workloads using Kubernetes namespaces.

---

## Namespaces

### ai-platform

Contains:

- fraud-detection
- self-healing
- transaction-simulator

---

### airflow

Contains:

- webserver
- scheduler
- workers
- flower

---

### monitoring

Contains:

- Prometheus
- Grafana
- Loki
- Tempo
- Alertmanager
- Promtail

---

### database

Contains:

- PostgreSQL
- MongoDB

---

### messaging

Contains:

- Kafka

---

## Verify

```bash
kubectl get ns
```

---

## Benefits

- workload separation
- better security
- easier operations
- fault isolation