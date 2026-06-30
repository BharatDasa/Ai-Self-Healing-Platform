# Istio Gateway

## Overview

Istio Gateway acts as the north-south traffic entry point.

It connects:

```text
Internet
    ↓
Ingress Controller
    ↓
Istio Gateway
    ↓
VirtualService
    ↓
Platform Services
```

---

# Responsibilities

* external access
* HTTP routing
* HTTPS support
* TLS termination
* traffic entry into mesh

---

# Platform Endpoints

## Fraud Detection

```text
fraud.platform.local
```

---

## Airflow

```text
airflow.platform.local
```

---

## Grafana

```text
grafana.platform.local
```

---

## Prometheus

```text
prometheus.platform.local
```

---

# TLS Integration

Istio Gateway integrates with:

* cert-manager
* wildcard certificates
* Kubernetes secrets

---

# Gateway Flow

```text
User Request
      ↓
Wildcard DNS
      ↓
Ingress Controller
      ↓
Istio Gateway
      ↓
VirtualService
      ↓
Services
      ↓
Pods
```

---

# Verify Gateway

List Gateways:

```bash
kubectl get gateway -A
```

Describe:

```bash
kubectl describe gateway
```

---

# Benefits

Istio Gateway provides:

* centralized traffic entry
* HTTPS support
* scalable architecture
* production-grade ingress
* secure external connectivity

---

# Networking Stack

```text
Wildcard DNS
       ↓
Ingress Controller
       ↓
Istio Gateway
       ↓
VirtualService
       ↓
Services
       ↓
Envoy Sidecars
       ↓
Applications
```

The Istio Gateway is the entry point into the AI Self-Healing Kubernetes Platform service mesh.
