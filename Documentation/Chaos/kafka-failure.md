# Kafka Failure Test

## Purpose

Validate platform resilience during messaging failures.

---

## Scenario

Kafka broker becomes unavailable.

---

## Chaos Test

```bash
kubectl delete pod -n messaging -l app=kafka
```

---

## Expected Behavior

StatefulSet recreates broker.

Consumers reconnect automatically.

Producers resume publishing.

No data corruption occurs.

---

## Validation

### Kafka Pods

```bash
kubectl get pods -n messaging
```

### Topics

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

---

## Observe

Grafana:

- Kafka throughput
- Consumer lag
- Topic metrics

---

## Success Criteria

- Kafka broker recovered
- Producers reconnect
- Consumers continue processing