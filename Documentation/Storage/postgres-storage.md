# PostgreSQL Storage

## Purpose

PostgreSQL stores:

* Airflow metadata
* scheduler state
* workflow history
* scaling events
* restart events

---

# Architecture

```text
Airflow
      ↓
PostgreSQL StatefulSet
      ↓
PVC
      ↓
NFS
```

---

# Verify

```bash
kubectl get pods -n database

kubectl get pvc -n database
```

---

# Backup

```bash
pg_dump postgres > backup.sql
```

---

# Restore

```bash
psql postgres < backup.sql
```

---

# Retention

Default:

```text
6 days
```
