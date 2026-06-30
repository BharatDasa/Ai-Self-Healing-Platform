# Retention Policy

## Purpose

Prevent unlimited storage growth.

---

# PostgreSQL

Retention:

6 days

Cleanup:

DELETE old records.

---

# MongoDB

Retention:

6 days

Cleanup:

TTL indexes.

---

# Kafka

Retention:

6 days

Automatic deletion:

retention.ms=518400000

---

# Prometheus

Retention:

6 days

---

# Loki

Retention:

6 days

---

# Tempo

Retention:

6 days

---

# Analytics

Delete files older than 6 days.

```bash
find /srv/nfs/k8s -type f -mtime +6 -delete