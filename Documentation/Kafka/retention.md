# Kafka Retention

## Purpose

Prevent unlimited disk growth.

Kafka stores events on NFS.

---

## Retention Policy

Retention Time

7 days

Retention Size

2GB

---

## Example Configuration

```properties
log.retention.hours=168

log.retention.bytes=2147483648
```

---

## Verify

```bash
kubectl exec -it kafka-0 -n messaging -- \
cat /opt/bitnami/kafka/config/server.properties | grep retention
```

---

## Cleanup

Kafka automatically deletes old segments.

No manual cleanup required.

---

## Benefits

- storage protection
- automatic retention
- controlled growth