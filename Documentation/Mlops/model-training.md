# Model Training

The platform trains two models.

## Fraud Detection Model

Purpose:

Classify suspicious transactions.

Features:

* amount
* event velocity
* anomaly count

Output:

```text
fraud_model.pkl
```

Model:

Random Forest Classifier

---

## Scaling Prediction Model

Purpose:

Predict Kubernetes replicas.

Features:

* event_rate
* model_score

Output:

```text
scaling_model.pkl
```

Model:

Regression model

---

## Training Flow

```text
Raw Events
    ↓
Feature Engineering
    ↓
Model Training
    ↓
Validation
    ↓
Save Model
    ↓
NFS Storage
```

Models are shared through NFS and consumed by the self-healing engine.
