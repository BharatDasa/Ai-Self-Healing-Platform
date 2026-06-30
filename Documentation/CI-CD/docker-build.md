# Docker Build Process

## Images

### Fraud Detection

```bash
docker build \
-t bharatdasa/fraud_ai_ml:latest .
```

---

### Self-Healing

```bash
docker build \
-t bharatdasa/self-healing_ai_ml:v2 .
```

---

### Transaction Simulator

```bash
docker build \
-t bharatdasa/transaction-simulator:v1 .
```

---

### Enterprise Airflow

```bash
docker build \
-t bharatdasa/enterprise-airflow:latest .
```

---

## Verify Images

```bash
docker images
```

---

## Benefits

- Immutable deployments
- Version control
- Reproducibility