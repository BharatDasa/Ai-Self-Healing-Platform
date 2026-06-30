# Decision Engine

File

services/self-healing/app/main.py

---

## NORMAL

Condition

Low pressure

Action

No scaling

Replicas

1

---

## ELEVATED

Condition

Pressure ≥ 2

Action

Warm scaling

Replicas

2

---

## SCALE

Condition

Pressure ≥ 4

Action

High-load scaling

Replicas

3-5

---

## RESTART

Condition

current_load ≥ 50

Action

Argo Rollout restart

Replicas reset

1

---

## Full Flow

Kafka Events

↓

Sliding Window

↓

Feature Engineering

↓

ML Prediction

↓

Pressure Score

↓

Decision Engine

↓

Metrics Export

↓

Prometheus

↓

KEDA

↓

Argo Rollout

↓

Kubernetes

↓

Platform Recovery