# Trivy Security Scanning

## Overview

Trivy performs image vulnerability scanning before deployment.

---

## Images

- fraud_ai_ml
- self-healing_ai_ml
- transaction-simulator
- enterprise-airflow

---

## Scan Levels

- HIGH
- CRITICAL

---

## Example

```bash
trivy image \
--severity HIGH,CRITICAL \
bharatdasa/fraud_ai_ml:latest
```

---

## Jenkins Stage

```bash
trivy image \
--severity HIGH,CRITICAL \
--exit-code 0 \
IMAGE_NAME
```

---

## Benefits

- CVE detection
- Supply chain security
- Secure deployment