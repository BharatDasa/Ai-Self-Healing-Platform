# Kafka Storage

## Purpose

Kafka provides durable event streaming.

Topics:

- fraud-transactions
- fraud-alerts
- scaling-events
- anomaly-events
- healing-events

---

## Architecture

Producer
    ↓
Kafka StatefulSet
    ↓
PVC
    ↓
NFS

---

## Verify

kubectl get pods -n messaging

kubectl get pvc -n messaging

---

## Benefits

- durable events
- replay capability
- fault tolerance

---

## Retention

6 days

retention.ms=518400000