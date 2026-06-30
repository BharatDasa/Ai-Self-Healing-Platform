# Predict Scale Logic

File:

services/self-healing/app/predict_scale.py

---

## Workflow

Events

↓

Feature Engineering

↓

ML Model

↓

Pressure Score

↓

Decision

↓

Target Replicas

---

## Features

### Event Rate

Number of events.

### Average Amount

Average transaction value.

### Maximum Amount

Highest transaction.

### Model Score

Normalized risk score.

---

## Final Actions

NORMAL

↓

1 replica

---

ELEVATED

↓

2 replicas

---

SCALE

↓

3-5 replicas

---

## Safety Limits

Minimum:

1

Maximum:

5