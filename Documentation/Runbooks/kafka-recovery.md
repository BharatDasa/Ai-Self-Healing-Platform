# Kafka Recovery Runbook

## Symptoms

- Consumer failures
- Event loss
- Producer timeout

---

## Check Brokers

```bash
kubectl get pods -n messaging
```

---

## Restart Kafka

```bash
kubectl rollout restart sts kafka -n messaging
```

---

## Verify Topics

```bash
kafka-topics.sh \
--bootstrap-server localhost:9092 \
--list
```

---

## Verify Logs

```bash
kubectl logs kafka-0 -n messaging
```

---

## Monitor

Grafana:

- Kafka throughput
- Consumer lag
- Message rate

---

## Success Criteria

- Topics available
- Producers connected
- Consumers healthy