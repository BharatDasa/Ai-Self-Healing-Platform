# Maintenance Guide

# Daily Checks

Verify cluster health:

```bash
kubectl get pods -A

kubectl get svc -A
```

Verify:

* Kafka
* MongoDB
* PostgreSQL
* Airflow
* Grafana
* Prometheus
* Loki
* Tempo

---

# Weekly Checks

Check storage:

```bash
df -h
```

Verify:

* NFS utilization
* database growth
* Kafka persistence
* dashboards
* traces

---

# Monthly Maintenance

Clean Docker:

```bash
docker system prune -af
```

Clean old analytics:

```bash
find /srv/nfs/k8s -mtime +30 -delete
```

Run:

```bash
./scripts/validation.sh
```

---

# Quarterly Maintenance

Upgrade:

* Kubernetes
* Helm charts
* Grafana
* Prometheus
* Loki
* Tempo
* Airflow

---

# Chaos Validation

Run:

```bash
./scripts/resilience-test.sh
```

Validate:

* pod recovery
* KEDA scaling
* Argo Rollouts
* restart engine

---

# Backup Verification

Verify:

* NFS backups
* PostgreSQL backups
* MongoDB backups

---

# Certificate Maintenance

Renew:

* cert-manager certificates
* wildcard TLS certificates

---

# Platform Health Checklist

✓ Kubernetes healthy

✓ Monitoring healthy

✓ Databases healthy

✓ Kafka healthy

✓ Airflow healthy

✓ KEDA healthy

✓ Argo Rollouts healthy

✓ Istio healthy

✓ AI services healthy

✓ NFS storage healthy

The objective of maintenance is to ensure continuous reliability of the AI Self-Healing Kubernetes Platform.
