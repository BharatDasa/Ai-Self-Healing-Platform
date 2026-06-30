# Cleanup Pipeline

The platform includes automated housekeeping and retention management.

The cleanup pipeline prevents uncontrolled storage growth and maintains healthy infrastructure.

Cleanup operations are orchestrated using:

```text
cleanup_pipeline_dag
```

---

# Pipeline Flow

```text
Airflow Scheduler
        ↓
cleanup_pipeline_dag
        ↓
Database Cleanup
        ↓
Kafka Retention
        ↓
Analytics Cleanup
        ↓
Model Cleanup
        ↓
NFS Cleanup
        ↓
Platform Maintenance
```

---

# PostgreSQL Cleanup

Tables cleaned:

* scaling_events
* restart_events
* analytics_history
* Airflow metadata

Example:

```sql
DELETE
FROM scaling_events
WHERE created_at < NOW() - INTERVAL '6 days';
```

---

# MongoDB Cleanup

Collections cleaned:

* predictions
* transactions
* anomalies

Example:

```javascript
db.predictions.deleteMany({
 timestamp: {
  $lt: new Date(Date.now() - 6*24*60*60*1000)
 }
})
```

TTL indexes are recommended.

---

# Kafka Retention

Topics:

```text
fraud-transactions

fraud-alerts

scaling-events

anomaly-events

healing-events
```

Retention:

```text
6 days
```

Example:

```text
retention.ms = 518400000
```

Kafka automatically removes old messages.

---

# Analytics Cleanup

Old files removed:

```text
fraud_history.csv

anomaly_history.csv

scaling_history.csv

feature_data.csv
```

---

# Model Cleanup

Old model versions removed:

```text
fraud_model.pkl

scaling_model.pkl
```

Older versions are deleted automatically.

---

# NFS Storage Cleanup

Directories:

```text
analytics/

reports/

models/

exports/
```

Example:

```bash
find /srv/nfs/k8s/analytics \
-type f \
-mtime +6 \
-delete
```

---

# Prometheus Retention

Metrics retention:

```text
6 days
```

---

# Loki Retention

Log retention:

```text
6 days
```

---

# Tempo Retention

Trace retention:

```text
6 days
```

---

# Benefits

Automated cleanup provides:

* lower storage consumption
* healthier databases
* faster queries
* smaller Kafka volumes
* reduced NFS growth
* better platform stability

---

# Enterprise Maintenance Architecture

```text
Airflow Scheduler
        ↓
cleanup_pipeline_dag
        ↓
PostgreSQL Cleanup
        ↓
MongoDB Cleanup
        ↓
Kafka Retention
        ↓
CSV Cleanup
        ↓
Model Cleanup
        ↓
NFS Cleanup
        ↓
Healthy Platform
```

---

# Future Improvements

Planned enhancements:

* model versioning
* S3 archive storage
* backup retention policies
* automated compression
* cold storage migration
* lifecycle management

The cleanup pipeline ensures long-term sustainability of the AI Self-Healing Kubernetes Platform.
