# MongoDB Storage

## Purpose

MongoDB stores:

- fraud predictions
- anomaly events
- transaction history
- analytics

---

## Architecture

Fraud Detection
       ↓
MongoDB StatefulSet
       ↓
PVC
       ↓
NFS

---

## Verify

kubectl get pods -n database

kubectl get pvc -n database

---

## Backup

mongodump

---

## Restore

mongorestore backup/

---

## Collections

- predictions
- anomalies
- transactions

---

## Retention

6 days