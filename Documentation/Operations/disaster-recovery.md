# Disaster Recovery Guide

This platform uses NFS shared storage for all components.

---

# Critical Components

* MongoDB
* PostgreSQL
* Kafka
* Airflow
* Prometheus
* Grafana
* Loki
* Tempo

---

# Backup NFS

```bash
tar czvf backup.tar.gz /srv/nfs/k8s
```

---

# MongoDB Restore

```bash
mongorestore backup/
```

---

# PostgreSQL Restore

```bash
psql postgres < backup.sql
```

---

# Kafka Recovery

Restart StatefulSets:

```bash
kubectl rollout restart sts kafka -n messaging
```

---

# Restore Airflow

```bash
kubectl rollout restart deploy airflow-webserver -n airflow
kubectl rollout restart deploy airflow-scheduler -n airflow
```

---

# Restore Monitoring

```bash
kubectl rollout restart deploy grafana -n monitoring

kubectl rollout restart sts prometheus-operated -n monitoring

kubectl rollout restart sts loki -n monitoring

kubectl rollout restart sts tempo -n monitoring
```

---

# Full Cluster Recovery

```bash
./scripts/deploy.sh

cd ml-pipelines

./deploy-ml-pipelines.sh
```

---

# Validation

```bash
kubectl get pods -A

kubectl get scaledobject -A

kubectl get rollout -A
```

Goal:

Restore platform with minimal downtime.
