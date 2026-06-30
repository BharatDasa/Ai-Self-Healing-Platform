# Deployment Guide

## Deployment Workflow

```text
GitHub
    ↓
Jenkins Pipeline
    ↓
Docker Build
    ↓
Trivy Scan
    ↓
DockerHub Push
    ↓
Kubernetes Deploy
    ↓
Argo Rollouts
    ↓
KEDA Scaling
    ↓
Production Platform
```

---

# Build Images

```bash
./scripts/build.sh
```

---

# Create Kafka Topics

```bash
./scripts/create-topics.sh
```

---

# Deploy Platform

```bash
./scripts/deploy.sh
```

---

# Deploy Airflow

```bash
cd ml-pipelines

./deploy-ml-pipelines.sh
```

---

# Verify

```bash
kubectl get pods -A

kubectl get svc -A

kubectl get rollout -A

kubectl get scaledobject -A
```

---

# Verify Argo Rollouts

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

# Verify Airflow

```bash
kubectl get pods -n airflow

airflow dags list
```

---

# Platform Components

* Kafka
* MongoDB
* PostgreSQL
* Airflow
* Prometheus
* Grafana
* Loki
* Tempo
* Alertmanager
* Istio
* KEDA
* Argo Rollouts
* Self-Healing Engine
* Fraud Detection Service
