# 🚀 How KEDA Autoscaling Works in Our AI Self-Healing Platform

# 🌍 High-Level Overview

Our platform uses an AI-driven autoscaling architecture built on:

* Kafka
* Prometheus
* KEDA
* Argo Rollouts
* Kubernetes
* AI-based anomaly analysis

Instead of scaling only on CPU or memory like traditional HPA, our system scales based on:

* fraud event pressure
* anomaly intensity
* AI prediction scores
* workload saturation
* live streaming traffic

---

# 🌊 Complete Scaling Flow

```text
Transaction Simulator
        ↓
Kafka Topics
        ↓
Self-Healing Kafka Consumer
        ↓
Sliding Event Window
        ↓
AI Feature Engineering
        ↓
Pressure Score Calculation
        ↓
Replica Recommendation
        ↓
Prometheus Custom Metrics
        ↓
KEDA Prometheus Trigger
        ↓
Argo Rollouts Scaling
        ↓
Fraud-Detection Pods Scale
```

---

# 🧠 Step 1 — Fraud Events Enter Kafka

The transaction simulator continuously generates fraud-like transactions.

Example:

```json
{
  "transaction_id": "TXN-1001",
  "amount": 15000
}
```

These events are pushed into Kafka topics such as:

* fraud-transactions
* fraud-alerts
* anomaly-events

---

# 🧠 Step 2 — Self-Healing Engine Consumes Events

The self-healing service consumes Kafka events in real time.

Inside `main.py`:

```python
start(process)
```

Each Kafka event enters:

```python
process(event)
```

---

# 🧠 Step 3 — Sliding Event Window

The platform stores recent events in memory:

```python
event_buffer.append(event)
```

Old events are automatically removed:

```python
cleanup_old_events(now)
```

Window duration:

```python
WINDOW_SECONDS = 60
```

This creates a real-time traffic analysis window.

---

# 🧠 Step 4 — Feature Engineering

The AI engine extracts features from live events:

```python
features = build_features(events)
```

Generated features:

* event_rate
* model_score
* avg_amount
* max_amount

Example:

```python
{
  "event_rate": 18,
  "model_score": 1.2,
  "avg_amount": 12000
}
```

---

# 🧠 Step 5 — Pressure Score Calculation

The platform calculates infrastructure pressure.

Event thresholds:

```python
LOW_PRESSURE_EVENTS = 5
MEDIUM_PRESSURE_EVENTS = 10
HIGH_PRESSURE_EVENTS = 15
```

Risk thresholds:

```python
MEDIUM_RISK_SCORE = 0.85
HIGH_RISK_SCORE = 0.95
```

Example logic:

```python
if event_rate >= 15:
    pressure_score += 3
```

```python
if model_score >= 0.95:
    pressure_score += 2
```

Example result:

```text
Pressure Score = 5
```

---

# 🧠 Step 6 — AI Decision Engine

The system determines platform state:

```python
if pressure_score >= 4:
    action = "SCALE"

elif pressure_score >= 2:
    action = "ELEVATED"

else:
    action = "NORMAL"
```

Possible states:

* NORMAL
* ELEVATED
* SCALE

---

# 🧠 Step 7 — Replica Recommendation

The AI engine determines replica count.

Example:

```python
if event_rate >= 30:
    replicas = 5

elif event_rate >= 20:
    replicas = 4

else:
    replicas = 3
```

The final value becomes:

```text
ai_target_replicas = 3
```

---

# 🧠 Step 8 — Prometheus Metrics Export

The AI engine exports custom metrics:

```python
ai_target_replicas.set(replicas)
```

Prometheus scrapes metrics from:

```text
http://self-healing:8000/metrics
```

Example metric:

```text
ai_target_replicas 3
```

---

# ⚡ Step 9 — KEDA Reads Prometheus Metrics

KEDA uses a Prometheus scaler.

ScaledObject:

```yaml
triggers:
  - type: prometheus
```

Query:

```yaml
query: |
  max(ai_target_replicas)
```

KEDA continuously asks Prometheus:

> "What replica count did the AI engine recommend?"

Prometheus returns:

```text
3
```

---

# ⚡ Step 10 — KEDA Scales Argo Rollout

KEDA scales the target workload:

```yaml
scaleTargetRef:
  kind: Rollout
  name: fraud-detection
```

This updates the Argo Rollout replica count.

---

# ☸️ Step 11 — Kubernetes Creates Pods

Kubernetes scheduler creates new fraud-detection pods.

Example:

```text
fraud-detection-abc
fraud-detection-def
fraud-detection-ghi
```

Traffic is redistributed automatically through:

* Kubernetes Services
* Istio
* Envoy sidecars

---

# 🧠 Why We Used KEDA Instead of Only HPA

Traditional HPA mainly scales using:

* CPU
* memory

Our platform scales using:

* fraud event pressure
* AI anomaly scores
* Kafka traffic intensity
* predictive scaling logic
* business-level metrics

This provides smarter autoscaling decisions.

---

# 🛡️ Enterprise Stability Features

The platform also includes:

## Cooldown Protection

```python
COOLDOWN_SECONDS = 60
```

Prevents rapid scaling flapping.

---

## Safety Normalization

The AI engine normalizes scaling decisions:

```python
if action == "ELEVATED":
    replicas = 2
```

This prevents aggressive scaling.

---

## Scaling Limits

```python
MIN_REPLICAS = 1
MAX_REPLICAS = 5
```

Protects cluster stability.

---

# 🌍 Final Summary

“Our platform implements AI-driven Kubernetes autoscaling using Prometheus custom metrics and KEDA. Kafka fraud events are analyzed in real time by the self-healing engine, which calculates anomaly pressure and exports replica recommendations to Prometheus. KEDA consumes those metrics and dynamically scales Argo Rollouts on Kubernetes.”
