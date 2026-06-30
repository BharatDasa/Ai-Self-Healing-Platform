# NFS Storage Architecture

## Overview

The AI Self-Healing Kubernetes Platform uses a centralized NFS server for persistent storage.

All stateful components use Kubernetes Persistent Volumes backed by NFS.

---

# Architecture

```text
Applications
      ↓
Persistent Volume Claims
      ↓
Persistent Volumes
      ↓
NFS Shared Storage
```

---

# Components Using NFS

* PostgreSQL
* MongoDB
* Kafka
* Airflow
* Prometheus
* Grafana
* Loki
* Tempo
* Analytics Exports
* ML Models
* Reports

---

# Benefits

* centralized storage
* persistent workloads
* simplified backup
* shared storage
* recovery support

---

# Verify

```bash
kubectl get pv

kubectl get pvc -A
```

---

# NFS Location

```text
/srv/nfs/k8s
```
