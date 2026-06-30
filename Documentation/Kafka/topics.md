# Kafka Topics

## Topics Used

### fraud-transactions

Incoming transactions.

---

### fraud-alerts

High-risk fraud events.

---

### scaling-events

Scaling recommendations.

---

### healing-events

Recovery actions.

---

### anomaly-events

Detected anomalies.

---

### telemetry-events

Telemetry exports.

---

## Verify Topics

```bash
kubectl exec -it kafka-0 -n messaging -- \
kafka-topics.sh \
--bootstrap-server localhost:9092 \
--list
```

---

## Topic Architecture

Transaction Simulator

↓

fraud-transactions

↓

Fraud Detection

↓

fraud-alerts

↓

Self-Healing Engine

↓

scaling-events

↓

KEDA