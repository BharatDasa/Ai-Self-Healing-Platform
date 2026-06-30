# Cleanup Guide

The platform performs periodic cleanup to prevent uncontrolled storage growth.

---

# PostgreSQL Cleanup

Delete records older than 6 days.

```sql
DELETE
FROM scaling_events
WHERE created_at < NOW() - INTERVAL '6 days';
```

Delete restart events:

```sql
DELETE
FROM restart_events
WHERE created_at < NOW() - INTERVAL '6 days';
```

---

# MongoDB Cleanup

Delete historical predictions:

```javascript
db.predictions.deleteMany({
  timestamp: {
    $lt: new Date(Date.now() - 6*24*60*60*1000)
  }
})
```

Collections:

* predictions
* anomalies
* transactions

---

# Kafka Retention

Topics:

* fraud-transactions
* fraud-alerts
* scaling-events
* anomaly-events
* healing-events

Retention:

```text
6 days
```

Kafka automatically removes expired messages.

---

# NFS Cleanup

Directories:

```bash
/srv/nfs/k8s/analytics
/srv/nfs/k8s/reports
/srv/nfs/k8s/models
```

Remove old files:

```bash
find /srv/nfs/k8s -type f -mtime +6 -delete
```

---

# Monitoring Cleanup

Prometheus retention:

```yaml
--storage.tsdb.retention.time=6d
```

Loki retention:

```yaml
retention_period: 144h
```

Tempo retention:

```yaml
block_retention: 144h
```

---

# Airflow Cleanup DAG

cleanup_pipeline_dag

Responsible for:

* database cleanup
* report cleanup
* model cleanup
* analytics cleanup
* retention management
