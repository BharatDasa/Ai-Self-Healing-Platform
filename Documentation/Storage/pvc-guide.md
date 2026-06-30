# PVC Guide

## Overview

PersistentVolumeClaims provide storage to stateful workloads.

---

# Flow

```text
Application
     ↓
PVC
     ↓
PV
     ↓
NFS
```

---

# PVC Consumers

## MongoDB

```text
mongodb-pvc
```

## PostgreSQL

```text
postgres-pvc
```

## Kafka

```text
kafka-pvc
```

## Airflow

```text
airflow-pvc
```

---

# Verify

```bash
kubectl get pvc -A

kubectl describe pvc
```

---

# Benefits

* persistent storage
* storage abstraction
* workload portability
