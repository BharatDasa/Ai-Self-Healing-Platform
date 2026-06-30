# DockerHub Registry

## Overview

DockerHub stores platform container images.

---

## Images

| Image | Purpose |
|---------|---------|
| fraud_ai_ml | Fraud Detection |
| self-healing_ai_ml | AI Recovery Engine |
| transaction-simulator | Event Generator |
| enterprise-airflow | MLOps |

---

## Push Images

```bash
docker push bharatdasa/fraud_ai_ml:latest

docker push bharatdasa/self-healing_ai_ml:v2

docker push bharatdasa/transaction-simulator:v1

docker push bharatdasa/enterprise-airflow:latest
```

---

## Pull Images

```bash
docker pull bharatdasa/fraud_ai_ml:latest
```

---

## Verify

```bash
docker images
```