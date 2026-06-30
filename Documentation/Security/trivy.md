# Trivy Vulnerability Scanning

## Overview

The platform uses Trivy for container image security scanning.

Trivy is integrated into the Jenkins CI/CD pipeline and scans all images before deployment.

---

## Images Scanned

- fraud_ai_ml
- self-healing_ai_ml
- transaction-simulator
- enterprise-airflow

---

## Scan Severity

The pipeline checks:

- HIGH vulnerabilities
- CRITICAL vulnerabilities

---

## Manual Scan

### Fraud Detection

```bash
trivy image bharatdasa/fraud_ai_ml:latest
```

### Self-Healing

```bash
trivy image bharatdasa/self-healing_ai_ml:v2
```

---

## Jenkins Integration

```bash
trivy image \
--severity HIGH,CRITICAL \
--exit-code 0 \
IMAGE_NAME
```

---

## Benefits

- container security
- CVE detection
- supply chain protection
- secure deployments

---

## Validation

```bash
trivy --version
```