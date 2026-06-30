# Kafka Producers

## Transaction Simulator

Produces fraud events continuously.

---

## Flow

Transaction Simulator

↓

Kafka Producer

↓

fraud-transactions topic

---

## Event Example

```json
{
  "transaction_id":"TXN-1001",
  "amount":9500,
  "country":"US"
}
```

---

## Verify Producer Logs

```bash
kubectl logs deploy/transaction-simulator -n ai-platform
```

---

## Benefits

- continuous traffic generation
- realistic workload simulation