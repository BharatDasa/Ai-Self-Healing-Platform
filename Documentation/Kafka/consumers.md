# Kafka Consumers

## Fraud Detection Consumer

Consumes:

fraud-transactions

Performs:

- AI inference
- fraud scoring
- MongoDB storage
- metrics export

---

## Self-Healing Consumer

Consumes:

fraud-alerts

Performs:

- anomaly detection
- pressure analysis
- scaling decisions
- restart decisions

---

## Flow

Kafka Topics

↓

Fraud Detection Service

↓

Fraud Alerts

↓

Self-Healing Engine

---

## Verify

```bash
kubectl logs deploy/fraud-detection -n ai-platform

kubectl logs deploy/self-healing -n ai-platform
```