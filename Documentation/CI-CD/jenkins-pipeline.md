# Jenkins Enterprise Pipeline

## Overview

The platform uses Jenkins for end-to-end CI/CD automation.

---

## Pipeline Stages

1. Checkout Repository
2. Verify DevOps Toolkit
3. Validate Services
4. Validate Airflow DAGs
5. Build Docker Images
6. Trivy Security Scanning
7. DockerHub Login
8. Push Images
9. Deploy Kubernetes Resources
10. Verify Readiness
11. Verify Airflow
12. Enterprise Validation
13. Chaos Engineering
14. Cleanup

---

## Images Built

- fraud_ai_ml
- self-healing_ai_ml
- transaction-simulator
- enterprise-airflow

---

## Components Verified

- Argo Rollouts
- KEDA
- HPA
- Airflow
- Kafka
- Prometheus

---

## Pipeline Trigger

GitHub Push

↓

Jenkins

↓

Build

↓

Security Scan

↓

Deploy

↓

Validate

↓

Production